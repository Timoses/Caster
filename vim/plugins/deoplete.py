from dragonfly import MappingRule, Key, Text, IntegerRef

class DeopleteRule(MappingRule):
    exported = True
    mapping = {
        # deo
        "day oh <n>": Text("0%(n)d"),
    }
    extras = [
        IntegerRef("n", 1, 100)
    ]
    defaults = {
        "n": 1,
    }

