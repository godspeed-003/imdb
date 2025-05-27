# Module to manage browser automation using Selenium.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def initialize_browser():
    """Initializes and returns a Selenium WebDriver instance."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())  # Automatically installs and manages ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)
    return driver