'''
Test file for handling command-line arguments
'''

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')

parser.add_argument('-v', '--verbose', help='turn on verbosity',
    action='count', default=0)

args = parser.parse_args()
answer = args.x ** args.y

if args.verbose >=2:
  print('Running from "{}"'.format(__file__))
if args.verbose >=1:
  print('{}^{} = '.format(args.x, args.y), end='')

print(answer)
