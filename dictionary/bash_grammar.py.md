# bash_grammar.py

command | action
--- | ---
apt cache search \<text> | SCText("apt-cache search [text]")
apt cache show | Text("apt-cache show ")
apt cache show \<text> | SCText("apt-get show [text]")
apt get install | Text("apt-get install ")
apt get install \<text> | SCText("apt-get install [text]")
apt get update | Text("apt-get update") + Key("enter")
sudo apt get install | Text("sudo apt-get install ")
sudo apt get install \<text> | SCText("sudo apt-get install [text]")
sudo apt get update | Text("sudo apt-get update") + Key("enter")
background | Text("bg ")
(cat\|C A T) | Text("cat ")
(cat\|C A T) \<text> | SCText("cat [text]")
(change (directory\|dir)\|C D) | Text("cd ")
(change (directory\|dir)\|C D) \<text> | SCText("cd [text]")
[press] control break | Key("ctrl:down, c/10, ctrl:up")
(copy\|C P) | Text("cp ")
(copy\|C P) recursive | Text("cp -r ")
copy terminal | Key("cs-c/3")
(change mode)\|C H mod | Text("chmod ")
(cron\|cron tab\|crontab) edit | Text("crontab -e") + Key("enter")
(cron\|cron tab\|crontab) list | Text("crontab -l") + Key("enter")
(cron\|cron tab\|crontab) reset | Text("crontab -r")
diff | Text("diff ")
directory up \<n> [times] | Function(directory_up)
(D P K G\|D package) | Text("dpkg ")
(D P K G\|D package) list | Text("dpkg -l ")
exit | Text("exit")
foreground | Text("fg ")
find process | Text("ps aux | grep -i ")
find process \<text> | Text("ps aux | grep -i ") + Function(lib.format.snake_case_text)
find | Text("find . -name ")
find \<text> | SCText("find . -name [text]")
[go to] end of line | Key("c-e")
[go to] start of line | Key("c-a")
grep | Text("grep ")
grep invert | Text("grep -v ")
grep \<text> | SCText("grep [text]")
grep invert \<text> | SCText("grep -v [text]")
grep recursive | Text("grep -rn ") +  Key("dquote/3, dquote/3") + Text(" *") + Key("left/3:3")
grep recursive \<text> | Text("grep -rn ") + Key("dquote/3") + SCText("[text]") + Key("dquote/3") + Text(" *") + Key("left/3:3")
history | Text("history ")
ifconfig | Text("ifconfig ")
(iptables\|I P tables) list | Text("iptables -L")
(iptables\|I P tables) flush | Text("iptables -F")
jobs | Text("jobs ")
kill | Text("kill ")
kill (hard\|[dash]9) | Text("kill -9 ")
kill line | Key("c-k")
(link\|L N) | Text("ln ")
list files | Text("ls -la") + Key("enter")
list files \<text> | SCText("ls -la [text]")
list files time sort | Text("ls -lat") + Key("enter")
make (directory\|dir) | Text("mkdir ")
make (directory\|dir) \<text> | SCText("mkdir [text]")
move | Text("mv ")
move \<text> | SCText("mv [text]")
paste terminal | Key("cs-v/3")
pipe | Text(" | ")
ping | Text("ping ")
(print working directory\|P W D) | Text("pwd") + Key("enter")
([list] processes [list]\|P S) | Text("ps -ef")
(R M\|remove file) | Text("rm ")
(R M\|remove file) \<text> | SCText("rm [text]")
remove (directory\|dir\|folder\|recursive) | Text("rm -rf ")
remove (directory\|dir\|folder\|recursive) \<text> | SCText("rm -rf [text]")
(sed\|S E D) | Text("sed ")
(secure copy\|S C P) | Text("scp ")
(secure copy\|S C P) \<text> | SCText("scp [text]")
(secure shell\|S S H) | Text("ssh ")
(secure shell\|S S H) \<text> | SCText("ssh [text]")
soft link | Text("ln -s ")
soft link \<text> | SCText("ln -s [text]")
sudo | Text("sudo ")
(switch user\|S U) | Text("su ")
(switch user\|S U) login | Text("su - ")
tail | Text("tail ")
tail \<text> | SCText("tail [text]")
tail (F\|follow) | Text("tail -f ")
tail (F\|follow) \<text> | SCText("tail -f [text]")
telnet | Text("telnet ")
touch | Text("touch ")
touch \<text> | SCText("touch [text]")
vim | Text("vim ")
vim \<text> | SCText("vim [text]")
(W C\|word count) | Text("wc ")
(W C\|word count) lines | Text("wc -l ")
W get  | Text("wget ")
X args | Text("xargs ")
X D O tool | Text("xdotool ")
X M L lint | Text("xmllint ")
X M L lint \<text> | SCText("xmllint [text]")
X M L lint format | Text("xmllint -format ")
X M L lint format \<text> | SCText("xmllint -format [text]")
X M L lint schema | Text("xmllint -schema ")
X M L lint schema \<text> | SCText("xmllint -schema [text]")
X prop | Text("xprop ")
X win info | Text("xwininfo ")
