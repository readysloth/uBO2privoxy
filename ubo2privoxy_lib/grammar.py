UBO_GRAMMAR = r'''

COMMENT_LINE: /(!|#\s|####|\[adblock).*/i
INLINE_COMMENT: /(\s+#).*?$/
NEWLINE: /[\r\n]/
COND_IF: /!#if/
COND_ENDIF: /!#endif/
IGNORE: (COMMENT_LINE | INLINE_COMMENT)? NEWLINE
      | COND_IF /[^!]+/ COND_ENDIF NEWLINE

NOT: "~"
ANCHOR: "|"
DOMAIN_ANCHOR: "||"
EXCEPTION: "@@"
SEPARATOR_PLACEHOLDER: "^"

// Not accurate, but filters are not yet supported
NET_ANCHOR: "$" | "#$"
LOCALHOST: "127.0.0.1" | "localhost" | "local"
THISHOST: "0.0.0.0" | "broadcasthost"

REST_OF_LINE: /[^\r\n]+/
EXT_ANCHOR: /(#@?(\$\?|\$|%|\?)?#).{1,2}/
FILTER_OPT: NET_ANCHOR /.*/
PLAIN_GENERIC_COSMETIC: /#.?#/ REST_OF_LINE

DOMAIN: /[0-9a-zA-Z_.\-*]+/
PATH: /([^@^#~|$][0-9a-zA-Z%&,\-.\/:;=?_~*@]*)(?!.*##)/
PROTOCOL: /https?/
PROTOCOL_SEPARATOR: "://"

hosts: (LOCALHOST | THISHOST) " " PATH
url: ANCHOR? SEPARATOR_PLACEHOLDER? PATH SEPARATOR_PLACEHOLDER? ANCHOR? FILTER_OPT?
path_rule: DOMAIN_ANCHOR PATH SEPARATOR_PLACEHOLDER? ANCHOR? FILTER_OPT?
         | (PROTOCOL? PROTOCOL_SEPARATOR)? url
         | FILTER_OPT
cosmetic: (NOT? DOMAIN ","?)* PLAIN_GENERIC_COSMETIC

ubo_rule: hosts
        | cosmetic
        | path_rule
start: (EXCEPTION? ubo_rule | IGNORE)*
'''
