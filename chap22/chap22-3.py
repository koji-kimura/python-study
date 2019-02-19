def palindorome(word):
  word = word.lower()
  return word[::-1] == word

print(palindorome("Mother"))
print(palindorome("Mom"))