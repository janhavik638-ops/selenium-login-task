from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome browser
driver = webdriver.Chrome()

# Open sample website
driver.get("https://the-internet.herokuapp.com/login")

# Fill username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click login button
driver.find_element(By.TAG_NAME, "button").click()

# Keep browser open until manually closed
input("Press Enter to close the browser...")

# Close browser after pressing Enter
driver.quit()