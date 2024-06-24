def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")

    return dividend / divisor

grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print("There are no grades")
except ValueError:
    print("Value Error")
else:
    print(f"Average grade: {average}")
finally:
    print("Done")
