from .grammar import ADBLOCK_GRAMMAR

from lark import Lark, Transformer


class Rule:
    def __init__(self):
        self.pattern = ''
        self.block = True
        self.match_domain = False

    def __str__(self):
        if self.match_domain and '/' not in self.pattern:
            return f'.{self.pattern}.'
        return self.pattern

    def __bool__(self):
        return bool(self.pattern)


class ADBTree(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rules = [Rule()]

    def filter_line(self, tok):
        self.rules.append(Rule())
        return tok

    def MATCH_DOMAIN(self, item):
        self.rules[-1].match_domain = True
        return item

    def BLOCKING_PATTERN(self, item):
        self.rules[-1].pattern += str(item).strip()
        return item

    def SEPARATOR(self, item):
        self.rules[-1].pattern += '/'
        return item


ADB_TREE_TRANSFORMER = ADBTree()


def get_privoxy_rules():
    return [r for r in ADB_TREE_TRANSFORMER.rules if r]


def create_parser(**kwargs):
    return Lark(ADBLOCK_GRAMMAR,
                transformer=ADB_TREE_TRANSFORMER,
                parser='lalr',
                **kwargs)
