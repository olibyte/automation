# handling errors and status codes

# TODO: import the request, error, and status modules
import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    url = "http://no-such-server.org"      # will generate a URLError
    # url = "http://httpbin.org/status/404"  # will generate an HTTPError
    # url = "http://httpbin.org/html"         # should work with no errors

    # TODO: use exception handling to attempt the URL access
    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        if (result.getcode() == HTTPStatus.OK):
            print(result.read().decode('utf-8'))
    except HTTPError as err:
        print("Error {0}".format(err.code))
    except URLError as err:
        print("Yeah that server is defunct. {0}".format(err.reason))

if __name__ == "__main__":
    main()