from dragonfly import Repeat, Pause, Function, Choice, MappingRule, Dictation

from castervoice.lib.actions import Key, Mouse, Text
from castervoice.lib.merge.state.short import R, L, S
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails

class GitRule(MappingRule):

    mapping = {
        "git diff":
            R(Text("git diff") + Key("enter")),
        "git diff cached":
            R(Text("git diff --cached") + Key("enter")),
        "git show":
            R(Text("git show") + Key("enter")),
        "git commit":
            R(Text("git commit") + Key("enter")),
        "git commit amend":
            R(Text("git commit --amend") + Key("enter")),
        "git add partial":
            R(Text("git add -p") + Key("enter")),
        "git rebase interactive":
            R(Text("git rebase -i HEAD~")),
        "git rebase continue":
            R(Text("git rebase --continue")),
        "git reset hard":
            R(Text("git reset --hard")),
        "git fetch [all]":
            R(Text("git fetch --all") + Key("enter")),
        "git a log":
            R(Text("git alog") + Key("enter")),
        "git status":
            R(Text("git status") + Key("enter")),
        "git push sys":
            R(Text("git push hss $(git rev-parse --abbrev-ref HEAD)") + Key("enter")),
        "git tag":
            R(Text("git tag ")),
        "(git add partial)":
            R(Text("git add -p") + Key("enter")),
        "git push":
            R(Text("git push ")),
    }
    extras = [
    ]
    defaults = {}

def get_rule():
    return GitRule, RuleDetails(name="git", executable="alacritty")
