try:
 a = int("abc")
 b = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)
 
