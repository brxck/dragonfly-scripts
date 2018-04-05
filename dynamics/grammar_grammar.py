from dragonfly import (
    MappingRule,
    Function,
    Grammar,
    IntegerRef,
    Dictation,
    Choice,
)

from aenea import (
    Key,
    Text,
)

# from lib.text import SCText
from aenea import Text as SCText

import lib.format

DYN_MODULE_TYPE = "programming_languages"
DYN_MODULE_NAME = "grammar"
INCOMPATIBLE_MODULES = [
    'ruby',
    'java',
    'javascript',
    'html',
    'css',
    'python'
]

def new_key():
    Key("end").execute()
    Text(": Key(\"\"),").execute()
    Key("left:3").execute()

def new_text():
    Key("end").execute()
    Text(": Text(\"\"),").execute()
    Key("left:3").execute()

def new_function():
    Key("end").execute()
    Text(": Function(\"\"),").execute()
    Key("left:3").execute()

rules = MappingRule(
    mapping = {
        "new key": Function(new_key),
        "new text": Function(new_text),
        "left num": Text("<n>"),
        "left text": Text("<text>"),
        "right num": Key("percent") + Text("(n)d"),
        "right text": Key("percent") + Text("()s") + Key("left:2"),
        "alt": Key("a"),
        "control": Key("c"),
        "shift": Key("s"),
        "super": Key("w"),
        "section": Text("### "),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

grammar = Grammar("grammar grammar")
grammar.add_rule(rules)
grammar.load()
grammar.disable()


def dynamic_enable():
    global grammar
    if grammar.enabled:
        return False
    else:
        grammar.enable()
        return True

def dynamic_disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
        return True
    else:
        return False

def is_enabled():
    global grammar
    if grammar.enabled:
        return True
    else:
        return False


# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
