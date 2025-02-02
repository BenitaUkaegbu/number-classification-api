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

    # Process valid numbers (e.g., 42 or -42)
    response = {
        "number": num,
        "is_prime": False,  # Example logic for primes
        "is_perfect": False,  # Example logic for perfect numbers
        "properties": ["even" if num % 2 == 0 else "odd"],
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": f"{num} is just an interesting number!",
    }
    return JSONResponse(content=response)
