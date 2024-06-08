from .grammar import UBO_GRAMMAR

from lark import Lark, Transformer


class Rule:
    def __init__(self):
        self.block = True
        self.contents = ''
        self.is_comment = False
        self.is_domain = False
        self.can_be_in_hosts = False
        self.exception = False
        self.possibly_chains = False

        self.not_supported = False

    def __str__(self):
        if self.is_domain:
            return self.contents
        return self.contents.replace('*', '.*')

    def __bool__(self):
        return bool(self.contents)


class ADBTree(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rules = [Rule()]
        self.current_obj = self.rules[-1]

    def ubo_rule(self, item):
        self.rules.append(Rule())
        self.current_obj = self.rules[-1]
        return item

    def EXCEPTION(self, item):
        self.current_obj.exception = True
        return item

    def IGNORE(self, item):
        if str(item) == '\n':
            return item
        ignore_escape = str(item).replace("\n", "# \n").strip()
        self.current_obj.contents = f'# {ignore_escape}'
        self.rules.append(Rule())
        self.current_obj = self.rules[-1]
        return item

    def DOMAIN_ANCHOR(self, item):
        self.current_obj.is_domain = True
        return item

    def PATH(self, item):
        item_str = str(item)
        self.current_obj.is_domain = any(c not in item_str for c in '/*?')
        if self.current_obj.is_domain:
            self.current_obj.can_be_in_hosts = True
        self.current_obj.contents = item_str
        return item

    DOMAIN = PATH

    def SEPARATOR_PLACEHOLDER(self, item):
        self.current_obj.possibly_chains = True
        self.current_obj.contents += r'[^a-zA-Z0-9_.%-]'
        return item

    # Not yet implemented
    def FILTER_OPT(self, item):
        if str(item):
            self.current_obj.not_supported = True
        return item

    # Not yet implemented
    def PLAIN_GENERIC_COSMETIC(self, item):
        self.current_obj.not_supported = True
        return item

    def cosmetic(self, item):
        if item[0].type == 'PLAIN_GENERIC_COSMETIC':
            self.rules[-2].not_supported = True
        return item

    def hosts(self, item):
        self.current_obj.can_be_in_hosts = True
        self.current_obj.contents = str(item)
        return item


ADB_TREE_TRANSFORMER = ADBTree()


def get_privoxy_rules():
    return [r for r in ADB_TREE_TRANSFORMER.rules if r]


def create_parser(**kwargs):
    return Lark(UBO_GRAMMAR,
                transformer=ADB_TREE_TRANSFORMER,
                parser='lalr',
                **kwargs)
