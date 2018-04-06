# _generic_edit.py

command | action
--- | ---
take \<n> (line|lines) | release + Key("end, shift:down, home, up:[xn], home, shift:up")
golf | "g"
java archive | "jar"
pope | "p"
camel | ft.camelCase
cut [that] | release + Key("c-x/3")
text | "txt"
(direction|directory) | "dir"
dynamic | "dyn"
(take|grab) line | release + Key("home, s-end")
dose | "2"
percy | "%"
quotes | Key("dquote/3, dquote/3, left/3")
pascal | ft.pascalCase
down [\<n>] | Key("down:[xn]")
[(hold|press)] control | Key("ctrl:down/3")
tilde | "~"
F two | 'f2'
alt | "alt"
(initialize|initializer) | "init"
previous | "prev"
left brace | "{"
redo \<n> [times] | release + Key("c-y/3:[xn]")
cut | "cut"
zed | "z"
integer | "int"
instance | "inst"
(extension|extend) | "ext"
colon [\<n>] | Key("colon/2:[xn]")
(enter|return) | "enter"
(dash|hyphen|minus) [\<n>] | Key("hyphen/2:[xn]")
double \<char> | Text("[xchar][xchar]")
session aidee | "sid"
source | "src"
window | "win"
query string | "qs"
(lowercase|low) dashify | [ft.dashify, ft.lowerCase]
backspace | "backspace"
save | release + Key("c-s")
hat | "^"
pixel | "px"
juke | "j"
string | "str"
python | "py"
press \<modifierSingle> | Key("[xmodifierSingle]")
utilities | "utils"
page up | "page up"
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
slide [\<n>] | release + Key("end, enter:[xn]")
page down | "page down"
squares | Key("lbracket, rbracket, left/3")
grab \<n> (word|words) | release + Key("shift:down, c-right:[xn], shift:up")
whisk | "w"
semi | ";"
page [\<n>] | Key("pgdown:[xn]")
button | "btn"
pinch [\<n>] | Key("pgup:[xn]")
scratch [\<n>] | release + Key("backspace:[xn]")
Text | Text
release | "release"
references | "refs"
(config|configuration) | "cfg"
app key | release + Key("apps/3")
squash (uppercase|shout) | [ft.squash, ft.upperCase]
undo \<n> [times] | release + Key("c-z/3:[xn]")
right | "right"
scratch [this] line | Key("home, s-end, del")
reference | "ref"
underscore [\<n>] | Key("underscore/2:[xn]")
short \<abbreviation> | Text("[xabbreviation]")
uppercase | "uppercase"
temporary | "tmp"
kilo | "k"
ocho | "8"
hail | "h"
cash | "$"
zero | "0"
escape | "escape"
uppercase \<n> [words] | Function(uppercase_count)
home | Key("home")
doc end | Key("c-end/3")
\<number> | Text("[xnumber]")
left [\<n>] (word|words) | Key("c-left/3:[xn]/10")
F ten | 'f10'
(dot|period) [\<n>] | Key("dot/2:[xn]")
space | release + Key("space")
fox | "f"
ice | "i"
uniform | "u"
(dictionary|dictation) | "dict"
F five | 'f5'
dashify | ft.dashify
slash | "/"
(develop|development) | "dev"
tab [\<n>] | Key("tab:[xn]")
utility | "util"
\<letter> | Text("[xletter]")
squash \<n> [words] | Function(squash_count)
parens | Key("lparen, rparen, left/3")
Key | Key
[(hold|press)] shift | Key("shift:down/3")
standard in | "stdin"
(special|specify|specific|specification) | "spec"
whack [\<n>] | Key("shift:down, c-left/3:[xn]/10, del, shift:up")
javascript | "js"
bump [\<n>] | Key("shift:down, c-right/3:[xn]/10, del, shift:up")
snake | ft.snakeCase
cork | "c"
F six | 'f6'
mew | "m"
yoke | "y"
undo | release + Key("c-z/3")
drop [\<n>] | release + Key("enter:[xn]")
take \<n> (word|words) | release + Key("shift:down, c-left:[xn], shift:up")
\<specialChar> | Text("[xspecialChar]")
(lowercase|low) | ft.lowerCase
standard | "std"
super | "win"
orc | "o"
single quotes | Key("squote, squote, left/3")
quack | "q"
property | "prop"
parameters | "params"
language | "lng"
package | "pkg"
shift | "shift"
press \<modifier1> \<modifier2> \<pressKey> [\<n>] | Key("[xmodifier1][xmodifier2]-[xpressKey]:[xn]")
(lowercase|low) squash | [ft.squash, ft.lowerCase]
equal | "="
minus | "minus"
length | "len"
context | "ctx"
act | Key("escape")
(uppercase|shout) | ft.upperCase
left [\<n>] | Key("left:[xn]")
expression | "exp"
uno | "1"
sace | "6"
braces | Key("lbrace, rbrace, left/3")
mod key | release + Key("win/3")
angles | Key("langle, rangle, left/3")
abbreviate | "abbreviate"
vie | "v"
hyphen | "hyphen"
press \<modifier1> \<pressKey> [\<n>] | Key("[xmodifier1]-[xpressKey]:[xn]")
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
select | "select"
speak | ft.sentence
siete | "7"
dotify lowercase | [ft.dotify, ft.lowerCase]
expand \<n> [words] | Function(expand_count)
triple \<char> | Text("[xchar][xchar][xchar]")
smote | "'"
[\<text>] (go to sleep|cancel and sleep) [\<text2>] | Function(cancel_and_sleep)
paste | "paste"
system | "sys"
F one | 'f1'
grab \<n> (line|lines) | release + Key("home, shift:down, down:[xn], end, shift:up")
beer | "b"
(uppercase|shout) dashify | [ft.dashify, ft.upperCase]
ares | "a"
right [\<n>] | Key("right:[xn]")
function | "func"
pascal \<n> [words] | Function(pascal_case_count)
dotify | ft.dotify
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
release [all] | release
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
space [\<n>] | release + Key("space:[xn]")
attribute | "attr"
right square | "]"
backslash | "\\"
dash | "dash"
(delete|remove) (double|extra) (type|char|character) | Key("c-left/3, del, c-right/3")
newevay | "9"
(take|grab) home | release + Key("shift:down, home, shift:up")
take \<n> | release + Key("shift:down, left:[xn], shift:up")
at | "@"
point | "pt"
say \<reservedWord> | Text("[xreservedWord]")
F twelve | 'f12'
copy [that] | Function(copy_command)
\<formatType> \<text> | Function(format_text)
chuck [\<n>] | Key("del/3:[xn]")
binary | "bin"
end | "end"
double escape | Key("escape, escape")
nike | "n"
(uppercase|shout) squash | [ft.squash, ft.upperCase]
F four | 'f4'
cross | "+"
right [\<n>] (word|words) | Key("c-right/3:[xn]/10")
dashify lowercase | [ft.dashify, ft.lowerCase]
application | "app"
arguments | "args"
regular (expression|expressions) | "regex"
(authenticate|authentication) | "auth"
parameter | "param"
revision | "rev"
(semi-colon|semicolon) [\<n>] | Key("semicolon/2:[xn]")
administrator | "admin"
camel \<n> [words] | Function(camel_case_count)
okay | "ok"
description | "desc"
trace | "3"
lend | Key("end")
right brace | "}"
class | "cls"
object | "obj"
rail | "_"
(define|definition) | "def"
snake \<n> [words] | Function(snake_case_count)
left square | "["
lowercase \<n> [words] | Function(lowercase_count)
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
F eleven | 'f11'
release shift | Key("shift:up")
F nine | 'f9'
dotify (uppercase|shout) | [ft.dotify, ft.upperCase]
(lowercase|low) dotify | [ft.dotify, ft.lowerCase]
up [\<n>] | Key("up:[xn]")
grab \<n> | release + Key("shift:down, right:[xn], shift:up")
request | "req"
drip | ","
comma [\<n>] | Key("comma/2:[xn]")
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
