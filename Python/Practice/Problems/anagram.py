# Anagram Checker — Return True if two strings are anagrams of each other (e.g., "listen" and "silent").

word1 = "listen"
word2 = "silent"

word1 =  sorted(word1.upper())
word2 =  sorted(word2.upper())
print(word1 == word2)

