import sys

import requests


def brute(url, wordlist):
    for word in wordlist:
        try:
            url_final = "{}/{}".format(url, word.strip())
            response = requests.get(url_final)
            code = response.status_code
            if code != 404:
                print("{} -- {}".format(url_final, code))
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as error:
            print(error)
            pass


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        url = args[1]
        wordlist = sys.argv[2]

    else:
        url = "http://www.google.com.br"
        wordlist = "wordlist.txt"

    with open(wordlist, "r") as file:
        wordlist = file.readlines()
        brute(url, wordlist)