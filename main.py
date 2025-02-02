from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert the number to float, then check if it's an integer
        num = float(number)
        if num.is_integer():
            num = int(num)
        else:
            # Handle non-integer floating-point numbers as invalid
            raise ValueError("Non-integer values are not supported.")
        
        # Generate response for valid numbers
        properties = ["odd" if num % 2 else "even"]
        response = {
            "number": num,
            "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
            "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(abs(num))),
            "fun_fact": f"{num} is just an interesting number!"
        }
        return JSONResponse(content=response, status_code=200)
    except ValueError:
        # Handle invalid input
        error_response = {
            "number": number,
            "error": True
        }
        return JSONResponse(content=error_response, status_code=400)
