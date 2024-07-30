
# Classifier_Pretrained_model Project
## Overview

Classify Cat Dog is a Django-based project designed to classify images of cats and dogs using a pre-trained MobileNetV2 model. The application allows users to upload images and receive predictions of the object depicted, along with some interesting facts fetched from Wikipedia.

# Features
- Image Upload: Upload images via a REST API to classify them.
- Image Classification: Utilizes MobileNetV2 for image classification.
- Wikipedia Facts: Fetches and displays interesting facts about the predicted object from Wikipedia.
- API Documentation: Swagger UI for easy API exploration.


# Installation
## Prerequisites
- Python 3.8 or later
- Django 4.2.13
- PostgreSQL 
- Virtualenv  (for virtual environment management)

For the full list of dependencies, refer to the requirements.txt file.

1. Clone the repository:

```bash
  git clone https://github.com/Vikasreddyofficial/Classification_prebuilt.git
  cd Classification_prebuilt
```
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate 

```
3. Install Dependencies

```bash
pip install -r requirements.txt

```
4. Set up the PostgreSQL database:

- Ensure you have PostgreSQL installed and running.

5. Apply the migrations:

```bash
python manage.py migrate

```

6. Create a superuser(optinal)

```bash
python manage.py createsuperuser

```

7. Run the development server:

```bash
python manage.py runserver

```
Access the application at http://localhost:8000/


# Configuration

## API Documentation:

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc UI: http://127.0.0.1:8000/redoc/


## API Endpoints
Here's a list of available API endpoints in the project:

1. Image Upload and Classification

- Endpoint: /api/upload-and-classify/
- Method: POST
- Description: Upload an image for classification. The response includes the top prediction and a list of facts from Wikipedia.

Response:

```bash
{
  "top_prediction": {
    "class_name": "Egyptian cat",
    "class_description": [
      "The Egyptian cat is a cat breed that originated in Egypt.",
      "It is known for its grace and beauty."
    ],
    "score": 0.9567
  },
  "image_url": "/media/images/your_image.jpg"
}

```

2. List Uploaded Images

- Endpoint: /api/images/
- Method: GET
- Description: Retrieve a list of uploaded images.

3. Retrieve Image Details

- Endpoint: /api/images/{id}/
- Method: GET
- Description: Retrieve details for a specific uploaded image.



## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Acknowledgements
- Django - The web framework used.
- Django REST Framework - For building the API.
- drf-yasg - For generating API documentation.
- Wikipedia API for fetching object descriptions.
- TensorFlow for providing the MobileNetV2 pre-trained model.

## License
This project is licensed under the MIT License - see the LICENSE file for details