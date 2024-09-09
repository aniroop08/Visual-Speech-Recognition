from flask import Flask, request,render_template
import tensorflow as tf

import os
import numpy as np

app = Flask(__name__)

# CTCLoss Definition

def CTCLoss(y_true, y_pred):
    batch_len = tf.cast(tf.shape(y_true)[0], dtype="int64")
    input_length = tf.cast(tf.shape(y_pred)[1], dtype="int64")
    label_length = tf.cast(tf.shape(y_true)[1], dtype="int64")

    input_length = input_length * tf.ones(shape=(batch_len, 1), dtype="int64")
    label_length = label_length * tf.ones(shape=(batch_len, 1), dtype="int64")

    loss = tf.keras.backend.ctc_batch_cost(y_true, y_pred, input_length, label_length)
    return loss

# Loading Model

with tf.keras.utils.custom_object_scope({'CTCLoss': CTCLoss}):
    model = tf.keras.models.load_model('models/model.keras', compile=False)

# Defining vocab for string generation

vocab = [x for x in "abcdefghijklmnopqrstuvwxyz'?!123456789 "]
char_to_num = tf.keras.layers.StringLookup(vocabulary=vocab, oov_token="")
num_to_char = tf.keras.layers.StringLookup(vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True)


# Data Loader

def load_data(path:str):
    path = bytes.decode(path.numpy())
    frames = np.load(path)
    frames = tf.cast(frames,tf.float32)
    return frames

def mappable_function(path: str):
    result = tf.py_function(load_data, [path], tf.float32)
    return result

# Predicting videos

def model_predict(video_path):
    data = tf.data.Dataset.list_files(video_path)
    data = data.map(mappable_function)
    data = data.padded_batch(1, padded_shapes=[75,50,70,1])
    
    yhat = model.predict(data)
    decoded = tf.keras.backend.ctc_decode(yhat, [75], greedy=False)[0][0].numpy()
    predicted_text = tf.strings.reduce_join(num_to_char(decoded[0])).numpy().decode('utf-8')


    return predicted_text

# Landing page route

@app.route('/', methods=['GET'])
@app.route('/index.html')
def index():
    return render_template('index.html')

# Prediction route

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    
    video = request.form.get('videoselect')

    numpy_path = os.path.join('static/media/backend',f'{video}.npy')
    txt_path = os.path.join('static/media/backend',f'{video}.txt')
    video_path = 'static/media/video/{}.mp4'.format(video)
    
    predicted = model_predict(numpy_path)

    with open(txt_path,'r') as f:
        original = f.readline()
    
    return render_template('result.html',video_path=video_path,result=predicted,original=original)