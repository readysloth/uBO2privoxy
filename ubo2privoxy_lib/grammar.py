UBO_GRAMMAR = r'''
WHITESPACE_START: /^\s+/
WHITESPACE_END: /\s+$/
COMMENT_LINE: /^(?:!|#\s|####|\[adblock)/i
EXT_ANCHOR: /(#@?(?:\$\?|\$|%|\?)?#).{1,2}/
INLINE_COMMENT: /(?:\s+#).*?$/
NET_EXCEPTION: /^@@/
NET_ANCHOR: /(?:)\$[^,\w~]/
HN_ANCHORED_PLAIN_ASCII: /^\|\|[0-9a-z%&,\-.\/:;=?_]+$/
HN_ANCHORED_HOSTNAME_ASCII: /^\|\|(?:[\da-z][\da-z_-]*\.)*[\da-z_-]*[\da-z]\^$/
HN_ANCHORED_HOSTNAME_UNICODE: /^\|\|(?:[\p{L}\p{N}][\p{L}\p{N}\u{2d}]*\.)*[\p{L}\p{N}\u{2d}]*[\p{L}\p{N}]\^$/u
HN3P_ANCHORED_HOSTNAME_ASCII: /^\|\|(?:[\da-z][\da-z_-]*\.)*[\da-z_-]*[\da-z]\^\$third-party$/
PLAIN_ASCII: /^[0-9a-z%&\-.\/:;=?_]{2,}$/
NET_HOSTS1: /^127\.0\.0\.1 (?:[\da-z][\da-z_-]*\.)+[\da-z-]*[a-z]$/
NET_HOSTS2: /^0\.0\.0\.0 (?:[\da-z][\da-z_-]*\.)+[\da-z-]*[a-z]$/
PLAIN_GENERIC_COSMETIC: /^##[.#][A-Za-z_][\w-]*$/
HOSTNAME_ASCII: /^(?:[\da-z][\da-z_-]*\.)*[\da-z][\da-z-]*[\da-z]$/
PLAIN_ENTITY: /^(?:[\da-z][\da-z_-]*\.)+\*$/
HOSTS_SINK: /^[\w%.:\[\]-]+\s+/
HOSTS_REDIRECT: /(?:0\.0\.0\.0|broadcasthost|local|localhost(?:\.localdomain)?|ip6-\w+)(?:[^\w.-]|$)/
NET_OPTION_COMMA: /,(?:~?[13a-z-]+(?:=.*?)?|_+)(?:,|$)/
POINTLESS_LEFT_ANCHOR: /^\|\|?\*+/
IS_TOKEN_CHAR: /^[%0-9A-Za-z]/
POINTLESS_LEADING_WILDCARDS: /^(\*+)[^%0-9A-Za-z\u{a0}-\u{10FFFF}]/u
POINTLESS_TRAILING_SEPARATOR: /\*(\^\**)$/
POINTLESS_TRAILING_WILDCARDS: /(?:[^%0-9A-Za-z]|[%0-9A-Za-z]{7,})(\*+)$/
HAS_WHITESPACE_CHAR: /\s/
HAS_UPPERCASE_CHAR: /[A-Z]/
HAS_UNICODE_CHAR: /[^\x00-\x7F]/
UNICODE_CHARS: /\P{ASCII}/gu
BAD_HOSTNAME_CHARS: /[\x00-\x24\x26-\x29\x2b\x2c\x2f\x3b-\x40\x5c\x5e\x60\x7b-\x7f]/
IS_ENTITY: /^[^*]+\.\*$/
PREPARSE_DIRECTIVE_IF: /^!#if /
PREPARSE_DIRECTIVE_ANY: /^!#(?:else|endif|if |include )/
URL: /\bhttps?:\/\/\S+/
HAS_PATTERN_SPECIAL_CHARS: /[\*\^]/
PATTERN_ALL_SPECIAL_CHARS: /[\*\^]+|[^\x00-\x7f]+/g
HAS_INVALID_CHAR: /[\x00-\x1F\x7F-\x9F\xAD\u061C\u200B-\u200F\u2028\u2029\uFEFF\uFFF9-\uFFFC]/
HOSTNAME_PATTERN_PART: /^[^\x00-\x24\x26-\x29\x2B\x2C\x2F\x3A-\x40\x5B-\x5E\x60\x7B-\x7F]+/
HOSTNAME_LABEL: /[^.]+/g
RESPONSEHEADER_PATTERN: /^\^responseheader\(.*\)$/
PATTERN_SCRIPTLET_JSON_ARGS: /^\{.*\}$/
GOOD_REGEX_TOKEN: /[^\x01%0-9A-Za-z][%0-9A-Za-z]{7,}|[^\x01%0-9A-Za-z][%0-9A-Za-z]{1,6}[^\x01%0-9A-Za-z]/
BAD_CSP: /(?:^|[;,])\s*report-(?:to|uri)\b/i
BAD_PP: /(?:^|[;,])\s*report-to\b/i
NOOP_OPTION: /^_+$/
'''
