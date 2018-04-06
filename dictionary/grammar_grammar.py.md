# grammar_grammar.py

command | action
--- | ---
new key | Function(new_key)
new text | Function(new_text)
left num | Text("<n>")
left text | Text("<text>")
right num | Key("percent") + Text("(n)d")
right text | Key("percent") + Text("()s") + Key("left:2")
alt | Key("a")
control | Key("c")
shift | Key("s")
super | Key("w")
section | Text("###  ###") + Key("left:4")
section \<text> | Text("### [text]while  ###")
