from dragonfly import Repeat, Pause, Function, Choice, MappingRule, Dictation

from castervoice.lib.actions import Key, Mouse, Text

from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R, L, S
from castervoice.lib.merge.state.actions import ContextSeeker
from castervoice.lib.merge.state.actions2 import NullAction

from castervoice.lib import github_automation
from castervoice.lib.temporary import Store, Retrieve

from libtmux import Server

from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Tmux(object):
    _server  = None
    _session = None

    """Docstring for Tmux. """

    def __init__(self):
        """TODO: to be defined. """
        self._server = Server()
        self._session = self._server.sessions[0]

    def window_new(self):
        self._session.new_window()

    def window_close(self):
        self._session.attached_window.kill_window()

    def window_n(self, **defaults):
        self._session.select_window(defaults['n'])

    def pane_display(self):
        self._server.cmd('display-panes', '-d1000')

    def pane_dir_n(self, **defaults):
        if 'dir' in defaults:
            dir_options = {
                Direction.UP: "-U",
                Direction.DOWN: "-D",
                Direction.LEFT: "-L",
                Direction.RIGHT: "-R"
            }

            self._session.attached_window.select_pane(dir_options[defaults['dir']])
        else:
            self._session.attached_window.select_pane(defaults['n'])

    def pane_n(self, **defaults):
        self._session.attached_window.select_pane(defaults['n'])

    def pane_zoom(self):
        self._session.attached_window.attached_pane.cmd('resize-pane', '-Z')

    def pane_new(self, dir, _node):
        args = "-"
        dir_options = {
            Direction.UP: "vb",
            Direction.DOWN: "v",
            Direction.LEFT: "hb",
            Direction.RIGHT: "h"
        }

        args = args + dir_options[dir]

        if _node.results[-1][0] == 'full':
            args += "f"

        self._session.attached_window.cmd('split-window', args)


    def pane_close(self):
        self._session.attached_window.attached_pane.cmd('kill-pane')

    def layout(self, _node, layout=None):
        if _node.results[-1][0] == 'even':
            self._session.attached_window.cmd('select-layout', '-E')
        else:
            self._session.attached_window.cmd('select-layout', layout)



class TmuxRule(MappingRule):

    tmux = Tmux()

    mapping = {
        "(window new)":
            R(Function(tmux.window_new)),
        "(window close)":
            R(Function(tmux.window_close)),
        "(window (<n>|last))":
            R(Function(tmux.window_n)),
        "pane (<dir>|<n>)":
            R(Function(tmux.pane_dir_n)),
        "pane (zoom|unzoom)":
            R(Function(tmux.pane_zoom)),
        "pane new <dir> [full]":
            R(Function(tmux.pane_new)),
        "pane close":
            R(Function(tmux.pane_close)),
        "pane":
            R(Function(tmux.pane_display), rspec="pane_n"),
        "<n>":
            ContextSeeker([
                L(
                    S(["default"], NullAction()),
                    S(["pane_n"], Function(tmux.pane_n))
                )
            ]),
        "layout [(<layout>|even)]":
            R(Function(tmux.layout)),
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
        Choice("dir", {
                "lease": Direction.LEFT,
                "left": Direction.LEFT,
                "ross": Direction.RIGHT,
                "right": Direction.RIGHT,
                "dunce": Direction.DOWN,
                "down": Direction.DOWN,
                "sauce": Direction.UP,
                "up": Direction.UP,
            }),
        IntegerRefST("n", 0, 100),
        IntegerRefST("m", 1, 10),
        Dictation("search"),
        Choice("layout", {
                "horizontal|whore": "even-horizontal",
                "vertical|virt": "even-vertical",
                "tiled|tile": "tiled"
            }),
    ]
    defaults = {
            "n": 1,
            "m":"",
            "nth": ""
    }

def get_rule():
    return TmuxRule, RuleDetails(name="t mux", executable="alacritty")

