# Module to handle search strategies, including CAPTCHA detection and Google search fallback.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def collect_search_results(driver):
    """Collect and return search results from the current page."""
    try:
        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ipc-metadata-list-summary-item"))
        )

        # Get all search result items
        results = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")

        # Extract title and URL information
        search_results = []
        for result in results[:5]:  # Limit to first 5 results
            try:
                title_elem = result.find_element(By.CSS_SELECTOR, "a.ipc-metadata-list-summary-item__t")
                title = title_elem.text.strip()
                url = title_elem.get_attribute('href')

                if title and url:
                    search_results.append({
                        'title': title,
                        'url': url
                    })
            except Exception as e:
                print(f"Error extracting result: {e}")
                continue

        return search_results

    except Exception as e:
        print(f"Error collecting search results: {e}")
        return []

def search_imdb(driver, title):
    """Searches IMDb for the given title and returns search results."""
    try:
        driver.get("https://www.imdb.com/")

        # Wait for search box and enter title
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "suggestion-search"))
        )
        search_box.clear()
        search_box.send_keys(title)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for results to load

        # Collect and return search results
        return collect_search_results(driver)

    except Exception as e:
        print(f"Error during IMDb search: {e}")
        return []

def handle_captcha_and_google_search(driver, title):
    """Handles CAPTCHA by switching to Google search."""
    try:
        if "captcha" in driver.page_source.lower():
            print("CAPTCHA detected. Switching to Google search.")
            driver.get(f"https://www.google.com/search?q=site:imdb.com+{title}")
            time.sleep(2)
            
            # Look for IMDb links in Google results
            imdb_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='imdb.com/title']")
            if imdb_links:
                # Click the first IMDb link
                imdb_links[0].click()
                time.sleep(2)
                return collect_search_results(driver)
                
        return []
        
    except Exception as e:
        print(f"Error during CAPTCHA handling: {e}")
        return []