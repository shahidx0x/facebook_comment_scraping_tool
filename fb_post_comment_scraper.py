from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Set up the Chrome WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://www.facebook.com')

# Get the email and password input from the user
email = input("Enter your email: ")
password = input("Enter your password: ")

# Find the email and password input fields and login button
email_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')

# Enter email and password
email_input.send_keys(email)
password_input.send_keys(password)

# Click the login button
login_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Get the Facebook post URL input from the user
post_url = input("Enter the URL of the Facebook post: ")
driver.get(post_url)

# Get the XPath input from the user
xpath_input = input("Enter the XPath of the element you want to retrieve text from: ")

try:
    # Wait for the element specified by XPath to be present
    wait = WebDriverWait(driver, 40)
    ul_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_input)))

    # Get the text from the <ul> element
    ul_text = ul_element.text

    # Save the text in a file
    with open("comment.txt", "w", encoding="utf-8") as file:
        file.write(ul_text)

    print("The text has been saved in comment.txt")

except NoSuchElementException as e:
    print("The specified element was not found.")
    print(e)

finally:
    # Close the WebDriver
    driver.quit()
