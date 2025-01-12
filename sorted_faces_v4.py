import os
import cv2
import face_recognition
import shutil
from collections import defaultdict

# Set the input and output directories
input_folder = "images"
output_folder = "sorted_faces"

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# A dictionary to store unique face encodings and their corresponding images
known_face_encodings = []
known_face_names = []

# Function to add a new person (i.e., a new unique face)
def add_face(face_encoding, name):
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)

# Initialize a counter for the total number of images saved per person
saved_images_count = defaultdict(int)

# Process each image in the input folder
for image_file in os.listdir(input_folder):
    image_path = os.path.join(input_folder, image_file)
    
    try:
        # Load the image
        image = face_recognition.load_image_file(image_path)
        
        # Detect faces in the image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        # Skip images with no faces
        if not face_locations:
            print(f"No faces found in {image_file}")
            continue

        print(f"Found {len(face_locations)} face(s) in {image_file}")

        # Loop through each detected face
        for face_encoding in face_encodings:
            # Compare the face encoding to known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            if True in matches:
                # If we have a match, get the name of the person (first match found)
                match_index = matches.index(True)
                name = known_face_names[match_index]
            else:
                # If no match, assign a new name and add the face encoding
                name = f"Person_{len(known_face_encodings) + 1}"
                add_face(face_encoding, name)

            # Create a subfolder for the current person if it doesn't exist
            person_folder = os.path.join(output_folder, name)
            os.makedirs(person_folder, exist_ok=True)

            # Move the original image to the person's folder
            original_image_output_path = os.path.join(person_folder, f"{image_file}")
            shutil.move(image_path, original_image_output_path)  # Move (cut) the original image
            print(f"Moved original image {image_file} to {name}'s folder.")

            # Increment the saved image count for the person
            saved_images_count[name] += 1

    except Exception as e:
        print(f"Error processing {image_file}: {e}")
        continue

# Summary of the results
print("\nFace detection and recognition complete!")
for name, count in saved_images_count.items():
    print(f"{name}: {count} image(s) moved.")
