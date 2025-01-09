numbers = []
while True:
    user_input = input("Enter a number 1 Through 10 or 'Q' to stop: ").strip().upper()
    if user_input == "Q":
        break
    number = int(user_input)
    if 1 <= number <= 10:
        numbers.append(number)
    else:
        print("Invalid input: '{}'. Please enter a number between 1 and 10.".format(user_input))

print("\nThe numbers you entered were:")
for number in set(numbers):
    count = numbers.count(number)
    print("{} was entered {} time{}.".format(number, count, "s" if count > 1 else ""))
