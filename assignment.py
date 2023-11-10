def print_diamond_pattern(word, n):
  if n % 2 == 0:
      n += 1

  length = len(word)
  k = 0

  for i in range(0, n // 2 + 1):
      pt = k
      print(" " * (n - i - 1), end="")
      for j in range(0, (2 * i) + 1):
          print(word[pt % length], end="")
          pt += 1
      k += 1
      print() 

  i = (n // 2) - 1

  for i in range(i, -1, -1):
      pt = k
      print(" " * (n - i - 1), end="")
      for j in range(0, (2 * i) + 1):
          print(word[pt % length], end="")
          pt += 1
      k += 1
      print()


n = int(input("INPUT: Enter the number of lines for the design: "))
print("OUTPUT:")
word = "FORMULAQSOLUTIONS"





print_diamond_pattern(word, n)