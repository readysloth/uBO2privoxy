import re

from .grammar import ADBLOCK_GRAMMAR

from lark import Lark, Transformer


class Rule:
    def __init__(self):
        self.pattern = ''
        self.block = True
        self.match_domain = False
        self.regex_body = False
        self.exception = False

    def __str__(self):
        output_str = self.pattern

        if self.exception:
            exception_start = r'{-block{exception}}'
            exception_end = r'{+block{exception_end}}'
            output_str = f'{exception_start}\n{output_str}\n{exception_end}'
        if self.match_domain and '/' not in self.pattern:
            if output_str[0] != '.':
                output_str = f'.{output_str}'
            if output_str[-1] != '.':
                output_str = f'{output_str}.'
            return output_str
        if self.regex_body:
            return output_str
        if output_str[-1] == '/':
            output_str = output_str[:-1]
        return output_str.replace('?', r'\?').replace(r'\*', '.*')

    def __bool__(self):
        return bool(self.pattern)


class ADBTree(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rules = [Rule()]

    def filter_line(self, tok):
        self.rules.append(Rule())
        return tok

    def EXCEPTION(self, item):
        self.rules[-1].exception = True
        return item

    def REGEX_BODY(self, item):
        self.rules[-1].pattern = str(item).strip()
        self.rules[-1].regex_body = True
        return item

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
