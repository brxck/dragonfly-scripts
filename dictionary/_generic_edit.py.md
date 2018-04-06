# _generic_edit.py

command | action
--- | ---
(bar\|vertical bar\|pipe) | "|"
(dash\|minus\|hyphen) | "-"
(dot\|period) | "."
drip | ","
backslash | "\\"
rail | "_"
splat | "*"
colon | ":"
semi | ";"
at | "@"
hat | "^"
[double] quote | '"'
smote | "'"
pound | "#"
cash | "$"
percy | "%"
amp | "&"
slash | "/"
equal | "="
cross | "+"
bang | "!"
backtick | "`"
tilde | "~"
quest | "?"
left brace | "{"
right brace | "}"
push | "("
pop | ")"
left square | "["
right square | "]"
alt | "alt"
control | "ctrl"
shift | "shift"
super | "win"
ares | "a"
beer | "b"
cork | "c"
delta | "d"
echo | "e"
fox | "f"
golf | "g"
hail | "h"
ice | "i"
juke | "j"
kilo | "k"
lima | "l"
mew | "m"
nike | "n"
orc | "o"
pope | "p"
quack | "q"
rho | "r"
styx | "s"
tau | "t"
uniform | "u"
vie | "v"
whisk | "w"
x-ray | "x"
yoke | "y"
zed | "z"
zero | "0"
uno | "1"
dose | "2"
trace | "3"
quatro | "4"
cinco | "5"
sace | "6"
siete | "7"
ocho | "8"
newevay | "9"
left | "left"
right | "right"
up | "up"
down | "down"
page up | "page up"
page down | "page down"
home | Key("home")
end | "end"
space | release + Key("space")
(enter\|return) | "enter"
escape | "escape"
F one | 'f1'
F two | 'f2'
F three | 'f3'
F four | 'f4'
F five | 'f5'
F six | 'f6'
F seven | 'f7'
F eight | 'f8'
F nine | 'f9'
F ten | 'f10'
F eleven | 'f11'
F twelve | 'f12'
camel | ft.camelCase
pascal | ft.pascalCase
snake | ft.snakeCase
(uppercase\|shout) | ft.upperCase
(lowercase\|low) | ft.lowerCase
squash | "squash"
(lowercase\|low) squash | [ft.squash, ft.lowerCase]
(uppercase\|shout) squash | [ft.squash, ft.upperCase]
squash lowercase | [ft.squash, ft.lowerCase]
squash (uppercase\|shout) | [ft.squash, ft.upperCase]
dashify | ft.dashify
(lowercase\|low) dashify | [ft.dashify, ft.lowerCase]
(uppercase\|shout) dashify | [ft.dashify, ft.upperCase]
dashify lowercase | [ft.dashify, ft.lowerCase]
dashify (uppercase\|shout) | [ft.dashify, ft.upperCase]
dotify | ft.dotify
(lowercase\|low) dotify | [ft.dotify, ft.lowerCase]
(uppercase\|shout) dotify | [ft.dotify, ft.upperCase]
dotify lowercase | [ft.dotify, ft.lowerCase]
dotify (uppercase\|shout) | [ft.dotify, ft.upperCase]
say | "say"
environment variable | [ft.snakeCase, ft.upperCase]
speak | ft.sentence
administrator | "admin"
administrators | "admins"
application | "app"
applications | "apps"
argument | "arg"
arguments | "args"
attribute | "attr"
attributes | "attrs"
(authenticate\|authentication) | "auth"
binary | "bin"
button | "btn"
class | "cls"
command | "cmd"
(config\|configuration) | "cfg"
context | "ctx"
database | "db"
(define\|definition) | "def"
description | "desc"
(develop\|development) | "dev"
(dictionary\|dictation) | "dict"
(direction\|directory) | "dir"
dynamic | "dyn"
example | "ex"
execute | "exec"
exception | "exc"
expression | "exp"
(extension\|extend) | "ext"
function | "func"
framework | "fw"
(initialize\|initializer) | "init"
instance | "inst"
integer | "int"
iterate | "iter"
java archive | "jar"
javascript | "js"
keyword | "kw"
keyword arguments | "kwargs"
language | "lng"
library | "lib"
length | "len"
number | "num"
object | "obj"
okay | "ok"
package | "pkg"
parameter | "param"
parameters | "params"
pixel | "px"
position | "pos"
point | "pt"
previous | "prev"
property | "prop"
python | "py"
query string | "qs"
reference | "ref"
references | "refs"
(represent\|representation) | "repr"
regular (expression\|expressions) | "regex"
request | "req"
revision | "rev"
ruby | "rb"
session aidee | "sid"
source | "src"
(special\|specify\|specific\|specification) | "spec"
standard | "std"
standard in | "stdin"
standard out | "stdout"
string | "str"
(synchronize\|synchronous) | "sync"
system | "sys"
utility | "util"
utilities | "utils"
temporary | "tmp"
text | "txt"
value | "val"
window | "win"
tab | "tab"
backspace | "backspace"
delete | "delete"
enter | "enter"
paste | "paste"
copy | "copy"
cut | "cut"
undo | release + Key("c-z/3")
release | "release"
select | "select"
select all | "select all"
abbreviate | "abbreviate"
uppercase | "uppercase"
lowercase | "lowercase"
expand | "expand"
dash | "dash"
underscore | "underscore"
dot | "dot"
period | "period"
minus | "minus"
semi-colon | "semi-colon"
hyphen | "hyphen"
up [\<n>] | Key("up:[n]")
down [\<n>] | Key("down:[n]")
left [\<n>] | Key("left:[n]")
right [\<n>] | Key("right:[n]")
pinch [\<n>] | Key("pgup:[n]")
page [\<n>] | Key("pgdown:[n]")
left [\<n>] (word\|words) | Key("c-left/3:[n]/10")
right [\<n>] (word\|words) | Key("c-right/3:[n]/10")
lend | Key("end")
lendit | Key("end, comma")
doc home | Key("c-home/3")
doc end | Key("c-end/3")
grab \<n> | release + Key("shift:down, right:[n], shift:up")
take \<n> | release + Key("shift:down, left:[n], shift:up")
take \<n> (line\|lines) | release + Key("end, shift:down, home, up:[n], home, shift:up")
grab \<n> (line\|lines) | release + Key("home, shift:down, down:[n], end, shift:up")
grab \<n> (word\|words) | release + Key("shift:down, c-right:[n], shift:up")
take \<n> (word\|words) | release + Key("shift:down, c-left:[n], shift:up")
(take\|grab) word | Key("c-left, sc-right")
(take\|grab) home | release + Key("shift:down, home, shift:up")
(take\|grab) end | release + Key("shift:down, end, shift:up")
(take\|grab) line | release + Key("home, s-end")
(take\|grab) all | release + Key("c-a/3")
act | Key("escape")
space [\<n>] | release + Key("space:[n]")
drop [\<n>] | release + Key("enter:[n]")
slide [\<n>] | release + Key("end, enter:[n]")
tab [\<n>] | Key("tab:[n]")
scratch [\<n>] | release + Key("backspace:[n]")
chuck [\<n>] | Key("del/3:[n]")
whack [\<n>] | Key("shift:down, c-left/3:[n]/10, del, shift:up")
bump [\<n>] | Key("shift:down, c-right/3:[n]/10, del, shift:up")
scratch [this] line | Key("home, s-end, del")
chuck [this] line | Key("home:2, s-end, backspace:2")
dump [that] | Function(paste_command)
nab [that] | Function(copy_command)
cut [that] | release + Key("c-x/3")
undo \<n> [times] | release + Key("c-z/3:[n]")
redo | release + Key("c-y/3")
redo \<n> [times] | release + Key("c-y/3:[n]")
save | release + Key("c-s")
app key | release + Key("apps/3")
mod key | release + Key("win/3")
[(hold\|press)] alt | Key("alt:down/3")
release alt | Key("alt:up")
[(hold\|press)] shift | Key("shift:down/3")
release shift | Key("shift:up")
[(hold\|press)] control | Key("ctrl:down/3")
release control | Key("ctrl:up")
release [all] | release
angles | Key("langle, rangle, left/3")
squares | Key("lbracket, rbracket, left/3")
braces | Key("lbrace, rbrace, left/3")
parens | Key("lparen, rparen, left/3")
quotes | Key("dquote/3, dquote/3, left/3")
single quotes | Key("squote, squote, left/3")
double \<char> | Text("[char][char]")
triple \<char> | Text("[char][char][char]")
double escape | Key("escape, escape")
colon [\<n>] | Key("colon/2:[n]")
(semi-colon\|semicolon) [\<n>] | Key("semicolon/2:[n]")
comma [\<n>] | Key("comma/2:[n]")
(dot\|period) [\<n>] | Key("dot/2:[n]")
(dash\|hyphen\|minus) [\<n>] | Key("hyphen/2:[n]")
underscore [\<n>] | Key("underscore/2:[n]")
camel \<n> [words] | Function(camel_case_count)
pascal \<n> [words] | Function(pascal_case_count)
snake \<n> [words] | Function(snake_case_count)
squash \<n> [words] | Function(squash_count)
expand \<n> [words] | Function(expand_count)
uppercase \<n> [words] | Function(uppercase_count)
lowercase \<n> [words] | Function(lowercase_count)
\<formatType> \<text> | Function(format_text)
say \<reservedWord> | Text("[reservedWord]")
short \<abbreviation> | Text("[abbreviation]")
(add\|fix) missing space | Key("c-left/3, space, c-right/3")
(delete\|remove) (double\|extra) (space\|whitespace) | Key("c-left/3, backspace, c-right/3")
(delete\|remove) (double\|extra) (type\|char\|character) | Key("c-left/3, del, c-right/3")
[\<text>] (go to sleep\|cancel and sleep) [\<text2>] | Function(cancel_and_sleep)
\<number> | Text("[number]")
\<letter> | Text("[letter]")
\<specialChar> | Text("[specialChar]")
Key | Key
Text | Text
press \<modifierSingle> | Key("[modifierSingle]")
press \<modifier1> \<pressKey> [\<n>] | Key("[modifier1]-[pressKey]:[n]")
press \<modifier1> \<modifier2> \<pressKey> [\<n>] | Key("[modifier1][modifier2]-[pressKey]:[n]")
n | 1
