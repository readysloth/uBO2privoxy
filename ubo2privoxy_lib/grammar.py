ADBLOCK_GRAMMAR = r'''
ANCHOR: "|"
EXCEPTION: "@@"
FILTER_OPT_START: "$"
SEPARATOR: "^"
MATCH_DOMAIN: "||"

ELEM_HIDING_MARK: /#.?#/
ELEM_HIDING: ELEM_HIDING_MARK /[^\r\n]*/
FILTER_OPT: /[^,\s]*/
BLOCKING_PATTERN: /[^^|$\r\n]+/
FILTER_OPTS: FILTER_OPT_START (FILTER_OPT ","?)*

SKIP_PATTERNS: ELEM_HIDING_MARK | /^~/
SKIP: /[^\n]*/ SKIP_PATTERNS /[^\n]*/
COMMENT: "!" /[^\n]*/
_EOL: /[\t ]*\r?\n/
_NEWLINE.9999: ( _EOL | COMMENT )+


blocking_pattern: SEPARATOR? (BLOCKING_PATTERN SEPARATOR?)+
rule_opt: (ANCHOR | EXCEPTION | MATCH_DOMAIN)~0..2
filter_line: _NEWLINE
           | FILTER_OPTS
           | rule_opt? blocking_pattern FILTER_OPTS?
           | rule_opt? blocking_pattern? FILTER_OPTS
filter_file: filter_line*

?start: filter_file

%ignore COMMENT
%ignore _NEWLINE
%ignore _EOL
%ignore ANCHOR
%ignore SKIP
'''
