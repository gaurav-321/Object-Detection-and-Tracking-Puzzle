# Object Detection and Tracking
This project is a real-time object detection that tracks similar objects within the same image. It can detect and highlight instances of a user-defined object in an image.

## Dependencies
- OpenCV
- NumPy
- imutils
## How to Use
Clone the repository and navigate to the directory:
```
git clone https://github.com/USERNAME/REPO.git
cd REPO
```
Run the script with the desired image file as an argument (default is "sample/odd-one-out-puzzle.png"):
```
python main.py [IMAGE_FILE]
```
- Use the mouse to define a bounding box around the object you want to detect in the image. The program will highlight all instances of the object in the image.

- Use the trackbar at the bottom of the window to adjust the sensitivity of the object detection. A higher value will result in more detections but may also include false positives.

- Press "q" to quit the program or "r" to reset the object detection.

## Customization
You can customize the object detection by adjusting the sensitivity of the detection using the trackbar. You can also modify the image file by providing a different file path as an argument when running the script.

## Acknowledgements
This project was built using the tutorial Real-time Object Detection using Template Matching with OpenCV by PyImageSearch.
