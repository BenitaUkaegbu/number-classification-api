from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert input to integer
        num = int(float(number))
        # Additional checks if required to ensure it's a valid integer
        if float(number) != num:
            raise ValueError
    except ValueError:
        # Raise an HTTPException for invalid input
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Process valid number
    properties = ["even" if num % 2 == 0 else "odd"]
    response = {
        "number": num,
        "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
        "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
        "properties": properties,
        "digit_sum": sum(map(int, str(abs(num)))),
        "fun_fact": f"{num} is just an interesting number!"
    }
    return response
