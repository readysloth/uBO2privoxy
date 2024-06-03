import sys
import argparse


from ubo2privoxy_lib import create_parser, get_privoxy_rules


argparser = argparse.ArgumentParser()
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
        parser.parse(file.read())
finally:
    [file.close() for file in filter_files]

print(r'+block{UBO2Privoxy}')
for rule in get_privoxy_rules():
    print(str(rule))
