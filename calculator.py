# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def add(a, b):
    """두 수의 합을 반환합니다."""
    return a + b


def subtract(a, b):
    """a에서 b를 뺀 값을 반환합니다."""
    return a - b


def multiply(a, b):
    """두 수의 곱을 반환합니다."""
    return a * b


def divide(a, b):
    """a를 b로 나눈 값을 반환합니다.
    b가 0이면 ValueError를 발생시킵니다.
    """
    if b == 0:
        raise ValueError(f"Cannot divide by zero: divisor was {b}"
)
    return a / b