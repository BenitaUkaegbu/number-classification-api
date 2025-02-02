from fastapi.responses import JSONResponse  # Import this for custom JSON responses
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert to integer
        num = int(number)
    except ValueError:
        # For invalid inputs, return 400 Bad Request with appropriate JSON
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
        )

    # Process valid numbers (add your logic here)
    response = {
        "number": num,
        "is_prime": False,  # Example field
        "is_perfect": False,  # Example field
        "properties": ["even" if num % 2 == 0 else "odd"],  # Example field
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": f"{num} is just an interesting number!",
    }
    return response
