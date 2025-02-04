from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert to integer
        num = int(number)
    except ValueError:
        # Return 400 status code with the error JSON
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
        )

    # Determine if the number is odd or even
    properties = ["even" if num % 2 == 0 else "odd"]

    # Check if the number is an Armstrong number
    digit_powers_sum = sum(int(digit) ** len(str(abs(num))) for digit in str(abs(num)))
    if num == digit_powers_sum:
        properties.insert(0, "armstrong")  # Add "armstrong" to the properties list

    # Construct the response
    response = {
        "number": num,
        "is_prime": False,  # Example logic for primes
        "is_perfect": False,  # Example logic for perfect numbers
        "properties": properties,  # Updated properties logic
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": f"{num} is just an interesting number!",
    }
    return JSONResponse(content=response)

