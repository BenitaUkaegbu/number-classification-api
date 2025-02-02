from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()  # This defines the app instance


def is_armstrong(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = list(map(int, str(number)))
    return sum(d ** len(digits) for d in digits) == number


def get_factors(number: int) -> list:
    """Get all factors of the number."""
    return [i for i in range(1, number + 1) if number % i == 0]


@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API!"}


@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        num = int(number)  # Convert input to integer
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, num) if num % i == 0) == num
    digit_sum = sum(map(int, str(num)))
    armstrong = is_armstrong(num)
    even = num % 2 == 0

    # Determine properties
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append("even" if even else "odd")

    # Fetch fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math")
        if response.status_code == 200:
            fun_fact = response.text
        else:
            fun_fact = "No fun fact available for this number."
    except requests.RequestException:
        fun_fact = "Error fetching fun fact."

    # Build the response
    response = {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "is_fibonacci": is_fibonacci(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "factors": get_factors(num),
        "fun_fact": fun_fact,
    }
    return response


def is_fibonacci(n: int) -> bool:
    """Check if a number is a Fibonacci number."""
    x1, x2 = 5 * (n ** 2) + 4, 5 * (n ** 2) - 4
    return any(x ** 0.5 == int(x ** 0.5) for x in (x1, x2))

