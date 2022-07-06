import aiohttp
import asyncio

from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url, timeout=3):
    """ Return True if the target URL in online.
    Raise an exception otherwise. """
    error = Exception("unknown error!")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            # Next two lines will print HTTP status code of the request
            response_code = connection.getresponse().status
            return response_code
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

async def site_is_online_async(url, timeout=3):
    """Return True if the target URL is online.
    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                # Old method, without status code
                # await session.head(target_url, timeout=timeout)
                async with session.head(target_url, timeout=timeout) as resp:
                    response = resp.status
                return response
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error
