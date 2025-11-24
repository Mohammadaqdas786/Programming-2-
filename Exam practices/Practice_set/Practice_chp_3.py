# Problem 1
name = input("Enter your name:")
print(f"Good afternoon {name}")

# Problem 2
letter = '''Dear <|Name|>
        You are selected! 
        <|Date|> '''

print(letter.replace("<|Name|>", "Mohammad").replace("<|Date|>", "december 1 2026"))

# Problem 3
name = "vanya is good girl and  "

print(name.find(" "))

# Problem 4
# name = "vanya is good girl and  "
#
# print(name.find(" ", " "))
# print(name)

# Problem 5
word= "Dear Mohammad,\n \tThis python course is nice.\n Thanks!"
print(word)
