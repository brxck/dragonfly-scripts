# grammar_grammar.py

command | action
control | Key("c")
left num | Text("<n>")
left text | Text("<text>")
shift | Key("s")
section | Text("### ")
new key | Function(new_key)
right text | Key("percent") + Text("()s") + Key("left:2")
new text | Function(new_text)
right num | Key("percent") + Text("(n)d")
alt | Key("a")
super | Key("w")
