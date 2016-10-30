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

def encrypt(message, key):
  keyMap = ''
  outputMessage = ''
  while len(keyMap) < len(message):
    keyMap = keyMap + key
  keyMap = keyMap[:len(message)]

  for i, c in enumerate(message):
    start = alphabet.index(c)
    magnitude = alphabet.index(keyMap[i])
    end = start + magnitude
    if end > len(alphabet) - 1:
      end = end - len(alphabet) - 1
      if end < 0:
        end = end * - 1
    outputMessage += alphabet[end]
  return outputMessage

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
encryptionKey = args.key
message = args.message.read()
if args.key:
  print "Your key is: {}".format(args.key)
if args.decrypt:
  print args.decrypt
if args.encrypt:
  print args.encrypt
if args.message:
  print encrypt(message, args.key)