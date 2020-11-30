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
parser.add_argument("-ifp", "--inFilePath",
  type=str)
parser.add_argument("-ofp", "--outFilePath",
  type=str)

args = parser.parse_args()
key = args.key
message = args.message

should_encrypt = args.encrypt
should_decrypt = args.decrypt
isDev = args.dev

inFilePath = args.inFilePath
outFilePath = args.outFilePath

if __name__ == '__main__':
  if should_encrypt:
    if inFilePath:
        file = open(inFilePath, 'r')
        fileMessage = file.read()
        file.close()

        encryptedMessage = encrypt(fileMessage, key, isDev)

        if outFilePath:
            outFile = open(outFilePath, 'w')
            outFile.write(encryptedMessage)
            outFile.close()
        else:
            print(encryptedMessage)
    else:
        encryptedMessage = encrypt(message, key, isDev)
        print(encryptedMessage)

  else:
    if inFilePath:
        file = open(inFilePath, 'r')
        fileMessage = file.read()
        file.close()

        decryptedMessage = decrypt(fileMessage, key, isDev)

        if outFilePath:
            outFile = open(outFilePath, 'w')
            outFile.write(decryptedMessage)
            outFile.close()
        else:
            print(decryptedMessage)
    else:
        decryptedMessage = decrypt(message, key, isDev)
        print(decryptedMessage)

