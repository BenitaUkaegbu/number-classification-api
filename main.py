from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from math import pow

app = FastAPI()

def is_armstrong(num: int) -> bool:
    digits = [int(d) for d in str(num)]
    return num == sum(pow(d, len(digits)) for d in digits)

@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        num = int(number)  # Ensure input is an integer
    except ValueError:
        # Return an error response for invalid inputs
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True
            }
        )

    # Calculate properties
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 != 0 else "even")

    # Construct response
    response = {
        "number": num,
        "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
        "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
        "is_fibonacci": False,  # Optional: Calculate Fibonacci if needed
        "properties": properties,
        "factors": [i for i in range(1, num + 1) if num % i == 0],
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": f"{num} is an Armstrong number because " +
                    f"{'+'.join([f'{d}^{len(str(num))}' for d in str(num)])} = {num}"
        if "armstrong" in properties else f"{num} is just an interesting number!"
    }

    return JSONResponse(content=response, status_code=200)
