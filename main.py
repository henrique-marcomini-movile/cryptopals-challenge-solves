"""
The Cryptopals Crypto Challenges For Python

Usage:
  tcccfp all [--no-banner]
  tcccfp set <set_number> [--no-banner]
  tcccfp chall <chall_number> [--no-banner]
  tcccfp -h | --version
  
Commands:
  all         Tests every challenge.
  set         Tests every challenge of a set.
  chall       Tests a single challenge.

Options:
  -h --help     Show this screen.
  --version     Show version.
  --no-banner   Does not displays the beautiful banner

"""

from docopt import docopt

def print_banner():
    with open("banner.txt", 'r') as f:
        print(f.read())
        print('\n\n')


if __name__ == "__main__":
    args = docopt(__doc__)
    
    if not args['--no-banner']:
        print_banner()

    