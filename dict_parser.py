#!/usr/bin/env python3
import sys
import string
import pdb


class DictionaryParser:
  def __init__(self, output_file):
    self.output_file = output_file
    self.input_files = []
    self.all_passwords = []

  def add_source(self, input_file):
    self.input_files.append(input_file)

  def load_words(self):
    for file in self.input_files:
      current_file = open(file, "r")
      words = current_file.read().split()
      for word in words:
        if len(word) < 6 and all(char.isalpha() for char in word):
          self.all_passwords.append(word)
      
      current_file.close()

  def write_words(self):
    output_file = open(self.output_file, "a")
    password_string = "\n".join(self.all_passwords)
    output_file.write(password_string)
    output_file.close

def main():
  if not len(sys.argv) == 2:
    print("Incorrect usage. Takes an output.txt argument")
    return 1
  dict_gen = DictionaryParser(sys.argv[1])
  print("Time to generate a dictionary of passwords.")
  print("Enter .txt files to be parsed, then enter done" )
  while(True):
    user_input = input("Please enter a .txt file in the same directory or enter done: \n")
    if user_input.lower() == "done":
      break
    dict_gen.add_source(user_input)
  dict_gen.load_words()
  dict_gen.write_words()
  print("File created.")
  return 0

if __name__ == "__main__":
    main()