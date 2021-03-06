# _app_vscode.py


## Files

command | action
--- | ---
[open] command palette | Key("cs-p")
(open [file] \| Go to [tab]) [\<text>] | Key("c-p") + Text("[text]")
open folder | Key("c-k/3, c-s")
save file | Key("c-s")
save and close | Key("c-s/10, c-w")
new window | Key("cs-n")
new file | Key("c-n")

## Search

command | action
--- | ---
search [all] (files \| codebase) | Key("cs-f")
find | Key("c-f")
find next \<n> | Key("f3:[n]")
find last \<n> | Key("s-f3:[n]")

## Tabs

command | action
--- | ---
nexta [\<n>] | Key("c-pgdown:[n]")
prexta [\<n>] | Key("c-pgup:[n]")
close tab | Key("c-w")
exit preview | Key("space, c-z")

## Navigation

command | action
--- | ---
jump \<n> | Key("c-g") + Text("[n]") + Key("enter")
go to definition | Key("f12")
go to required definition | Key("c-f12:2, c-right:5, left/50, f12")
go to (top \| first line) | Key("c-home")
go to ( bottom \| last line) | Key("c-end")

## Editing

command | action
--- | ---
indent [\<n>] | Key("c-rbracket")
outdent [\<n>] | Key("c-lbracket")
slide [\<n>] | Key("c-enter")
slip [\<n>] | Key("cs-enter")
comment | Key("c-slash")
block comment | Key("sa-a")
move up \<n> | Key("a-up:[n]")
move down \<n> | Key("a-down:[n]")
take [all] others | Key("cs-l")
take next [\<n>] | Key("c-d:[n]")
scrup [\<n>] | Key("a-up:[n]")
scrown [\<n>] | Key("a-down:[n]")
scrup page [\<n>] | Key("a-pgup:[n]")
scrown page [\<n>] | Key("a-pgdown:[n]")

## Window

command | action
--- | ---
[toggle] full screen | Key("f11")
[toggle] Zen mode | Key("c-k/3, z")
[toggle] side bar | Key("c-b")
[toggle] files | Key("cs-e")
[toggle] git | Key("cs-g")
split | Key("c-backslash")
focus (term\|terminal\|one) | Key("c-1")
focus two | Key("c-2")
focus three | Key("c-3")
focus four | Key("c-4")
toggle (term\|terminal) | Key("a-1")

## Debugging

command | action
--- | ---
[toggle] breakpoint | Key("f9")
step into | Key("f11")
step out [of] | Key("s-f11")
resume | Key("f5")
n | 1
