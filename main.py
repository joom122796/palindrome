word = input('Enter a word: ')
word = word.lower()
word2 = word[::-1]
if word2 == word:
  print('This is a palindrome')
else:
  print('Not a palindrome')
