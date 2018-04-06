# git_grammar.py

command | action
--- | ---
git diff \<text> | SCText("git diff [xtext]")
all | "--all"
help | "--help"
show | "show"
skip | "--skip"
move | "move"
git diff cached | Text("git diff --cached ")
git branch delete \<text> | SCText("git branch -d [xtext]")
git add (all|period|dot) | Text("git add .") + Key("enter")
git fetch prune | Text("git fetch -p")
git remote | Text("git remote") + Key("enter")
graph | "--graph"
cache | "--cache"
git command \<gitcmd> | Text("git [xgitcmd] ")
add | "--add"
git push | Text("git push")
git remote rename | Text("git remote rename ")
ours | "--ours"
git (move|M V) \<text> | SCText("git mv [xtext]")
git diff staged \<text> | SCText("git diff --staged [xtext]")
git config list | Text("git config --list") + Key("enter")
format | "--format"
git diff cached \<text> | SCText("git diff --cached [xtext]")
git merge \<text> | SCText("git merge [xtext]")
no (check out|checkout) | "--no-checkout"
(diff|difference|differentiate) | "diff"
git remote prune  | Text("git remote prune ")
git log | Text("git log") + Key("enter")
git tag delete | Text("git tag -d ")
cached | "--cached"
git log graph limit \<n> | Text("git log --graph --oneline --decorate --all -n [xn]") + Key("enter")
rebase | "rebase"
list | "--list"
patch | "--patch"
git config | Text("git config ")
no color | "--no-color"
continue | "--continue"
git help \<gitcmd> | Text("git --help [xgitcmd]") + Key("enter")
force | "--force"
revert | "revert"
hard | "--hard"
git push all | Text("git push --all") + Key("enter")
git branch \<text> | SCText("git branch [xtext]")
git log limit \<n> | Text("git log -n [xn]") + Key("enter")
git cherry-pick | Text("git cherry-pick ")
git revert | Text("git revert ")
git stash | Text("git stash") + Key("enter")
merge | "merge"
git option \<gitopt> | Text(" [xgitopt]")
git tag (annotate|annotated) | Text("git tag -a  -m ") + Key("dquote/3, dquote/3, left/3:6")
git remote add | Text("git remote add ")
version | "--version"
git commit | Text("git commit -m ") + Key("dquote/3, dquote/3, left/3")
git (remove|R M) | Text("git rm ")
no tags | "--no-tags"
no fast forward | "--no-ff"
dry run | "--dry-run"
git (check out|checkout) | Text("git checkout ")
git merge (no (fast forward|F F)) \<text> | SCText("git merge --no-ff [xtext]")
tags | "--tags"
git (init|initialize) bare | Text("git init --bare") + Key("enter")
porcelain | "--porcelain"
git pull origin \<text> | SCText("git pull origin [xtext]")
blame | "blame"
base | "--base"
git commit amend | Text("git commit --amend -m ")
git tag | Text("git tag ")
git (status|S T) \<gitopt> | Text("git status [xgitopt]") + Key("enter")
git config add | Text("git config --add ")
git add \<text> | SCText("git add [xtext]")
git revert head | Text("git revert HEAD")
(one line|oneline) | "--oneline"
theirs | "--theirs"
git remote prune \<text> | SCText("git remote prune [xtext]")
quiet | "--quiet"
git reset hard | Text("git reset --hard")
(init|initialize) | "init"
git commit all tracked | Text("git commit -a -m ") + Key("dquote/3, dquote/3, left/3")
git fetch \<text> | SCText("git fetch [xtext] ")
commit | "commit"
delete | "--delete"
git push origin \<text> | SCText("git push origin [xtext]")
git (remove|R M) \<text> | SCText("git rm [xtext]")
verbose | "--verbose"
color | "--color"
(check out|checkout) | "checkout"
git remote add \<text> | SCText("git remote add [xtext]")
git show | Text("git show ")
message | "--message"
git blame | Text("git blame ")
log | "log"
git grep | Text("git grep \"\"") + Key("left:1")
git remote rename \<text> | SCText("git remote rename [xtext]")
git (init|initialize) | Text("git init") + Key("enter")
git config add \<text> | SCText("git config --add [xtext] ")
git merge | Text("git merge ")
git push origin  | Text("git push origin ")
git help | Text("git --help") + Key("enter")
git archive | Text("git archive --format=tar ")
git (check out|checkout) force | Text("git checkout -f ")
git diff | Text("git diff ")
remote | "--remote"
reset | "reset"
grep | "grep"
git log graph | Text("git log --graph --oneline --decorate --all") + Key("enter")
amend | "--amend"
git branch delete  | Text("git branch -d ")
staged | "--staged"
git push origin \<gitopt> | SCText("git push origin [xgitopt]")
decorate | "--decorate"
git add patch \<text> | SCText("git add --patch [xtext]")
fetch | "fetch"
git (status|S T) | Text("git status") + Key("enter")
git clone \<text> | SCText("git clone [xtext]")
git add patch | Text("git add --patch ")
git clone | Text("git clone ")
git (check out|checkout) branch | Text("git checkout -b ")
git merge (no (fast forward|F F)) | Text("git merge --no-ff ")
git (rebase|re-base) \<text> | SCText("git rebase [xtext]")
git (check out|checkout) branch \<text> | SCText("git checkout -b [xtext]")
git remote show | Text("git remote show ")
tag | "tag"
git remote (remove|R M) \<text> | SCText("git remote rm [xtext]")
git pull | Text("git pull ")
git (check out|checkout) \<text> | SCText("git checkout [xtext]")
git fetch | Text("git fetch") + Key("enter")
git (rebase|re-base) | Text("git rebase ")
branch | "branch"
git remote (remove|R M) | Text("git remote rm ")
git (check out|checkout) force \<text> | SCText("git checkout -f [xtext]")
config | "config"
git stash pop | Text("git stash pop") + Key("enter")
status | "status"
git remote show \<text> | SCText("git remote show [xtext]")
track | "--track"
git branch track | Text("git branch -- track ")
git push tags | Text("git push --tags") + Key("enter")
short | "--short"
(remove|R M) | "rm"
git diff staged | Text("git diff --staged ")
git (move|M V) | Text("git mv ")
git remote \<gitopt> | Text("git remote [xgitopt]")
git add | Text("git add ")
push | "push"
git branch | Text("git branch") + Key("enter")
