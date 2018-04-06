import os.path
import glob
import re
import fileinput
from collections import OrderedDict

class Dictionary:
  def __init__(self, grammar):
    self.grammar = grammar
    self.name = os.path.basename(grammar)
    self.file = os.path.normpath("../dictionary/" + self.name + ".md")
    self.matches = []
    self.rules = OrderedDict()

  def scan_grammar(self):
    for line in fileinput.input(self.grammar):
      match = pattern.search(line)
      if match != None:
        self.matches.append(match)

  def parse_matches(self):
    for match in self.matches:
      command = re.sub(r"<", r"\<", match.group(1))
      command = re.sub(r"\|", r"\\|", command)      
      action = re.sub(r"%\((?P<inter>\w+)\)\w", r"[\g<inter>]", match.group(2))
      self.rules[command] = action

  def write_header(self, f):
    f.write("# " + self.name + "\n\n")
    f.write("command | action\n")
    f.write("--- | ---\n")

  def write_definitions(self, f):
    for command, action in self.rules.iteritems():
      f.write(command + " | " + action + "\n")

  def write_dictionary(self):
    with open(self.file, "w+") as f:
      self.write_header(f)
      self.write_definitions(f)
      f.truncate()

  def execute(self):
    self.scan_grammar()
    if self.matches == []:
      return
    self.parse_matches()
    self.write_dictionary()

os.chdir("./scripts")

grammar_paths = ["..", "../dynamics"]

pattern = re.compile(r"^\s*[\"'](?P<spoken>[^\"']+)[\"']:\s*(?P<result>.*),")

grammars = []
for path in grammar_paths:
  grammars += glob.glob(os.path.abspath(path + "/*.py"))

for grammar in grammars:
  Dictionary(grammar).execute()
    