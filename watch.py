from browser_use import Agent
from gemini_api import configure_gemini, match_title_with_gemini
from dotenv import load_dotenv
import asyncio
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Disable telemetry (optional)
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Ensure the images folder exists
IMAGES_FOLDER = "images"
os.makedirs(IMAGES_FOLDER, exist_ok=True)

def show_parts(response):
    """Helper for rendering a GenerateContentResponse object."""
    parts = response.candidates[0].content.parts
    if parts is None:
        finish_reason = response.candidates[0].finish_reason
        print(f'{finish_reason=}')
        return

    for part in parts:
        if part.text:
            print(part.text)
        elif part.executable_code:
            print(f'Python code:\n{part.executable_code.code}')

async def process_titles(titles):
    # Initialize LangChain's Gemini model
    llm = configure_gemini()
    logs = []
    
    # Combine login, verification, and title processing into a single task
    combined_task = f"""
    Task: IMDb Login, Verification, and Title Processing
    Steps:
    1. Navigate to https://www.imdb.com
    2. Wait for the user to log in manually
    3. Verify that the user is logged in by checking the IMDb homepage (e.g., username "Vedant" in the top navigation bar)
    4. Process the following titles:
    {', '.join(titles)}
        a. Verify we are on IMDb (go to https://www.imdb.com if not)
        b. Locate and click the search box at the top of the page
        c. Enter the title and press Enter to search
        d. From the results, click the most relevant match for the title
        e. Scroll down by a meaningful amount (e.g., 500 pixels) to locate the "Mark as Watched" button
        f. If the "Watched" button is already present, skip the next step
        g. If not already watched, click the "Mark as Watched" button
        h. Scroll back up by a meaningful amount (e.g., 500 pixels) to the search bar for the next title
    """
    
    # Initialize single persistent agent instance
    agent = Agent(
        task=combined_task,
        llm=llm
    )
    
    try:
        print("\nPlease log in to your IMDb account in the browser window.")
        print("The agent will handle login verification and title processing in one session.")
        
        # Run the combined task
        result = await agent.run()
        
        # Process the result
        if isinstance(result, dict):
            success = result.get('success', False)
            message = result.get('text', 'Unknown result')
            if success:
                logs.append(["All Titles", "Success", message])
                print(f"Successfully completed all tasks: {message}")
            else:
                logs.append(["All Titles", "Failed", message])
                print(f"Failed to complete tasks: {message}")
        else:
            logs.append(["All Titles", "Failed", "Invalid result format"])
            print("Failed to complete tasks: Invalid result format")
            
    except Exception as e:
        print(f"Error during task execution: {e}")
        logs.append(["All Titles", "Error", str(e)])
    
    return logs

async def main():
    print("IMWatch Automation Tool - Starting...")

    # Step 1: Import titles from CSV
    from title_importer import read_titles_from_csv
    titles = read_titles_from_csv("titles.csv")
    print(f"Imported {len(titles)} titles.")

    # Limit to processing the top 10 titles
    titles = titles[:10]

    # Step 2: Process titles
    logs = await process_titles(titles)

    # Step 3: Generate report
    from report_generator import generate_report
    generate_report(logs)  # Ensure logs are passed to the report generator

    print("IMWatch Automation Tool - Completed.")

# Example usage of match_title_with_gemini
target_title = "The Perfect Year"
search_results = ["The Perfect Year (2023)", "The Perfect Pear (2022)", "Perfect Year (2021)"]

gemini_model = configure_gemini()
matched_title = match_title_with_gemini(gemini_model, target_title, search_results)
print(f"Matched Title: {matched_title}")

# Run the main function
asyncio.run(main())