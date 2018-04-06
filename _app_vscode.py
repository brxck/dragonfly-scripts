"""A command module for Dragonfly, for controlling Visual Studio Code.

-----------------------------------------------------------------------------
Licensed under the LGPL3.

"""

from dragonfly import AppContext, Grammar, MappingRule, Dictation, Pause, Function, IntegerRef

from aenea import (
    Key,
    Text,
)

import lib.format

mapping = {

    # Files
    "[open] command palette": Key("cs-p"),
    "(open [file] | Go to [tab]) [<text>]": Key("c-p") + Text("%(text)s"),
    "open folder": Key("c-k/3, c-s"),
    "save file": Key("c-s"),
    "save and close": Key("c-s/10, c-w"),
    "new window": Key("cs-n"),
    "new file": Key("c-n"),
    
    # Search
    "search [all] (files | codebase)": Key("cs-f"),
    "find": Key("c-f"),
    "find next <n>": Key("f3:%(n)d"),
    "find last <n>": Key("s-f3:%(n)d"),    
    # "(Find | Jump [to]) next <text>": Function(findNthToken, n=1, direction="forward"),
    # "(Find | Jump [to]) previous <text>": Function(findNthToken, n=1, direction="reverse"),

    # Tabs
    "nexta [<n>]": Key("c-pgdown:%(n)d"),
    "prexta [<n>]": Key("c-pgup:%(n)d"),
    "close tab": Key("c-w"),
    "exit preview": Key("space, c-z"),

    # Navigation
    "jump <n>": Key("c-g") + Text("%(n)d") + Key("enter"),
    "go to definition": Key("f12"),
    "go to required definition": Key("c-f12:2, c-right:5, left/50, f12"),
    "go to (top | first line)": Key("c-home"),
    "go to ( bottom | last line)": Key("c-end")

    # Editing
    "indent [<n>]": Key("c-rbracket"),
    "outdent [<n>]": Key("c-lbracket"),
    "slide [<n>]": Key("c-enter"),
    "slip [<n>]": Key("cs-enter"),
    "comment": Key("c-slash"),
    "block comment": Key("sa-a"),
    "move up <n>": Key("a-up:%(n)d"),
    "move down <n>": Key("a-down:%(n)d"),
    "take [all] others": Key("cs-l"),
    "take next [<n>]": Key("c-d:%(n)d"),
    "scrup [<n>]": Key("a-up:%(n)d"),
    "scrown [<n>]": Key("a-down:%(n)d"),
    "scrup page [<n>]": Key("a-pgup:%(n)d"),
    "scrown page [<n>]": Key("a-pgdown:%(n)d"),

    # Window
    "[toggle] full screen": Key("f11"),
    "[toggle] Zen mode": Key("c-k/3, z"),
    "[toggle] side bar": Key("c-b"),
    "[toggle] files": Key("cs-e"),
    "[toggle] git": Key("cs-g"),
    "split": Key("c-backslash"),
    "focus (term|terminal|one)": Key("c-1"),
    "focus two": Key("c-2"),
    "focus three": Key("c-3"),
    "focus four": Key("c-4"),
    "toggle (term|terminal)": Key("a-1"),

    # Debugging
    "[toggle] breakpoint":          Key("f9"),
    # "step over [<n>]":              Key("f10/50") * Repeat(extra="n"),
    "step into":                    Key("f11"),
    "step out [of]":                Key("s-f11"),
    "resume":                       Key("f5"),

}

class CommandRule(MappingRule):
    mapping = mapping

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50000)
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("vscode")
grammar.add_rule(CommandRule())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
