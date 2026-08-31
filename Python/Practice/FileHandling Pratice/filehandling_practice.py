import os

path = "notes.txt"

with open(path, "w") as file:
    file.write("hello\n")
    file.write("hello\n")
    file.write("hello\n")

with open(path, "a") as file:
    file.write("world hello\n")

char_count = 0
lines = 0
word_count = 0

with open(path, "r") as file:
    content = file.read()
    print(content)

    word_list = content.split() #turned into list
    word_count = len(word_list) 

    line_list = content.strip().splitlines() #create a list from break lines

    for line in line_list: #line count
            lines += 1

    chars = content.replace(" ", "").replace("\n", "") #removed spaces and '\n'

    for char in chars:
        char_count += 1
  
print("char :", char_count )
print("line :", lines)
print("word :", word_count)
#line 
#word
#character