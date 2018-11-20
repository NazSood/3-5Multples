total = 0

for i in range(1, 1000):
  result3 = i % 3
  result5 = i % 5

  if (result3 == 0) or (result5 == 0):
    total += i
    print(" Total: {:d} " .format(total))


