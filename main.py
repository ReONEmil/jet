value = input()

if value.isdigit():
    print(f"{value} is an integer")
elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
    print(f"{value} is a float")
else:
    print(f"{value} is a string")




age = int(input())

if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")



numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)





num = int(input())

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")




count = 10

while count > 0:
    print(count, end=" ")
    count -= 1




number = int(input())

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5.")
elif number % 3 == 0:
    print("Divisible by 3.")
elif number % 5 == 0:
    print("Divisible by 5.")
else:
    print("Not divisible by 3 or 5.")




lst = [1, 3, 4, 3, 5, 3]
count = lst.count(3)
print(f"3 appears {count} times in the list.")




ages = {'Alice': 25, 'Bob': 17, 'Charlie': 20}
over_18 = [name for name, age in ages.items() if age > 18]

for name in over_18:
    print(name, end=" ")



numbers = [-2, 3, 0, 5, -7]
result = []

for num in numbers:
    if num > 0:
        result.append("Positive")
    elif num < 0:
        result.append("Negative")
    else:
        result.append("Zero")

for res in result:
    print(res, end=" ")
