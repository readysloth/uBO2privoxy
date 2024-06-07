UBO_GRAMMAR = r'''

COMMENT_LINE: /(?:!|#\s|####|\[adblock).*/i
INLINE_COMMENT: /(?:\s+#).*?$/
NEWLINE: /[\r\n]/
IGNORE: (COMMENT_LINE | INLINE_COMMENT)? NEWLINE
%ignore IGNORE

NOT: "~"
ANCHOR: "||"
EXCEPTION: "@@"
SEPARATOR_PLACEHOLDER: "^"
NET_ANCHOR: "$"
LOCALHOST: "127.0.0.1" | "localhost" | "local"
THISHOST: "0.0.0.0" | "broadcasthost"

REST_OF_LINE: /[^\r\n]+/
EXT_ANCHOR: /(#@?(?:\$\?|\$|%|\?)?#).{1,2}/
FILTER_OPT: NET_ANCHOR /.*/
PLAIN_GENERIC_COSMETIC: "##" REST_OF_LINE

PATH: /[0-9a-z%&,\-.\/:;=?_]+/
ANCHORED_PATH: /^[0-9a-z%&,\-.\/:;=?_]+/
PROTOCOL: /https?/
PROTOCOL_SEPARATOR: "://"

hosts: (LOCALHOST | THISHOST) " " PATH
url: PROTOCOL? PROTOCOL_SEPARATOR REST_OF_LINE
   | ANCHORED_PATH SEPARATOR_PLACEHOLDER? FILTER_OPT?
path_rule: EXCEPTION? ANCHOR PATH SEPARATOR_PLACEHOLDER? FILTER_OPT?
         | url
cosmetic: (NOT? PATH ","?)* PLAIN_GENERIC_COSMETIC

ubo_rule: hosts
        | cosmetic
        | path_rule
start: (ubo_rule | IGNORE)*
'''
