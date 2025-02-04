# Number Classification API

## Project Story
This project is part of the **HNG Internship Stage 1 - DevOps Task**, where the goal was to create an API that accepts a number and returns its interesting mathematical properties along with a fun fact. This API demonstrates practical usage of Python's FastAPI framework while integrating external APIs like [Numbers API](http://numbersapi.com/) to fetch fun facts dynamically.

The objective was to:
- Understand and implement RESTful APIs.
- Practice input validation and error handling.
- Learn how to deploy a stable, publicly accessible API.

---

## Features
- Accepts a number as input and returns its **mathematical properties**:
  - Is it **prime**?
  - Is it **perfect**?
  - Is it an **Armstrong number**?
  - Is it part of the **Fibonacci sequence**?
  - Is it **odd** or **even**?
- Provides a **digit sum** (sum of its digits).
- Lists all the **factors** of the number.
- Fetches a **fun fact** about the number using the [Numbers API](http://numbersapi.com/).

---

## Endpoints

### **Base URL**
https://number-classification-api.onrender.com/

### **1. Endpoint: `/api/classify-number`**
Classifies a number based on its properties and fetches a fun fact.

#### **Request Parameters**
| Parameter | Type   | Description               |
|-----------|--------|---------------------------|
| `number`  | string | The number to classify.   |

#### **Success Response**
**Status Code:** `200 OK`
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "is_fibonacci": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "factors": [1, 7, 53, 371],
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Error Response
Status Code: 400 Bad Request
{
    "number": "alphabet",
    "error": true
}
Examples
1. GET Request:
https://number-classification-api.onrender.com/api/classify-number?number=371
2. Output:
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "is_fibonacci": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "factors": [1, 7, 53, 371],
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Technologies Used
FastAPI: To build the API.
Uvicorn: ASGI server for serving the app.
Numbers API: For fetching fun facts dynamically.
Python: The primary programming language.

Deployment
The API is deployed on Render and is accessible at:
https://number-classification-api.onrender.com

Author
 Benita Ukaegbu


