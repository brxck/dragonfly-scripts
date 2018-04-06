# _generic_edit.py

command | action
--- | ---
golf | "g"
java archive | "jar"
pope | "p"
camel | ft.camelCase
cut [that] | release + Key("c-x/3")
text | "txt"
(direction|directory) | "dir"
grab <n> (line|lines) | release + Key("home, shift:down, down:%(n)d, end, shift:up")
dynamic | "dyn"
dose | "2"
percy | "%"
quotes | Key("dquote/3, dquote/3, left/3")
pascal | ft.pascalCase
<number> | Text("%(number)s")
[(hold|press)] control | Key("ctrl:down/3")
tilde | "~"
whack [<n>] | Key("shift:down, c-left/3:%(n)d/10, del, shift:up")
F two | 'f2'
alt | "alt"
(initialize|initializer) | "init"
previous | "prev"
left brace | "{"
[(hold|press)] shift | Key("shift:down/3")
cut | "cut"
zed | "z"
integer | "int"
instance | "inst"
(extension|extend) | "ext"
triple <char> | Text("%(char)s%(char)s%(char)s")
(enter|return) | "enter"
uppercase <n> [words] | Function(uppercase_count)
session aidee | "sid"
source | "src"
window | "win"
query string | "qs"
expand <n> [words] | Function(expand_count)
(lowercase|low) dashify | [ft.dashify, ft.lowerCase]
backspace | "backspace"
snake <n> [words] | Function(snake_case_count)
save | release + Key("c-s")
hat | "^"
pixel | "px"
juke | "j"
take <n> (word|words) | release + Key("shift:down, c-left:%(n)d, shift:up")
string | "str"
python | "py"
left [<n>] (word|words) | Key("c-left/3:%(n)d/10")
utilities | "utils"
page up | "page up"
colon [<n>] | Key("colon/2:%(n)d")
execute | "exec"
(take|grab) end | release + Key("shift:down, end, shift:up")
period | "period"
framework | "fw"
bang | "!"
quest | "?"
pop | ")"
underscore | "underscore"
keyword arguments | "kwargs"
amp | "&"
[double] quote | '"'
nab [that] | Function(paste_command)
standard out | "stdout"
page down | "page down"
squares | Key("lbracket, rbracket, left/3")
whisk | "w"
semi | ";"
button | "btn"
say <reservedWord> | Text("%(reservedWord)s")
Text | Text
release | "release"
references | "refs"
squash <n> [words] | Function(squash_count)
(config|configuration) | "cfg"
app key | release + Key("apps/3")
squash (uppercase|shout) | [ft.squash, ft.upperCase]
right | "right"
scratch [this] line | Key("home, s-end, del")
reference | "ref"
scratch [<n>] | release + Key("backspace:%(n)d")
uppercase | "uppercase"
temporary | "tmp"
kilo | "k"
ocho | "8"
hail | "h"
cash | "$"
camel <n> [words] | Function(camel_case_count)
(dash|hyphen|minus) [<n>] | Key("hyphen/2:%(n)d")
zero | "0"
escape | "escape"
right [<n>] (word|words) | Key("c-right/3:%(n)d/10")
home | Key("home")
doc end | Key("c-end/3")
right [<n>] | Key("right:%(n)d")
F ten | 'f10'
[<text>] (go to sleep|cancel and sleep) [<text2>] | Function(cancel_and_sleep)
space | release + Key("space")
short <abbreviation> | Text("%(abbreviation)s")
down [<n>] | Key("down:%(n)d")
fox | "f"
pascal <n> [words] | Function(pascal_case_count)
ice | "i"
uniform | "u"
(dictionary|dictation) | "dict"
F five | 'f5'
dashify | ft.dashify
slash | "/"
(develop|development) | "dev"
utility | "util"
<letter> | Text("%(letter)s")
chuck [<n>] | Key("del/3:%(n)d")
parens | Key("lparen, rparen, left/3")
standard in | "stdin"
(special|specify|specific|specification) | "spec"
javascript | "js"
snake | ft.snakeCase
cork | "c"
F six | 'f6'
mew | "m"
yoke | "y"
undo | release + Key("c-z/3")
(lowercase|low) | ft.lowerCase
standard | "std"
super | "win"
orc | "o"
single quotes | Key("squote, squote, left/3")
quack | "q"
up [<n>] | Key("up:%(n)d")
property | "prop"
parameters | "params"
language | "lng"
package | "pkg"
shift | "shift"
(lowercase|low) squash | [ft.squash, ft.lowerCase]
equal | "="
minus | "minus"
length | "len"
redo <n> [times] | release + Key("c-y/3:%(n)d")
<specialChar> | Text("%(specialChar)s")
<formatType> <text> | Function(format_text)
context | "ctx"
act | Key("escape")
(uppercase|shout) | ft.upperCase
double <char> | Text("%(char)s%(char)s")
expression | "exp"
grab <n> (word|words) | release + Key("shift:down, c-right:%(n)d, shift:up")
uno | "1"
sace | "6"
braces | Key("lbrace, rbrace, left/3")
mod key | release + Key("win/3")
angles | Key("langle, rangle, left/3")
abbreviate | "abbreviate"
vie | "v"
hyphen | "hyphen"
number | "num"
backtick | "`"
echo | "e"
down | "down"
environment variable | [ft.snakeCase, ft.upperCase]
colon | ":"
(bar|vertical bar|pipe) | "|"
(uppercase|shout) dotify | [ft.dotify, ft.upperCase]
lima | "l"
redo | release + Key("c-y/3")
release [all] | release
select | "select"
speak | ft.sentence
siete | "7"
dotify lowercase | [ft.dotify, ft.lowerCase]
(semi-colon|semicolon) [<n>] | Key("semicolon/2:%(n)d")
smote | "'"
paste | "paste"
press <modifierSingle> | Key("%(modifierSingle)s")
system | "sys"
F one | 'f1'
beer | "b"
(uppercase|shout) dashify | [ft.dashify, ft.upperCase]
ares | "a"
undo <n> [times] | release + Key("c-z/3:%(n)d")
tab [<n>] | Key("tab:%(n)d")
slide [<n>] | release + Key("end, enter:%(n)d")
(take|grab) line | release + Key("home, s-end")
function | "func"
dotify | ft.dotify
take <n> | release + Key("shift:down, left:%(n)d, shift:up")
comma [<n>] | Key("comma/2:%(n)d")
squash | "squash"
[(hold|press)] alt | Key("alt:down/3")
argument | "arg"
administrators | "admins"
cinco | "5"
lendit | Key("end, comma")
select all | "select all"
F eight | 'f8'
library | "lib"
quatro | "4"
delta | "d"
semi-colon | "semi-colon"
copy | "copy"
ruby | "rb"
grab <n> | release + Key("shift:down, right:%(n)d, shift:up")
pinch [<n>] | Key("pgup:%(n)d")
exception | "exc"
doc home | Key("c-home/3")
squash lowercase | [ft.squash, ft.lowerCase]
F three | 'f3'
keyword | "kw"
release control | Key("ctrl:up")
(add|fix) missing space | Key("c-left/3, space, c-right/3")
(represent|representation) | "repr"
database | "db"
up | "up"
value | "val"
n | 1
(delete|remove) (double|extra) (space|whitespace) | Key("c-left/3, backspace, c-right/3")
(dot|period) | "."
(take|grab) all | release + Key("c-a/3")
say | "say"
example | "ex"
x-ray | "x"
delete | "delete"
control | "ctrl"
tau | "t"
pound | "#"
tab | "tab"
styx | "s"
attribute | "attr"
right square | "]"
backslash | "\\"
underscore [<n>] | Key("underscore/2:%(n)d")
(dot|period) [<n>] | Key("dot/2:%(n)d")
dash | "dash"
(delete|remove) (double|extra) (type|char|character) | Key("c-left/3, del, c-right/3")
newevay | "9"
(take|grab) home | release + Key("shift:down, home, shift:up")
at | "@"
point | "pt"
F twelve | 'f12'
space [<n>] | release + Key("space:%(n)d")
lowercase <n> [words] | Function(lowercase_count)
page [<n>] | Key("pgdown:%(n)d")
binary | "bin"
copy [that] | Function(copy_command)
end | "end"
double escape | Key("escape, escape")
nike | "n"
(uppercase|shout) squash | [ft.squash, ft.upperCase]
F four | 'f4'
cross | "+"
Key | Key
dashify lowercase | [ft.dashify, ft.lowerCase]
application | "app"
arguments | "args"
regular (expression|expressions) | "regex"
take <n> (line|lines) | release + Key("end, shift:down, home, up:%(n)d, home, shift:up")
(authenticate|authentication) | "auth"
parameter | "param"
revision | "rev"
press <modifier1> <pressKey> [<n>] | Key("%(modifier1)s-%(pressKey)s:%(n)d")
administrator | "admin"
okay | "ok"
description | "desc"
trace | "3"
lend | Key("end")
right brace | "}"
class | "cls"
object | "obj"
rail | "_"
(define|definition) | "def"
bump [<n>] | Key("shift:down, c-right/3:%(n)d/10, del, shift:up")
left square | "["
applications | "apps"
(dash|minus|hyphen) | "-"
release alt | Key("alt:up")
rho | "r"
attributes | "attrs"
lowercase | "lowercase"
iterate | "iter"
chuck [this] line | Key("home:2, s-end, backspace:2")
splat | "*"
expand | "expand"
left [<n>] | Key("left:%(n)d")
press <modifier1> <modifier2> <pressKey> [<n>] | Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d")
F eleven | 'f11'
release shift | Key("shift:up")
drop [<n>] | release + Key("enter:%(n)d")
F nine | 'f9'
dotify (uppercase|shout) | [ft.dotify, ft.upperCase]
(lowercase|low) dotify | [ft.dotify, ft.lowerCase]
request | "req"
drip | ","
(synchronize|synchronous) | "sync"
command | "cmd"
dot | "dot"
(take|grab) word | Key("c-left, sc-right")
enter | "enter"
push | "("
position | "pos"
dashify (uppercase|shout) | [ft.dashify, ft.upperCase]
F seven | 'f7'
left | "left"
