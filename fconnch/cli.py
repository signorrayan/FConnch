from argparse import ArgumentParser

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white
BLD = '\033[1m'


def banner():
    print(r"""{}{}
 _____ ____                       _
|  ___/ ___|___  _ __  _ __   ___| |__
| |_ | |   / _ \| '_ \| '_ \ / __| '_ \
|  _|| |__| (_) | | | | | | | (__| | | |
|_|   \____\___/|_| |_|_| |_|\___|_| |_|

{}{}# Coded By Mohammadreza Sarayloo - @signorrayan {}
""".format(BLD, G, W, B, W))
    print(f"\n\n{BLD}{'|':30}{'Domain':32}{'|':5}{'Availability':15}{'|':5}{'Status':10}|{W}\n|", '-' * 96)


def no_color():
    global G, Y, B, R, W, BLD
    G = Y = B = R = W = BLD = ''


def read_user_cli_args():
    """ Handle the cli arguments and options. """
    parser = ArgumentParser(
        prog="fconnch",
        description="Check websites availability."
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more website URLs (separated by space)."
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from a file."
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="Run the connectivity check asynchronously",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        default=False,
        help="Shows if any error exists related to the dns resolve"
    )
    parser.add_argument(
        '-n',
        '--no-color',
        help='Output without color',
        default=False,
        action='store_true'
    )
    parser.add_argument(
        '-t',
        '--timeout',
        help='Set timeout - default is 3s',
        default=3,
        type=int,
    )
    return parser.parse_args()


def display_check_result(response, url, error=""):
    """ Display the connectivity check result. """
    message = f"{BLD}{G}{'Online':12}{W}{'|':6}{BLD}{B}{response}{W}" if response else f"{R}{BLD}{'Offline':12}{W}{'|':6}{R}{error}{W}"
    print(f"| {url:60}{'|':8}{message}")
