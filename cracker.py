import sys
import crypt
import string

# crypt usage: crypt.crypt(key, salt)

class Cracker():
    ALPHABET = string.ascii_letters
    ALPHA_LENGTH = len(ALPHABET)
    SALT = str(50)

    def __init__(self, hashed_pass):
        self.hashed_pass = hashed_pass

    def hash_the_salt(self, word):
        crypt

    def brute_force(self):
        word = ""
        for i in range(self.ALPHA_LENGTH):
          for j in range(self.ALPHA_LENGTH):
            for k in range(self.ALPHA_LENGTH):
              for l in range(self.ALPHA_LENGTH):
                if crypt.crypt(str(word), self.SALT) == self.hashed_pass:
                  print("Match Found:")
                  print(word)
                  return 0
                word = self.ALPHABET[l] + word[1:]
              word = word[:1] + self.ALPHABET[k] + word[2:]
            word = word[:2] + self.ALPHABET[j] + word[3:]
          word = word[:3] + self.ALPHABET[i]
        print("Brute force failed")
        return 1

    def load_dictionary(self):
      input_file = open("mega_passwords.txt", 'r')
      self.all_passwords = input_file.read().split()

    def dictionary_attack(self):
      for word in self.all_passwords:
        if crypt.crypt(word, self.SALT) == self.hashed_pass or crypt.crypt(word.upper(), self.SALT) == self.hashed_pass:
          print("Match Found:")
          print(word)
          return 0
      print("Dictionary attack failed.")
      return 1

def main():
  if not len(sys.argv) == 2:
    print("Takes a password hash as an argument")
    return 0
  hash = sys.argv[1]
  cracker = Cracker(hash)
  print("Initiating brute force sequence")
  results = cracker.brute_force()
  if results == 1:
    cracker.load_dictionary()
    cracker.dictionary_attack()

if __name__ == "__main__":
    main()