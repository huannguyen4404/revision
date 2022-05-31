i = 0
try:
    j = 100/i
except ZeroDivisionError as e:
    print("Division zero")
    print(e)
except Exception as e:
    print("Somethings went wrong")
    print(e)
finally:
    print("I always run.")