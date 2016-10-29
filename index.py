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

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key",
  help="Enter your alphabetic encryption key")
parser.add_argument("-e", "--encrypt",
  help="specify encription",
  action="store_true")
parser.add_argument("-d", "--decrypt",
  help="specify decription",
  action="store_true")
args = parser.parse_args()
encryptionKey = args.key
if args.key:
  print ("Your key is: %s" % encryptionKey)
if args.decrypt:
  print args.decrypt
if args.encrypt:
  print args.encrypt

# def getpass():
#   print 'fd: ' + str(fd), 'old' + str(old)
#   userKey = '{}'.format(raw_input('Enter key: '))
#   print 'your key is: ' + userKey

# getpass()