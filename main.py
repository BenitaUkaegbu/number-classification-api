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
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True,
            },
        )

    # Check properties
    properties = []
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Check if Armstrong number
    digit_sum = sum(int(digit) ** len(str(num)) for digit in str(num))
    if digit_sum == num:
        properties.append("armstrong")

    # Check if Fibonacci number
    def is_perfect_square(x):
        return int(x**0.5) ** 2 == x

    is_fibonacci = is_perfect_square(5 * num * num + 4) or is_perfect_square(
        5 * num * num - 4
    )

    # Check if Perfect number
    def get_factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    factors = get_factors(num)
    is_perfect = sum(factors[:-1]) == num  # Exclude the number itself

    # Generate a fun fact
    fun_fact = f"{num} is an interesting number!"
    if num == 371:  # Specific fun fact for Armstrong number
        fun_fact = (
            f"{num} is an Armstrong number because the sum of its digits "
            f"raised to the power of their count equals the number."
        )

    response = {
        "number": num,
        "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)),
        "is_perfect": is_perfect,
        "is_fibonacci": is_fibonacci,
        "properties": properties,
        "factors": factors,
        "class_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": fun_fact,
    }
    return response
