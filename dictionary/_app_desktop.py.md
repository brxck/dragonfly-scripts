# _app_desktop.py

command | action
--- | ---
snap screen | Key("w-up")
snap wox [<n>] | Key("sca-left:%(n)d")
louder | Key("volup")
snap wix [<n>] | Key("sca-right:%(n)d")
snap woke <n> | Key("scaw-%(n)d")
next track | Key("tracknext")
snap full | Key("f11")
woke <n> | Key("caw-%(n)d")
wox [<n>] | Key("ca-left:%(n)d")
snap win | Key("w-down")
flap | Key("a-tab")
last track | Key("trackprev")
spite [<text>] | Key("scaw-space/3") + Text("%(text)s") + Key("enter")
wix [<n>] | Key("ca-right:%(n)d")
snap right | Key("w-right")
snap close | Key("c-w")
spot [<text>] | Key("scaw-space/3") + Text("%(text)s")
snap quit | Key("c-q")
(play|pause) | Key("playpause")
flop | Key("sa-escape")
flip | Key("a-escape")
n | 1
softer | Key("voldown")
snap left | Key("w-left")
[toggle] mute | Key("volmute")
