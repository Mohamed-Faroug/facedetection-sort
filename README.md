# facedetection-sort
# Face Detection and Sorting Script

This script detects faces in images and sorts them into separate folders based on the detected individuals. It uses `face_recognition` and `OpenCV` libraries to recognize faces and organize the images.

### Features:
- **Face Detection**: Detects faces in the images using `face_recognition`.
- **Face Recognition**: Identifies unique individuals based on their facial features.
- **Folder Organization**: Moves original images into separate folders for each identified individual.
- **No Cropped Faces**: Only the original images are moved to the corresponding folders, not cropped faces.
- **Error Handling**: Skips images with no faces and continues processing the rest.

## Requirements:
- Python 3.x
- `face_recognition`
- `opencv-python`
- `shutil` (comes with Python standard library)

### Installation

1. Clone this repository or download the script to your local machine.

   ```bash
   git clone https://github.com/yourusername/facedetection-sort.git

Install the required Python libraries.

    ```bash
    pip install face_recognition opencv-python


Ensure you have an "images" folder containing the images you want to process. This folder should be in the same directory as the script.
 
How to Use
Place your images in the images folder.

Run the script by executing the following command:

    ```bash
    python face_sorter.py
The script will detect faces, recognize individuals, and move the original images into a folder for each person under the sorted_faces directory.

If the script finds multiple faces in an image, it will move the image to the folder of the person detected, based on facial recognition.

Example Folder Structure:

      ```sorted_faces/
      ├── Person_1/
      │   ├── original_image1.jpg
      ├── Person_2/
      │   ├── original_image2.jpg
      └── ...
Summary:
The original images are moved into a folder named after the identified person.
If no faces are detected, the image is skipped.
The script will create folders for new individuals as it processes the images.
License:
This project is licensed under the MIT License - see the LICENSE file for details.
