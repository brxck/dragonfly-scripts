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
    "(Open [file] | Go to [tab]) [<text>]": Key("c-p") + Text("%(text)s"),
    "Save file": Key("c-s"),
    "Save and close": Key("c-s/10, c-w"),
    
    # Search
    "(search | find in) [all] (files | codebase)": Key("cs-f"),
    "(search | find) [file]": Key("c-f"),
    # "(Find | Jump [to]) next <text>": Function(findNthToken, n=1, direction="forward"),
    # "(Find | Jump [to]) previous <text>": Function(findNthToken, n=1, direction="reverse"),

    # Tabs
    "nexta [<n>]": Key("c-pgdown"),
    "prexta [<n>]": Key("c-pgup"),
    "Close tab": Key("c-w"),
    "Exit preview": Key("space, c-z"),

    # Navigation
    "jump <n>": Key("c-g") + Text("%(n)d") + Key("enter"),
    "Go to definition": Key("f12"),
    "Go to required definition": Key("c-f12:2, c-right:5, left/50, f12"),
    "Go to (top | first line)": Key("c-home"),
    "Go to ( bottom | last line)": Key("c-end"),
    "Go back [<n>]": Key("a-left"),
    "Go forward [<n>]": Key("a-right"),

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
