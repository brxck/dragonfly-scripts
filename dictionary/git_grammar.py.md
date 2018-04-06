# git_grammar.py

command | action
all | "--all"
help | "--help"
show | "show"
skip | "--skip"
move | "move"
git diff cached | Text("git diff --cached ")
git diff cached <text> | SCText("git diff --cached %(text)s")
git remote rename <text> | SCText("git remote rename %(text)s")
git add (all|period|dot) | Text("git add .") + Key("enter")
git fetch prune | Text("git fetch -p")
git remote | Text("git remote") + Key("enter")
graph | "--graph"
cache | "--cache"
git log graph limit <n> | Text("git log --graph --oneline --decorate --all -n %(n)d") + Key("enter")
git (check out|checkout) branch <text> | SCText("git checkout -b %(text)s")
git push | Text("git push")
git remote rename | Text("git remote rename ")
ours | "--ours"
git command <gitcmd> | Text("git %(gitcmd)s ")
git config list | Text("git config --list") + Key("enter")
git (rebase|re-base) <text> | SCText("git rebase %(text)s")
format | "--format"
git (check out|checkout) force <text> | SCText("git checkout -f %(text)s")
git diff staged <text> | SCText("git diff --staged %(text)s")
no (check out|checkout) | "--no-checkout"
git (move|M V) <text> | SCText("git mv %(text)s")
(diff|difference|differentiate) | "diff"
git remote prune  | Text("git remote prune ")
git log | Text("git log") + Key("enter")
git tag delete | Text("git tag -d ")
cached | "--cached"
rebase | "rebase"
git branch <text> | SCText("git branch %(text)s")
patch | "--patch"
git config | Text("git config ")
no color | "--no-color"
continue | "--continue"
git branch delete <text> | SCText("git branch -d %(text)s")
git merge (no (fast forward|F F)) <text> | SCText("git merge --no-ff %(text)s")
git log limit <n> | Text("git log -n %(n)d") + Key("enter")
force | "--force"
list | "--list"
hard | "--hard"
git (status|S T) <gitopt> | Text("git status %(gitopt)s") + Key("enter")
git push all | Text("git push --all") + Key("enter")
git revert head | Text("git revert HEAD")
git cherry-pick | Text("git cherry-pick ")
git revert | Text("git revert ")
git stash | Text("git stash") + Key("enter")
merge | "merge"
git tag (annotate|annotated) | Text("git tag -a  -m ") + Key("dquote/3, dquote/3, left/3:6")
git remote add | Text("git remote add ")
version | "--version"
git commit | Text("git commit -m ") + Key("dquote/3, dquote/3, left/3")
git (remove|R M) | Text("git rm ")
no tags | "--no-tags"
no fast forward | "--no-ff"
dry run | "--dry-run"
git (check out|checkout) | Text("git checkout ")
tags | "--tags"
git (init|initialize) bare | Text("git init --bare") + Key("enter")
porcelain | "--porcelain"
git show | Text("git show ")
blame | "blame"
git add <text> | SCText("git add %(text)s")
base | "--base"
git commit amend | Text("git commit --amend -m ")
git tag | Text("git tag ")
git diff <text> | SCText("git diff %(text)s")
git config add | Text("git config --add ")
(one line|oneline) | "--oneline"
theirs | "--theirs"
quiet | "--quiet"
(init|initialize) | "init"
git commit all tracked | Text("git commit -a -m ") + Key("dquote/3, dquote/3, left/3")
commit | "commit"
revert | "revert"
git help <gitcmd> | Text("git --help %(gitcmd)s") + Key("enter")
verbose | "--verbose"
color | "--color"
(check out|checkout) | "checkout"
git reset hard | Text("git reset --hard")
git remote show <text> | SCText("git remote show %(text)s")
message | "--message"
git blame | Text("git blame ")
log | "log"
git remote <gitopt> | Text("git remote %(gitopt)s")
git grep | Text("git grep \"\"") + Key("left:1")
add | "--add"
git (init|initialize) | Text("git init") + Key("enter")
git merge | Text("git merge ")
git push origin  | Text("git push origin ")
git help | Text("git --help") + Key("enter")
git (check out|checkout) <text> | SCText("git checkout %(text)s")
git archive | Text("git archive --format=tar ")
git (check out|checkout) force | Text("git checkout -f ")
git diff | Text("git diff ")
remote | "--remote"
git config add <text> | SCText("git config --add %(text)s ")
reset | "reset"
grep | "grep"
git remote add <text> | SCText("git remote add %(text)s")
git log graph | Text("git log --graph --oneline --decorate --all") + Key("enter")
amend | "--amend"
git branch delete  | Text("git branch -d ")
staged | "--staged"
git remote prune <text> | SCText("git remote prune %(text)s")
decorate | "--decorate"
git add patch <text> | SCText("git add --patch %(text)s")
git clone <text> | SCText("git clone %(text)s")
fetch | "fetch"
git (status|S T) | Text("git status") + Key("enter")
delete | "--delete"
git merge <text> | SCText("git merge %(text)s")
git add patch | Text("git add --patch ")
git clone | Text("git clone ")
git (check out|checkout) branch | Text("git checkout -b ")
git merge (no (fast forward|F F)) | Text("git merge --no-ff ")
git remote show | Text("git remote show ")
tag | "tag"
git pull | Text("git pull ")
git fetch | Text("git fetch") + Key("enter")
git (rebase|re-base) | Text("git rebase ")
git remote (remove|R M) <text> | SCText("git remote rm %(text)s")
branch | "branch"
git remote (remove|R M) | Text("git remote rm ")
config | "config"
git option <gitopt> | Text(" %(gitopt)s")
git stash pop | Text("git stash pop") + Key("enter")
status | "status"
git (remove|R M) <text> | SCText("git rm %(text)s")
track | "--track"
git push origin <text> | SCText("git push origin %(text)s")
git branch track | Text("git branch -- track ")
git push tags | Text("git push --tags") + Key("enter")
short | "--short"
(remove|R M) | "rm"
git diff staged | Text("git diff --staged ")
git (move|M V) | Text("git mv ")
git pull origin <text> | SCText("git pull origin %(text)s")
git fetch <text> | SCText("git fetch %(text)s ")
git add | Text("git add ")
push | "push"
git branch | Text("git branch") + Key("enter")
git push origin <gitopt> | SCText("git push origin %(gitopt)s")
