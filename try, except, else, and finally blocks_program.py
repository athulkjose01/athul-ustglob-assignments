try:
 num = 5
 print(num / 1)
except Exception:
 print("Something went wrong")
else:
 print("No error occurred")
finally:
 print("This block always runs")
