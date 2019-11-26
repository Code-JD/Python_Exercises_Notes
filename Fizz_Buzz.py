# def fizz_buzz(max_num):
#   for num in range(1, max_num + 1):
#     if num % 3 == 0 and num % 5 == 0:
#     		print('FizzBuzz')
#     elif num % 5 == 0:
#     		print('Buzz')
#     elif num % 3 == 0:
#     		print('Fizz')
#     else:
#     		print(num)

# fizz_buzz(100)

# def fizz_buzz(max_num):
#     for num in range(1, max_num + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print(f'Fizz Buzz,')
#         elif num % 5 == 0:
#             print(f'Buzz,')
#         elif num % 3 == 0:
#             print(f'Fizz,')
#         else:
#             print(num)

# fizz_buzz(100)

# for FizzBuzz in range(101):
#     if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif FizzBuzz % 3 == 0:
#         print("Fizz")
#         continue
#     elif FizzBuzz % 5 == 0:
#         print("Buzz")
#         continue
#     print(FizzBuzz)

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)