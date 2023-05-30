## Adding sample data to a google form

import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the CSV file
csv_file_path = 'data.csv'
data = []
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Initialize the web driver
driver = webdriver.Chrome()  # Replace with the appropriate web driver for your browser

# Open the Google Form
url = 'https://docs.google.com/forms/d/e/your_form_id/viewform'  # Replace with your Google Form URL
driver.get(url)

# Wait for the form to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/span/div/div[1]/label/div/div[2]/div/div[3]/div/div/div[1]/input')))

# Fill the form with data from the CSV file
for row in data:
    name_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/span/div/div[1]/label/div/div[2]/div/div[3]/div/div/div[1]/input')
    name_input.send_keys(row['Name'])
    
    email_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/div[3]/div/div/div[1]/input')
    email_input.send_keys(row['Email'])
    
    message_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/span/div/div[1]/label/div/div[2]/div/div[3]/div/div/div[1]/input')
    message_input.send_keys(row['Message'])
    
    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    submit_button.click()
    
    # Wait for the form submission to complete
    sleep(2)

# Close the web driver
driver.quit()
