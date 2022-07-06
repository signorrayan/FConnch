from argparse import ArgumentParser


G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white


def no_color():
    global G, Y, B, R, W
    G = Y = B = R = W = ''

def read_user_cli_args():
    """ Handle the cli arguments and options. """
    parser = ArgumentParser(
        prog="connch",
        description="check websites availability."
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more website URLs (seperated by space)."
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
    return parser.parse_args()

def display_check_result(response, url, error=""):
    """ Display the connectivity check result. """

    # if options.verbose:
    #     res = "\U0001F7E2" if result else f"\U0001F534\nError: {error}"
    # else:
    #     res = "\U0001F7E2" if result else f"\U0001F534"
    # print(f"{url} : {res}")

    if read_user_cli_args().verbose:
        message = f"{G}Online{W},{response}" if response else f"{R}Offline\nError: {error}{W}"
    else:
        message = f"{G}Online{W},{response}" if response else f"{R}Offline{W}"
    print(f"{url} : {message}")
