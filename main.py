from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert input to an integer
        num = int(number)  # Handles negative numbers too
    except ValueError:
        # If conversion fails, return a 400 error
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Check if the number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(abs(n) ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Calculate the sum of the digits
    digit_sum = sum(int(d) for d in str(abs(num)))

    # Determine properties (odd/even and Armstrong number)
    properties = ["odd" if num % 2 else "even"]
    if sum(int(d) ** len(str(num)) for d in str(abs(num))) == abs(num):
        properties.insert(0, "armstrong")

    # Prepare fun fact using Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math?json")
        fun_fact = response.json().get("text", f"{num} is just an interesting number!")
    except:
        fun_fact = f"{num} is just an interesting number!"

    # Return the JSON response
    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": False,  # Additional logic for perfect number can be added
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
