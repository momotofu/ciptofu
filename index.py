import argparse
from app.index import encrypt, decrypt

parser = argparse.ArgumentParser()

parser.add_argument("-k", "--key", # Flags
  help="Enter your alphabetic encryption key",
  type=str)
parser.add_argument("-e", "--encrypt",
  action="store_true")
parser.add_argument("-d", "--decrypt",
  action="store_true")
parser.add_argument("--dev",
  action="store_true")
parser.add_argument("-m", "--message",
  type=str)

args = parser.parse_args()
key = args.key
message = args.message
should_encrypt = args.encrypt 
should_decrypt = args.decrypt 
isDev = args.dev

if __name__ == '__main__':
  if should_encrypt:
    print(encrypt(message, key, isDev))
  else:
    print(decrypt(message, key, isDev))