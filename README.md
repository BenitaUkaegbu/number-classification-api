# Number Classification API

A FastAPI-based web service that takes a number as input and returns interesting mathematical properties, including whether the number is prime, perfect, or Fibonacci, along with other unique properties and a fun fact.

---

## Features

- Accepts a number as input via a query parameter.
- Returns a detailed JSON response with:
  - Number properties (prime, perfect, Fibonacci, Armstrong, etc.).
  - Factors of the number.
  - Sum of digits (digit sum).
  - Fun fact about the number.
- Provides appropriate error messages for invalid inputs.
- Deployed on a publicly accessible platform with fast response times.

---

## Endpoints

### 1. **Home Endpoint**
- **URL:** `/`
- **Method:** `GET`
- **Response Example:**
  ```json
  {
    "message": "Welcome to the Number Classification API!"
  }

URL: /api/classify-number
Method: GET
Query Parameter:
number (required): An integer.
Successful Response (200 OK):
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "is_fibonacci": false,
  "properties": ["armstrong", "odd"],
  "factors": [1, 7, 53, 371],
  "class_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Error Response (400 Bad Request):
{
  "number": "alphabet",
  "error": true
}

Technologies Used
Programming Language: Python
Framework: FastAPI
Deployment Platform: Render

How to Run Locally
Prerequisites
Python 3.11 or later installed.
Install dependencies from requirements.txt
pip install -r requirements.txt

Run the API
By Cloning
git clone https://github.com/BenitaUkaegbu/number-classification-api.git
cd number-classification-api

Start the FastAPI server using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

Open your browser and navigate to:

API Docs: http://127.0.0.1:8000/docs
API Home: http://127.0.0.1:8000/

Deployment
The API is publicly accessible at: Number Classification API

Example:
https://number-classification-api.onrender.com/api/classify-number?number=371
Test the API
You can test the API using tools like:

Postman
Curl
Browser (by entering query parameters in the URL)
Acceptance Criteria
Functionality
Accepts GET requests with a number parameter.
Returns the specified JSON response.
Provides appropriate error codes and messages for invalid input.
Code Quality
Organized and modular code.
Handles errors gracefully.
Avoids hardcoding where possible.
Documentation
Complete and easy-to-understand README.md.
Deployment
Publicly accessible and stable.
Fast response time (<500ms).
License
This project is open-source and available under the MIT License.


