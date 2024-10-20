# Visual Speech Recognition

## Table of Contents
- [Introduction](#introduction)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Visual Speech Recognition is the process of understanding speech by visually interpreting the movements of the lips, jaw, and tongue. It plays a crucial role in scenarios where audio is not available or clear, such as noisy environments or for individuals with hearing impairments. This project aims to develop a deep learning model for Visual Speech Recognition using TensorFlow.

The GridCorpus dataset consists of videos of speakers reciting a fixed set of sentences. Each video includes both the audio and video of the speaker's face. This dataset is commonly used for training Visual Speech Recognition models due to its size and variety of speakers.

This project implements a Visual Speech Recognition deep learning model using TensorFlow. The model is trained on the GridCorpus dataset to recognize spoken words from lip movements. Additionally, it provides a web interface built using HTML, Bootstrap CSS for styling, and Flask as the backend.

The web interface allows users to upload videos containing speech to be processed by the Visual Speech Recognition model. The model then predicts the spoken words based on the lip movements in the video. The interface provides a user-friendly way to interact with the model without requiring any knowledge of machine learning or programming.

## Screenshots
![Annotation 2024-10-20 092002](https://github.com/user-attachments/assets/a5edc04d-3f75-4c0b-9b12-6ae30907841c)

![Annotation 2024-10-20 092208](https://github.com/user-attachments/assets/0fea95c1-8c3b-4b73-801f-718df60404f4)

![Annotation 2024-10-20 093000](https://github.com/user-attachments/assets/ab474d2a-d8e8-4e73-8432-4a6b8bb1acd8)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/akashchatterjee3502/lip-reading.git
   cd lip-reading
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```bash
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Choose a video from the dropdown menu.

4. Wait for the model to process the video and display the predicted words.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code lints without errors.
4. Commit your changes and push them to your fork.
5. Submit a pull request with a detailed description of your changes.

