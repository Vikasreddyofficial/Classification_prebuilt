# classify_cat_dog/model
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
import re

# Load the prebuilt MobileNetV2 model
model = MobileNetV2(weights='imagenet')

def fetch_wikipedia_facts(keyword, num_facts=10):
    # Wikipedia API URL for search
    search_url = "https://en.wikipedia.org/w/api.php"

    # Parameters for the API call
    search_params = {
        "action": "query",
        "list": "search",
        "format": "json",
        "srsearch": keyword
    }

    # Make the search API request
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    # Check if there are any search results
    search_results = search_data.get("query", {}).get("search", [])
    if not search_results:
        return ["No description available from Wikipedia."]

    # Get the first search result title
    first_title = search_results[0]["title"]

    # Wikipedia API URL for fetching page content
    page_url = "https://en.wikipedia.org/w/api.php"

    # Parameters for fetching page content
    page_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": first_title
    }

    # Make the page content API request
    page_response = requests.get(page_url, params=page_params)
    page_data = page_response.json()

    # Extract page information
    pages = page_data.get("query", {}).get("pages", {})
    facts = []

    for page_id, page in pages.items():
        if "extract" in page:
            # Split the extract into sentences and select the first few as facts
            sentences = page["extract"].split('. ')
            for sentence in sentences[:num_facts]:
                stripped_sentence = sentence.strip()
                if stripped_sentence:  # Check if the sentence is not empty
                    facts.append(stripped_sentence)

    # Fallback if facts are empty
    if not facts:
        facts = ["No description available from Wikipedia."]

    return facts[:num_facts]

def clean_class_name(class_name):
    # Replace underscores with spaces
    cleaned_name = re.sub(r'_', ' ', class_name)
    return cleaned_name.strip()

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    results = []
    for pred in decoded_predictions:
        object_name = pred[1]
        cleaned_name = clean_class_name(object_name)
        facts = fetch_wikipedia_facts(cleaned_name)
        results.append({
            "class_name": cleaned_name,
            "class_description": facts,
            "score": float(pred[2])
        })

    return results

# Example usage
if __name__ == "__main__":
    img_path = 'path_to_your_image.jpg'  # Replace with your image path
    results = classify_image(img_path)
    print(results)
