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
      if match:
        self.matches.append(match)

  def parse_matches(self):
    for i, match in enumerate(self.matches):
      if match.groupdict()["section"]:
        self.rules["section" + str(i)] = match.groupdict()["section"]
      else:
        command = re.sub(r"<", r"\<", match.groupdict()["command"])
        command = re.sub(r"\|", r"\\|", command)      
        action = re.sub(r"%\((?P<inter>\w+)\)\w", r"[\g<inter>]", match.groupdict()["action"])
        self.rules[command] = action

  def write_table(self, f):
    f.write("command | action\n")
    f.write("--- | ---\n")

  def write_definitions(self, f):
    for key, value in self.rules.iteritems():
      if re.match(r"section\d+", key) != None:
        f.write("\n## " + value + "\n\n")
        self.write_table(f)
      else:
        f.write(key + " | " + value + "\n")

  def write_dictionary(self):
    with open(self.file, "w+") as f:
      f.write("# " + self.name + "\n\n")
      self.write_table(f)
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

pattern = re.compile(r"(^\s*[\"'](?P<command>[^\"']+)[\"']:\s*(?P<action>.*),|^\s*###\s*(?P<section>\w*)\s*###)")

grammars = []
for path in grammar_paths:
  grammars += glob.glob(os.path.abspath(path + "/*.py"))

for grammar in grammars:
  Dictionary(grammar).execute()
    