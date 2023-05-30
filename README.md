**Web Form Automation**

This project automates the process of filling a web form using data from a CSV file.

**Prerequisites**:

- Python 3.x
- Selenium library
- Web driver for your browser (e.g., ChromeDriver for Chrome)

**Installation**:

1. Clone the repository:
   git clone https://github.com/your-username/web-form-automation.git

2. Install the required dependencies:
   pip install selenium

3. Download the appropriate web driver for your browser and make sure it's in your system's PATH.

**Configuration**:

1. Open config.py and set the following variables:
   - url: The URL of the web form you want to automate.
   - csv_file_path: The path to your CSV file containing the data.
   - field_mappings: A dictionary mapping field names from the CSV file to the corresponding CSS selectors of the input fields on the web form.

Example:
```python
field_mappings = {
    'Name': '#inputField1',
    'Email': '#inputField2',
    'Message': '#inputField3'
}
```

**Usage**:

Run the script by executing the following command:
python fill_web_form.py

The script will automatically open a web browser, load the specified web form, and fill it with the data from your CSV file.

**Contributing**:

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

**License**:

This project is licensed under the MIT License. 
