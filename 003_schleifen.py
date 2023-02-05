def for_loop():
  sum = 0
  for i in range(0,21, 2):
    print(i)
    sum += i
  print(f"{sum = }")
def while_loop():
  sum = 0
  i = 0
  while i <21:
    print(i)
    sum += i
    i += 2
  print(f"{sum = }")
if __name__ == "__main__":
  while_loop()