# Object-Detection-and-Tracking-Puzzle

## Description
Object-Detection-and-Tracking-Puzzle is a Python program designed for real-time object detection and tracking within images, specifically targeting user-defined objects using template matching. This tool simplifies the process of identifying and highlighting instances of a target object in an image.

## Features
- Real-time object detection and tracking.
- User-friendly interface with adjustable sensitivity thresholds.
- Ability to manually select reference images for detection.
- Saves detected locations for further analysis or processing.

## Installation
To use this program, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install opencv-python numpy imutils
```

## Usage
Here's a basic example of how to run and use the program:

```python
# Import necessary libraries
import cv2
import numpy as np
from imutils import resize

# Initialize the ObjectDetector class with your reference image
ref_image = cv2.imread('path_to_reference_image.jpg')
detector = ObjectDetector(ref_image)

# Load the input image where you want to detect objects
input_image = cv2.imread('path_to_input_image.jpg')

# Perform object detection and tracking
output_image, locations = detector.detect(input_image)

# Display the output image with detected objects highlighted
cv2.imshow('Object Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Configuration
The program uses a trackbar to dynamically adjust the sensitivity threshold for object detection. The default value can be set in the `main.py` file.

## Tests
No tests are currently available for this project. However, you can manually test the functionality by running the script with different images and adjusting the sensitivity threshold.

## Project Structure
```
Object-Detection-and-Tracking-Puzzle/
├── main.py
└── README.md
```

## Contributing
Contributions to Object-Detection-and-Tracking-Puzzle are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Owner:** gag3301v  
[GitHub Repository](https://github.com/gag3301v/Object-Detection-and-Tracking-Puzzle)