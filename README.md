# QR Code Scanner (Python + OpenCV)

A console-based Python application that detects and decodes QR codes from image files using OpenCV.

## Overview
This project focuses on understanding the basics of computer vision by working with QR code detection and decoding. The application processes image files containing QR codes and extracts the embedded information through a command-line interface.

## Features
- Load and process image files using OpenCV
- Detect QR codes present in the image
- Decode and display QR code data
- Draw bounding boxes around detected QR codes
- Save and display the processed output image

## Tech Stack
- Python
- OpenCV

## Project Structure
QR_Project/
│── main.py # Main QR code detection script
│── qr_image.png # Input QR code image
│── qr_detected.png # Output image with bounding box
│── README.md # Project documentation

## How It Works
- The user provides an image file containing a QR code
- The image is processed using OpenCV
- Detected QR code data is decoded and displayed
- A bounding box is drawn around the QR code in the output image

## Learning Outcomes
- Gained hands-on experience with OpenCV for image processing
- Learned QR code detection and decoding techniques
- Improved Python scripting and problem-solving skills
