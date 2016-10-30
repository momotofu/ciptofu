# CLI

"""
  Decode
  a) prompt user for key
  b) prompt user for path to message
  c) decode message
  d) promt user for return file name and path
  e) return decoded message file

  Encode
  a) prompt user for key
  b) prompt user for path to message
  c) encode message
  d) promt user for return file name and path
  e) return encoded massage file

"""
import argparse
import string

alphabet = list(string.ascii_letters +
  string.punctuation + '\x20\n')

def createKeyMap(message, key):
  keyMap = ''
  while len(keyMap) < len(message):
    keyMap = keyMap + key
  return keyMap[:len(message)]

def encrypt(message, key):
  outputMessage = ''
  keyMap = createKeyMap(message, key)

  for i, c in enumerate(message):
    start = alphabet.index(c)
    magnitude = alphabet.index(keyMap[i])
    end = start + magnitude
    if end > len(alphabet) - 1:
      end = (len(alphabet) - end) * -1
    outputMessage += alphabet[end]

  return outputMessage

def decrypt(message, key):
  outputMessage = ''
  keyMap = createKeyMap(message, key)

  for i, c in enumerate(message):
    start = alphabet.index(c)
    magnitude = alphabet.index(keyMap[i])
    end = start - magnitude
    if end < 0:
      end += len(alphabet) - 1
    outputMessage += alphabet[end]

  return outputMessage

print alphabet.index('\x20'), len(alphabet), 'str:' + alphabet[84] + '|'

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key",
  help="Enter your alphabetic encryption key",
  type=str)
parser.add_argument("-e", "--encrypt",
  help="specify encription",
  action="store_true")
parser.add_argument("-d", "--decrypt",
  help="specify decription",
  action="store_true")
parser.add_argument("-m", "--message",
  type=file)

args = parser.parse_args()
message = args.message.read()

# if args.key:
#   print "Your key is: {}".format(args.key)
# if args.decrypt:
#   print args.decrypt
# if args.encrypt:
#   print args.encrypt

if args.message:
  print encrypt(message, args.key)
  print decrypt(encrypt(message, args.key), args.key)