try:
    x = 10 / 0  # No error here
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
else:
    print("Division was successful!")
