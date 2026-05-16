import cv2
import easyocr


reader = easyocr.Reader(['en'])


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    # Convert to grayscale only
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray


def extract_text(image_path):

    processed_image = preprocess_image(image_path)

    results = reader.readtext(processed_image)

    extracted_text = ""

    for result in results:
        extracted_text += result[1] + "\n"

    return extracted_text