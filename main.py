user_input = input("Biror matn kiriting: ")
if user_input == user_input[::-1]:
    print('Palindrom soz')
else:
    print('palindrom soz emas')
user_input = int(input("Bir son kiriting: "))

if user_input % 2 == 0:
    print("Juft son")
else:
    print("Toq son")
