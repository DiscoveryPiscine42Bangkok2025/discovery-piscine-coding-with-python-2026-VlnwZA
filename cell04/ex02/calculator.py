num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 // num2 if num2 != 0 else 'ใส่ศูนย์ทำพรื่อมันจะหารยังไง'}")
print(f"{num1} * {num2} = {num1 * num2}")