from fastapi import FastAPI, HTTPException

app = FastAPI()  # This defines the app instance

@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        num = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    properties = ["odd" if num % 2 else "even"]

    response = {
        "number": num,
        "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
        "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
        "properties": properties,
        "class_sum": sum(map(int, str(num))),
        "fun_fact": f"Did you know? {num} is an interesting number!",
    }

    return response
S
