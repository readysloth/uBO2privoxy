ADBLOCK_GRAMMAR = r'''
ANCHOR: "|"
EXCEPTION: "@@"
FILTER_OPT_START: "$"
SEPARATOR: "^"
MATCH_DOMAIN: "||"

ELEM_HIDING_MARK: /#.?#/
ELEM_HIDING: ELEM_HIDING_MARK /[^\r\n]*/ _NEWLINE
FILTER_OPT: /[^,\s]*/
BLOCKING_PATTERN: /[^^@|$#]+/ ELEM_HIDING?
FILTER_OPTS: FILTER_OPT_START (FILTER_OPT ","?)*

COMMENT: /![^\n]*/
_NEWLINE: ( /[\t ]*\r?\n/ | COMMENT )+


blocking_pattern: SEPARATOR? (BLOCKING_PATTERN SEPARATOR?)+
?rule_opt: (ANCHOR | EXCEPTION | MATCH_DOMAIN)~0..2
filter_line: _NEWLINE | rule_opt? blocking_pattern FILTER_OPTS?
filter_file: filter_line*

?start: filter_file

%ignore COMMENT
%ignore _NEWLINE
'''
