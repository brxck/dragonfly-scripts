"""A command module for Dragonfly, for generic editing help.

-----------------------------------------------------------------------------
This is a heavily modified version of the _multiedit-en.py script at:
http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html  # @IgnorePep8
Licensed under the LGPL, see http://www.gnu.org/licenses/

"""
from natlink import setMicState
from dragonfly import (
    Choice,
    Pause,
    Window,
    FocusWindow,
    Config,
    Section,
    Item,
    Function,
    Dictation,
    IntegerRef,
    MappingRule,
    Alternative,
    RuleRef,
    Grammar,
    Repetition,
    CompoundRule,
    AppContext,
)

from aenea import (
    Key,
    Text,
)

import win32con
from dragonfly.actions.keyboard import Typeable, keyboard
from dragonfly.actions.typeables import typeables
if not 'Control_R' in typeables:
    keycode = win32con.VK_RCONTROL
    typeables["Control_R"] = Typeable(code=keycode, name="Control_R")
if not 'semicolon' in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

import lib.config
config = lib.config.get_config()

import lib.sound as sound
from lib.format import (
    camel_case_count,
    pascal_case_count,
    snake_case_count,
    squash_count,
    expand_count,
    uppercase_count,
    lowercase_count,
    format_text,
    FormatTypes as ft,
)


release = Key("shift:up, ctrl:up, alt:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
    with a sound and a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    sound.play(sound.SND_DING)
    setMicState("sleeping")


def reload_natlink():
    """Reloads Natlink and custom Python modules."""
    win = Window.get_foreground()
    FocusWindow(executable="natspeak",
        title="Messages from Python Macros").execute()
    Pause("10").execute()
    Key("a-f, r").execute()
    Pause("10").execute()
    win.set_foreground()

# For repeating of characters.
# TODO: rename variables to stop confliction.
specialCharMap = {
    "(bar|vertical bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|period)": ".",
    "drip": ",",
    "backslash": "\\",
    "rail": "_",
    "splat": "*",
    "colon": ":",
    "semi": ";",
    "at": "@",
    "hat": "^",    
    "[double] quote": '"',
    "smote": "'",
    "pound": "#",
    "cash": "$",
    "percy": "%",
    "amp": "&",
    "slash": "/",
    "equal": "=",
    "cross": "+",
    "bang": "!",
    "backtick": "`",
    "tilde": "~",
    "quest": "?",
    "l brace": "{",
    "r brace": "}",
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

letterMap = {
    "ares": "a",
    "beer": "b",
    "chi": "c",
    "delt": "d",
    "echo": "e",
    "fox": "f",
    "golf": "g",
    "hera": "h",
    "imp": "i",
    "ju": "j",
    "kilo": "k",
    "lima": "l",
    "mew": "m",
    "nike": "n",
    "orc": "o",
    "pope": "p",
    "quack": "q",
    "rho": "r",
    "styx": "s",
    "tau": "t",
    "uniform": "u",
    "vie": "v",
    "whisk": "w",
    "x-ray": "x",
    "yoke": "y",
    "zed": "z",
}

numberMap = {
    "zero": "0",
    "uno": "1",
    "dose": "2",
    "trace": "3",
    "quatro": "4",
    "cinco": "5",
    "sace": "6",
    "siete": "7",
    "ocho": "8",
    "newevay": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab"
}

# F1 to F12.
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)


formatMap = {
    "camel": ft.camelCase,
    "pascal": ft.pascalCase,
    "snake": ft.snakeCase,
    "(uppercase|shout)": ft.upperCase,
    "(lowercase|low)": ft.lowerCase,
    "squash": ft.squash,
    "(lowercase|low) squash": [ft.squash, ft.lowerCase],
    "(uppercase|shout) squash": [ft.squash, ft.upperCase],
    "squash lowercase": [ft.squash, ft.lowerCase],
    "squash (uppercase|shout)": [ft.squash, ft.upperCase],
    "dashify": ft.dashify,
    "(lowercase|low) dashify": [ft.dashify, ft.lowerCase],
    "(uppercase|shout) dashify": [ft.dashify, ft.upperCase],
    "dashify lowercase": [ft.dashify, ft.lowerCase],
    "dashify (uppercase|shout)": [ft.dashify, ft.upperCase],
    "dotify": ft.dotify,
    "(lowercase|low) dotify": [ft.dotify, ft.lowerCase],
    "(uppercase|shout) dotify": [ft.dotify, ft.upperCase],
    "dotify lowercase": [ft.dotify, ft.lowerCase],
    "dotify (uppercase|shout)": [ft.dotify, ft.upperCase],
    "say": ft.spokenForm,
    "environment variable": [ft.snakeCase, ft.upperCase],
    "speak": ft.sentence,
}


abbreviationMap = {
    "administrator": "admin",
    "administrators": "admins",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "(authenticate|authentication)": "auth",
    "binary": "bin",
    "button": "btn",
    "class": "cls",
    "command": "cmd",
    "(config|configuration)": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "database": "db",
    "(define|definition)": "def",
    "description": "desc",
    "(develop|development)": "dev",
    "(dictionary|dictation)": "dict",
    "(direction|directory)": "dir",
    "dynamic": "dyn",
    "example": "ex",
    "execute": "exec",
    "exception": "exc",
    "expression": "exp",
    "(extension|extend)": "ext",
    "function": "func",
    "framework": "fw",
    "(initialize|initializer)": "init",
    "instance": "inst",
    "integer": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "keyword": "kw",
    "keyword arguments": "kwargs",
    "language": "lng",
    "library": "lib",
    "length": "len",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
    "previous": "prev",
    "property": "prop",
    "python": "py",
    "query string": "qs",
    "reference": "ref",
    "references": "refs",
    "(represent|representation)": "repr",
    "regular (expression|expressions)": "regex",
    "request": "req",
    "revision": "rev",
    "ruby": "rb",
    "session aidee": "sid",  # "session id" didn't work for some reason.
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "(synchronize|synchronous)": "sync",
    "system": "sys",
    "utility": "util",
    "utilities": "utils",
    "temporary": "tmp",
    "text": "txt",
    "value": "val",
    "window": "win",
}

# For use with "say"-command. Words that are commands in the generic edit
# grammar were treated as separate commands and could not be written with the
# "say"-command. This overrides that behavior.
# Other words that won't work for one reason or another, can also be added to
# this list.
reservedWord = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "home": "home",
    "end": "end",
    "space": "space",
    "tab": "tab",
    "backspace": "backspace",
    "delete": "delete",
    "enter": "enter",
    "paste": "paste",
    "copy": "copy",
    "cut": "cut",
    "undo": "undo",
    "release": "release",
    "page up": "page up",
    "page down": "page down",
    "say": "say",
    "select": "select",
    "select all": "select all",
    "abbreviate": "abbreviate",
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "expand": "expand",
    "squash": "squash",
    "dash": "dash",
    "underscore": "underscore",
    "dot": "dot",
    "period": "period",
    "minus": "minus",
    "semi-colon": "semi-colon",
    "hyphen": "hyphen",
    "triple": "triple"
}


def copy_command():
    # Add Command Prompt, putty, ...?
    context = AppContext(executable="console")
    window = Window.get_foreground()
    if context.matches(window.executable, window.title, window.handle):
        return
    release.execute()
    Key("c-c/3").execute()


def paste_command():
    # Add Command Prompt, putty, ...?
    context = AppContext(executable="console")
    window = Window.get_foreground()
    if context.matches(window.executable, window.title, window.handle):
        return
    release.execute()
    Key("c-v/3").execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        ### Navigation
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "pinch [<n>]": Key("pgup:%(n)d"),
        "page [<n>]": Key("pgdown:%(n)d"),
        "left [<n>] (word|words)": Key("c-left/3:%(n)d/10"),
        "right [<n>] (word|words)": Key("c-right/3:%(n)d/10"),
        "home": Key("home"),
        "lend": Key("end"),
        "lendit": Key("end, comma"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),

        # Selections
        "grab <n>": release + Key("shift:down, right:%(n)d, shift:up"),
        "take <n>": release + Key("shift:down, left:%(n)d, shift:up"),
        "take <n> (line|lines)": release + Key("end, shift:down, home, up:%(n)d, home, shift:up"),
        "grab <n> (line|lines)": release + Key("home, shift:down, down:%(n)d, end shift:up"),
        "grab <n> (word|words)": release + Key("shift:down, c-right:%(n)d, shift:up"),
        "take <n> (word|words)": release + Key("shift:down, c-left:%(n)d, shift:up"),
        "(take|grab) home": release + Key("shift:down, home, shift:up"),
        "(take|grab) end": release + Key("shift:down, end, shift:up"),
        "(take|grab) line": release + Key("home, s-end"),
        "(take|grab) all": release + Key("c-a/3"),

        # Functional keys
        "act": Key("escape"),
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "slap [<n>]": release + Key("enter:%(n)d"),
        "slide [<n>]": release + Key("end, enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
    
        # Deletions
        "scratch [<n>]": release + Key("backspace:%(n)d"),
        "chuck [<n>]": Key("del/3:%(n)d"),
        "whack [<n>]": Key("shift:down, c-left/3:%(n)d/10, del, shift:up"),
        "bump [<n>]": Key("shift:down, c-right/3:%(n)d/10, del, shift:up"),      
        "scratch [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "chuck [this] line": Key("home:2, s-end, backspace:2"),

        # Common functions
        "paste [that]": Function(paste_command),
        "copy [that]": Function(copy_command),
        "cut [that]": release + Key("c-x/3"),
        "undo": release + Key("c-z/3"),
        "undo <n> [times]": release + Key("c-z/3:%(n)d"),
        "redo": release + Key("c-y/3"),
        "redo <n> [times]": release + Key("c-y/3:%(n)d"),
        "save": release + Key("c-s"),

        # Modifiers
        "app key": release + Key("apps/3"),
        "mod key": release + Key("win/3"),
        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,

        # Closures
        "angles": Key("langle, rangle, left/3"),
        "squares": Key("lbracket, rbracket, left/3"),
        "braces": Key("lbrace, rbrace, left/3"),
        "parens": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "single quotes": Key("squote, squote, left/3"),

        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.

        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "(semi-colon|semicolon) [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        "(dot|period) [<n>]": Key("dot/2:%(n)d"),
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),

        # To release keyboard capture by VirtualBox.
        # "press right control": Key("Control_R"),

        # Formatting <n> words to the left of the cursor.
        "camel <n> [words]": Function(camel_case_count),
        "pascal <n> [words]": Function(pascal_case_count),
        "snake <n> [words]": Function(snake_case_count),
        "squash <n> [words]": Function(squash_count),
        "expand <n> [words]": Function(expand_count),
        "uppercase <n> [words]": Function(uppercase_count),
        "lowercase <n> [words]": Function(lowercase_count),
        # Format dictated words. See the formatMap for all available types.
        # Ex: "camel case my new variable" -> "myNewVariable"
        # Ex: "snake case my new variable" -> "my_new_variable"
        # Ex: "uppercase squash my new hyphen variable" -> "MYNEW-VARIABLE"
        "<formatType> <text>": Function(format_text),
        # For writing words that would otherwise be characters or commands.
        # Ex: "period", tab", "left", "right", "home".
        "say <reservedWord>": Text("%(reservedWord)s"),
        # Abbreviate words commonly used in programming.
        # Ex: arguments -> args, parameters -> params.
        "short <abbreviation>": Text("%(abbreviation)s"),
        # Text corrections.
        "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
        # Reload Natlink.
        # "reload Natlink": Function(reload_natlink),

        "<number>": Text("%(number)s"),
        "<letter>": Text("%(letter)s"),
        "<specialChar>": Text("%(specialChar)s"),
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


if config.get("aenea.enabled") == True:
    # Keypresses, to get that working better in Linux.
    grammarCfg.cmd.map.update({
        "press <modifierSingle>": Key("%(modifierSingle)s"),
        "press <modifier1> <pressKey> [<n>]": Key("%(modifier1)s-%(pressKey)s:%(n)d"),  # @IgnorePep8
        "press <modifier1> <modifier2> <pressKey> [<n>]": Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d"),  # @IgnorePep8
    })


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
        Choice("formatType", formatMap),
        Choice("abbreviation", abbreviationMap),
        Choice("reservedWord", reservedWord),
        Choice("number", numberMap),
        Choice("letter", letterMap),
        Choice("specialChar", specialCharMap),
        
    ]
    defaults = {
        "n": 1,
    }


alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
single_action = Alternative(alternatives)


sequence = Repetition(single_action, min=1, max=16, name="sequence")


class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
        release.execute()

grammar = Grammar("Generic edit")
grammar.add_rule(RepeatRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
