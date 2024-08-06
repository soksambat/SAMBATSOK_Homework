# Q1
word = input("Enter a word: ")
n = int(input("Enter a number: "))
if word == "good" and 7 <= n <= 15:
    print("it's good")
elif word == "bad" and (n < 7 or n > 15):
    print("it's bad")
else:
    print("conditions not met")
