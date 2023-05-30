from selenium import webdriver
import csv
from time import sleep
from config import url, csv_file_path, field_mappings

# Load the web driver (e.g., ChromeDriver for Chrome)
driver = webdriver.Chrome()

# Load the web form
driver.get(url)

# Read data from CSV file
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Fill the form fields using the data from the CSV file
        for field_name, selector in field_mappings.items():
            value = row[field_name]
            input_field = driver.find_element_by_css_selector(selector)
            input_field.clear()
            input_field.send_keys(value)

        # Submit the form (if needed)
        submit_button = driver.find_element_by_css_selector('#submit_button')
        submit_button.click()

        # Add some delay before processing the next entry
        sleep(2)

# Close the browser
driver.quit()
