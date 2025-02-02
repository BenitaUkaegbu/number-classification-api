from fastapi import FastAPI, HTTPException

app = FastAPI()  # Defines the app instance

@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        num = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail={"error": "Invalid input. Please provide a valid integer."}
        )

    # Determine basic properties
    is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, num) if num % i == 0) == num
    is_fibonacci = is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)
    properties = ["even" if num % 2 == 0 else "odd"]
    factors = [i for i in range(1, num + 1) if num % i == 0]

    # Fun facts
    fun_facts = {
        0: "Zero is the only real number that is neither positive nor negative!",
        1: "One is the multiplicative identity.",
        42: "42 is the answer to the ultimate question of life, the universe, and everything!",
        5: "Did you know? 5 is a Fibonacci number!",
    }
    fun_fact = fun_facts.get(num, f"{num} is an interesting number!")

    response = {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "is_fibonacci": is_fibonacci,
        "properties": properties,
        "factors": factors,
        "class_sum": sum(map(int, str(num))),
        "fun_fact": fun_fact,
    }

    return response


# Utility function to check perfect square
def is_perfect_square(n: int) -> bool:
    root = int(n**0.5)
    return root * root == n

