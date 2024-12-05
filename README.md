# LicensePlateOCR

A Python program that leverages Tesseract OCR and OpenCV to detect and predict license plates from images. It compares the predicted results with actual license plate values and calculates the prediction accuracy.

## Features

- Reads license plate images from a specified folder.
- Extracts license plate text using Tesseract OCR.
- Cleans and processes OCR results for better accuracy.
- Compares predicted license plate text with actual values.
- Calculates and displays prediction accuracy for each image.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.8 or higher
- Tesseract OCR ([Installation Guide](https://github.com/tesseract-ocr/tesseract))
- OpenCV
- pytesseract
- glob

Install the required Python packages using:

```bash
pip install opencv-python pytesseract
