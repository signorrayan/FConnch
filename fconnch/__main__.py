# Entry-point script
import asyncio
import sys

from fconnch.cli import display_check_result, read_user_cli_args, no_color
from fconnch.checker import site_is_online, site_is_online_async
from pathlib import Path


def main():
    """ Run ConnChecker."""
    global verbose_mode, user_args
    user_args = read_user_cli_args()
    verbose_mode = True if user_args.verbose else False
    if user_args.no_color:
        no_color()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: No URL to check.", file=sys.stderr)
        sys.exit(1)

    if user_args.asynchronous:
        asyncio.run(_asynchronous_check(urls))
    else:
        _synchronous_check(urls)


def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: Empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found!", file=sys.stderr)

    return []


async def _asynchronous_check(urls):
    async def _check(url):
        error = ""
        try:
            response = await site_is_online_async(url, timeout=user_args.timeout)
        except Exception as e:
            response = False
            error = f"\nError: {str(e)}"
        if verbose_mode:
            display_check_result(response, url, error)
        else:
            display_check_result(response, url)

    await asyncio.gather(*(_check(url) for url in urls))


def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            response = site_is_online(url, timeout=user_args.timeout)
        except Exception as e:
            response = False
            error = f"\nError: {str(e)}"
        if verbose_mode:
            display_check_result(response, url, error)
        else:
            display_check_result(response, url)


if __name__ == "__main__":
    main()
