# GestureGenius: Virtual Cursor Commander

## Overview
GestureGenius transforms your standard webcam into a touchless virtual cursor controller with high precision and real-time responsiveness. This project leverages powerful computer vision libraries—OpenCV and Mediapipe—to track hand gestures and seamlessly translate them into on-screen actions like clicks, movements, and scrolling via PyAutoGUI.

Designed for accessibility, gaming, smart environments, and interactive displays, GestureGenius pushes the boundaries of modern human-computer interaction, offering a futuristic and intuitive alternative to traditional input devices.

---

## Table of Contents
1. [Features](#1-features)
2. [Motivation](#2-motivation)
3. [Installation](#3-installation)
   - [Prerequisites](#31-prerequisites)
   - [Clone the Repository](#32-clone-the-repository)
   - [Install Required Packages](#33-install-required-packages)
   - [Hardware Requirements](#34-hardware-requirements)
4. [Usage](#4-usage)
   - [Step 1: Connect Your Webcam](#41-step-1-connect-your-webcam)
   - [Step 2: Run the Code](#42-step-2-run-the-code)
   - [Step 3: Interact with Gestures](#43-step-3-interact-with-gestures)
   - [Step 4: Exit the Program](#44-step-4-exit-the-program)
5. [Methodology](#5-methodology)
6. [Applications](#6-applications)
7. [Future Plans](#7-future-plans)
8. [Contributions](#8-contributions)
9. [License](#9-license)
10. [Literature Survey & References](#10-literature-survey--references)

---

## 1. Features
- **Hand Gesture Recognition**: Detect hand movements via webcam.
- **Real-time Cursor Control**: Use gestures to control the cursor and perform actions like clicking and scrolling.
- **No Specialized Hardware Needed**: Works with standard webcams.
- **Cross-Platform Compatibility**: Supports Windows, Linux, and macOS.
- **Seamless Integration**: Designed for accessibility, gaming, presentations, and more.

## 2. Motivation
Traditional input devices—like keyboards and mice—create a barrier between users and digital content. Gesture-based interfaces bring a natural, immersive experience, especially beneficial for users with accessibility needs, or in gaming, smart displays, and automotive control systems. GestureGenius provides a smooth, touch-free solution to empower modern interactions.

## 3. Installation

### 3.1 Prerequisites
Ensure that Python 3.x is installed. You can get it from [Python's official website](https://www.python.org/downloads/).

### 3.2 Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/achyuth-2308/GestureGenius-Virtual-Cursor-Commander.git
cd GestureGenius-Virtual-Cursor-Commander
```

### 3.3 Install Required Packages
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```
Or install them individually:
```bash
pip install opencv-python mediapipe pyautogui
```

### 3.4 Hardware Requirements
- **Webcam**: Any standard webcam (built-in or external).
- **Processor**: Intel i3 or higher (i5 or above recommended).
- **RAM**: 4GB or more.
- **Operating System**: Windows, Linux, or macOS.

---

## 4. Usage

### 4.1 Step 1: Connect Your Webcam
Ensure your webcam is connected and operational.

### 4.2 Step 2: Run the Code
Open your terminal and navigate to the project folder. Run the following command:
```bash
python gesturegenius.py
```

### 4.3 Step 3: Interact with Gestures
Once the webcam feed is live:
- **Move Cursor**: Move your hand to control the cursor.
- **Click**: Pinch your fingers together for a mouse click.
- **Scroll**: Swipe your hand up or down to scroll.

### 4.4 Step 4: Exit the Program
Press `Ctrl + C` in your terminal to stop the program.

---

## 5. Methodology

GestureGenius relies on a sophisticated pipeline:
- **Hand Detection**: OpenCV processes the video input from your webcam and detects hand regions.
- **Landmark Extraction**: Mediapipe identifies 21 key hand landmarks, allowing precise tracking.
- **Gesture Recognition**: Custom algorithms interpret gestures (e.g., pinch for clicks, swipes for scrolling).
- **Cursor Mapping**: PyAutoGUI converts gestures into system-wide actions, such as mouse movement and scrolling.

---

## 6. Applications
- **Accessibility**: Assist individuals with disabilities to control their computer through gestures.
- **Interactive Displays**: Enable touch-free interactions in kiosks and public systems.
- **Gaming**: Adds an immersive element to gameplay by controlling the environment using gestures.
- **Presentations**: Navigate slides with hand gestures during business or academic presentations.
- **Automotive Interfaces**: Enable gesture controls for infotainment systems in vehicles.
- **Smart Home Systems**: Control smart home displays or devices without touching a screen.

---

## 7. Future Plans
- **Expand Gesture Set**: Add more complex gestures like multi-finger movements or 3D gestures.
- **Improve Accuracy**: Integrate machine learning models to further improve detection and reduce false positives.
- **Cross-Application Support**: Expand support to game engines, automotive interfaces, and smart home systems.

---

## 8. Contributions
We’re excited to collaborate! Feel free to open issues, submit pull requests, or suggest new features. Let's push the boundaries of human-computer interaction together.

---

## 9. License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 10. Literature Survey & References
Gesture recognition and computer vision have become pivotal in enhancing human-computer interaction. Libraries like OpenCV and Mediapipe have democratized access to these technologies, making gesture-based interfaces feasible for everyday users without requiring specialized hardware.

### Key Literature:
- **Zhang, Z.** (2021). Hand Tracking in Computer Vision Using Mediapipe. _International Journal of Computer Vision_.
- **Bradski, G.** (2000). The OpenCV Library. _Dr. Dobb’s Journal of Software Tools_.
- **Raffel, C.** (2020). Gesture Recognition: A Comprehensive Survey. _IEEE Transactions on Human-Machine Systems_.
- **Gutierrez, M.** (2022). Human-Computer Interaction through Vision-Based Systems. _ACM Computing Surveys_.

---
This repository hosts the code and documentation for GestureGenius: Virtual Cursor Commander. Contributions and feedback are highly encouraged as we push the boundaries of hands-free, gesture-based interaction for a smarter, touchless future!
