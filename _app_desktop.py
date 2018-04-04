"""A command module for Dragonfly, for controlling Solus/Budgie/Gnome.

-----------------------------------------------------------------------------
Licensed under the LGPL3.

"""

from dragonfly import AppContext, Grammar, MappingRule, Dictation, Pause, Function, IntegerRef

from aenea import (
    Key,
    Text,
)

mapping = {

    # Windows
    "snap screen": Key("w-up"),
    "snap win": Key("w-down"),
    "snap left": Key("w-left"),
    "snap right": Key("w-right"),    
    "snap close": Key("c-w"),
    "snap quit": Key("c-q"),    
    "snap full": Key("f11"),
    "flip": Key("a-tab"),
    "flop": Key("sa-tab"),

    # Workspaces
    "woke [<n>]": Key("scaw-%(n)d"),
    "wix": Key("ca-right"),
    "wox": Key("ca-left"),

    # Albert
    "spot": Key("scaw-space"),

}

class CommandRule(MappingRule):
    mapping = mapping

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 20)
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("desktop")
grammar.add_rule(CommandRule())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
