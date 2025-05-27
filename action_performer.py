# Module to perform actions like adding titles to the "Watched" list and clicking the "Watched" button.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def add_to_watched_list(driver, title_data):
    """Marks the given title as watched on IMDb."""
    try:
        # Navigate to the title's URL if provided
        if isinstance(title_data, dict) and 'url' in title_data:
            driver.get(title_data['url'])
        else:
            print(f"Error: No URL provided for title {title_data}")
            return False

        # Wait for the "Mark as watched" button to be present
        wait = WebDriverWait(driver, 10)
        watched_button = wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                "button[data-testid^='watched-button']"
            ))
        )

        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", watched_button)
        time.sleep(5)  # Wait for any animations to complete

        # Click the button
        watched_button.click()
        time.sleep(5)  # Wait for the action to complete

        # Log success
        title = title_data['title'] if 'title' in title_data else "Unknown Title"
        print(f"Successfully marked '{title}' as watched.")
        return True

    except Exception as e:
        print(f"Error marking title as watched: {e}")
        return False