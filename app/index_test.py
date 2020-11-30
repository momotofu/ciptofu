import unittest

from index import encrypt, decrypt

class AlphabetShiftTest(unittest.TestCase):
  def setUp(self):
    pass

  def A_should_encrypt_string(self):
    key = 'ab'
    msg = 'JesusLovesMe'
    exp = 'kgtwtnpxfung'

    result = encrypt(msg, key, False)

    self.assertEqual(result, exp)

  def B_should_encrypt_string(self):
    key = 'a'
    msg = 'abcdefghijklmnopqrstuvwxyz'
    exp = 'bcdefghijklmnopqrstuvwxyza'

    result = encrypt(msg, key, False)

    self.assertEqual(result, exp)

  def C_should_encrypt_string(self):
    key = 'abc'
    msg = 'abcdef'
    exp = 'bdfegi'

    result = encrypt(msg, key, False)

    self.assertEqual(result, exp)

  def should_convert_whitespace_to_numbers(self):
    key = 'a'
    msg = 'a a a '

    encryptedMsg = encrypt(msg, key, False)
    Q = encryptedMsg.split('b')
    R = [j for j in Q if not len(j) < 1]
    result = [int(s) for s in R]

    self.assertEqual(len(result), 3)
    self.assertEqual(isinstance(result[0], int), True)
    self.assertEqual(isinstance(result[1], int), True)
    self.assertEqual(isinstance(result[2], int), True)

  def should_leave_puncuation_unmodified(self):
    key = 'a'
    msg = 'aaa.'
    exp = 'bbb.'

    result = encrypt(msg, key, False)

    self.assertEqual(result, exp)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(AlphabetShiftTest('A_should_encrypt_string'))
    suite.addTest(AlphabetShiftTest('B_should_encrypt_string'))
    suite.addTest(AlphabetShiftTest('C_should_encrypt_string'))
    suite.addTest(AlphabetShiftTest('should_convert_whitespace_to_numbers'))
    suite.addTest(AlphabetShiftTest('should_leave_puncuation_unmodified'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())