ADBLOCK_GRAMMAR = r'''
ANCHOR: "|"
EXCEPTION: "@@"
FILTER_OPT_START: "$"
SEPARATOR: "^"
MATCH_DOMAIN: "||"
REGEX_MARK: "/"

REGEX_BODY: /(\\\/|[^\/])+/
ELEM_HIDING_MARK: /#.?#/
ELEM_HIDING: ELEM_HIDING_MARK /[^\r\n]*/
FILTER_OPT: /[^,\s]*/
VALID_URL: /[-a-zA-Z0-9@:%._\+~#=\/*?&;]+/
BLOCKING_PATTERN: VALID_URL
FILTER_OPTS: FILTER_OPT_START (FILTER_OPT ","?)*

SKIP_PATTERNS: ELEM_HIDING_MARK | /^~/
SKIP: /[^\n]*/ SKIP_PATTERNS /[^\n]*/
COMMENT: "!" /[^\n]*/
_EOL: /[\t ]*\r?\n/
_NEWLINE.9999: ( _EOL | COMMENT | SKIP)+

regex: REGEX_MARK REGEX_BODY REGEX_MARK
blocking_pattern: regex
                | SEPARATOR? (BLOCKING_PATTERN SEPARATOR?)+
rule_opt: (ANCHOR | EXCEPTION | MATCH_DOMAIN)~0..2
filter_line: _NEWLINE
           | rule_opt? FILTER_OPTS
           | rule_opt? blocking_pattern FILTER_OPTS?
filter_file: filter_line*

?start: filter_file

%ignore COMMENT
%ignore _NEWLINE
%ignore _EOL
%ignore ANCHOR
%ignore SKIP
'''
