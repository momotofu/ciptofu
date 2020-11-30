import string
import random


alphabet = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
whitespace = string.whitespace

def getKeyIndex(length):
  current_index = 0

  def increment():
    nonlocal current_index

    if current_index < length - 1:
      current_index += 1
    else:
      current_index = 0
  
  def getIndex():
    nonlocal current_index

    return current_index
  
  return [getIndex, increment]
  

def encrypt(message, key, isDev):
  outputMessage = ''
  keyLength = len(key)
  getIndex, increment = getKeyIndex(keyLength)

  for i, c in enumerate(message):
    c = c.lower()

    # Check for edge cases
    if (c in digits or c in punctuation):
      outputMessage += c
      continue

    if (c in whitespace):
      outputMessage += random.choice(digits)
      continue

    # Set char index in relation to the alphabet
    charIndex = alphabet.index(c);
    keyIndex = alphabet.index(key[getIndex()])

    if (charIndex + keyIndex >= 25):
      charIndex = charIndex - 26

    shiftedCharIndex = charIndex + alphabet.index(key[getIndex()]) + 1
    isDev and print(c, charIndex, shiftedCharIndex, getIndex())
    shiftedChar = alphabet[shiftedCharIndex]
    increment()
    
    outputMessage += shiftedChar

  return outputMessage

def decrypt(message, key, isDev):
  outputMessage = ''
  keyLength = len(key)
  getIndex, increment = getKeyIndex(keyLength)

  for i, c in enumerate(message):
    c = c.lower()

    # Check for edge cases
    if (c in digits):
      outputMessage += ' '
      continue

    if (c in punctuation):
      outputMessage += c
      continue

    # Set char index in relation to the alphabet
    charIndex = alphabet.index(c)
    keyIndex = alphabet.index(key[getIndex()])

    if (charIndex - keyIndex < 0):
      charIndex = charIndex + 25

    shiftedCharIndex = charIndex + ((alphabet.index(key[getIndex()]) + 1) * -1)
    isDev and print(charIndex, shiftedCharIndex, getIndex())
    shiftedChar = alphabet[shiftedCharIndex]
    increment()
    
    outputMessage += shiftedChar

  return outputMessage
