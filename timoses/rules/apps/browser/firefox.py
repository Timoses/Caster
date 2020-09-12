from dragonfly import Repeat, Pause, Function, Choice, MappingRule, Dictation

from castervoice.lib.actions import Key, Mouse, Text

from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

from castervoice.lib import github_automation
from castervoice.lib.temporary import Store, Retrieve

class FirefoxRule(MappingRule):
    mapping = {
        "(new window|window new)":
            R(Key("w-n")),
        "(new incognito window | incognito)":
            R(Key("ws-p")),
        "window close|close all tabs":
            R(Key("cs-w")),
        "new tab [<n>]|tab new [<n>]":
            R(Key("w-t") * Repeat(extra="n")),
        "reopen tab [<n>]|tab reopen [<n>]":
            R(Key("ws-t")) * Repeat(extra="n"),
        "(back|previous) tab [<n>]|tab (left|lease) [<n>]":
            R(Key("cs-tab")) * Repeat(extra="n"),
        "(next|forward) tab [<n>]|tab (right|sauce) [<n>]":
            R(Key("c-tab")) * Repeat(extra="n"),
        "close tab [<n>]|tab close [<n>]":
            R(Key("w-w")) * Repeat(extra='n'),
        "go (back|prev|prior|previous) [<n>]":
            R(Key("w-left/20")) * Repeat(extra="n"),
        "go (next|forward) [<n>]":
            R(Key("w-right/20")) * Repeat(extra="n"),
        "find (next|forward) [match] [<n>]":
            R(Key("w-g/20")) * Repeat(extra="n"),

        "find <search>":
            R(Key("w-f/20")) + Text("%(search)s"),
        "search <search>":
            R(Key("w-l/20")) + Text("%(search)s")
    }
    extras = [
        Choice("nth", {
                "first": "1",
                "second": "2",
                "third": "3",
                "fourth": "4",
                "fifth": "5",
                "sixth": "6",
                "seventh": "7",
                "eighth": "8",
            }),
        IntegerRefST("n", 1, 100),
        IntegerRefST("m", 1, 10),
        Dictation("search")
    ]
    defaults = {"n": 1, "m":"", "nth": ""}

def get_rule():
    return FirefoxRule, RuleDetails(name="fire fox", executable="firefox")
