# _desktop.py


## Windows

command | action
--- | ---
snap screen | Key("w-up")
snap win | Key("w-down")
snap left | Key("w-left")
snap right | Key("w-right")
snap close | Key("c-w")
snap quit | Key("c-q")
snap full | Key("f11")
flip | Key("a-escape")
flop | Key("sa-escape")
flap | Key("a-tab")

## Workspaces

command | action
--- | ---
woke \<n> | Key("caw-[n]")
wix [\<n>] | Key("ca-right:[n]")
wox [\<n>] | Key("ca-left:[n]")
snap wix [\<n>] | Key("sca-right:[n]")
snap wox [\<n>] | Key("sca-left:[n]")
snap woke \<n> | Key("scaw-[n]")

## Albert

command | action
--- | ---
spot [\<text>] | Key("scaw-space/3") + Text("[text]")
spite [\<text>] | Key("scaw-space/3") + Text("[text]") + Key("enter")

## Media

command | action
--- | ---
[toggle] mute | Key("volmute")
louder | Key("volup")
softer | Key("voldown")
next track | Key("tracknext")
last track | Key("trackprev")
(play\|pause) | Key("playpause")
n | 1
