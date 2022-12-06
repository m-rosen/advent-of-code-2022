
# LEN = 4  # Part 1
LEN = 14 # Part 2

line = input()

for start in range(0, len(line)):
  success = True
  for i in range(start, start + LEN - 1):
    if line[i] in line[i + 1: start + LEN]:
      success = False

  if success:
    print(start + LEN)
    break
