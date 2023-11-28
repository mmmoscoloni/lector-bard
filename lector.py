# Import necessary libraries
from PIL import Image
import cv2
import pytesseract

# Function to recognize text from an image
def recognize_question(image_path):
    # Use Tesseract to recognize text from the image
    question_text = pytesseract.image_to_string(Image.open(image_path))

    return question_text

# Specify the image path
image_path = 'imagenes/prueba2.jpeg'

# Recognize the question from the image
recognized_text = recognize_question(image_path)

# Print the recognized text
print(recognized_text)
