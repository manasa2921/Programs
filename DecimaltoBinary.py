def a(num):
  if num >= 1:
    a(num // 2)
  print(num % 2, end = ' ')
if __name__ == '__main__':
  dec_val = int(input("Enter a number"))
  a(dec_val)
