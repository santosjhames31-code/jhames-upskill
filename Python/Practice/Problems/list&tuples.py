"""
Given a = [5, 3, 8] and b = [1, 9, 2], merge them into one list and sort in descending order.
"""
a = [5, 3, 8]
b = [1, 9, 2]
c = a + b
c.sort()
print(c)
c.sort(reverse=True)
print(c)

"""
Given words = ["hi", "hello", "hey", "greetings", "sup"], return a new list with only words longer than 4 characters.
"""
words = ["hi", "hello", "hey", "greetings", "sup"]
new_words = []
for i in range(len(words)):
    if len(words[i]) > 4:
        new_words.append(words[i])
print(new_words)

# List comphrehension
new_words = [word for word in words if len(word) > 4]
print(new_words)
