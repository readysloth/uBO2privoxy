#!/usr/bin/env python3

import sys
import argparse

from pprint import pformat

from ubo2privoxy_lib import create_parser, get_privoxy_rules


argparser = argparse.ArgumentParser()
argparser.add_argument(
    '-d', '--debug',
    action='store_true',
    help='Dump AST')
argparser.add_argument(
    'filter_files',
    default='-',
    nargs='*',
    help='File with UBO filters, default is stdin')
args = argparser.parse_args()

filter_files = [sys.stdin]
if args.filter_files != '-':
    filter_files = [open(filter_files, 'r')
                    for filter_files in args.filter_files]

parser = create_parser()

try:
    for file in filter_files:
        AST = parser.parse(file.read())
        if args.debug:
            print(pformat(AST.children, indent=2), file=sys.stderr)
finally:
    [file.close() for file in filter_files]

print(r'{+block{UBO2Privoxy}}')
for rule in get_privoxy_rules():
    if rule.not_supported:
        continue

    privoxy_line = str(rule)
    # optimization for domains
    if privoxy_line.endswith('[^a-zA-Z0-9_.%-]'):
        privoxy_line = privoxy_line.rstrip('[^a-zA-Z0-9_.%-]')
    if len(privoxy_line) < 8 or privoxy_line.startswith('http'):
        continue
    if rule.exception:
        print(r'{-block{UBO2Privoxy exception}}')
        print(privoxy_line)
        print(r'{+block{UBO2Privoxy}}')
        continue
    print(privoxy_line)
