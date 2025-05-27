# **Project Requirements Document: IMWatch - IMDb Watchlist Automation Tool**

The following table outlines the detailed functional requirements of the IMWatch automation tool.

| Requirement ID | Description | User Story | Expected Behavior/Outcome |
|----------------|-------------|------------|---------------------------|
| FR001 | Environment Setup | As a user, I want the system to create and use a dedicated virtual environment named "imwatch" for the application. | The system should automatically create a Python virtual environment named "imwatch" and install all necessary dependencies within it. |
| FR002 | Browser Automation | As a user, I want the tool to automate actions in my web browser to interact with IMDb. | The system should be able to control Chrome (initially) and eventually other browsers to navigate to IMDb and perform required actions. |
| FR003 | CSV Title Import | As a user, I want to provide a list of movie/show titles in a CSV file that the tool can process. | The system should read and parse a CSV file containing a single column of movie/show titles. |
| FR004 | Captcha Handling | As a user, I want the tool to detect and respond appropriately when faced with a CAPTCHA. | When a CAPTCHA is detected, the system should switch to Google search using "site:imdb [title]" to find the correct IMDb page. |
| FR005 | Title Search | As a user, I want the tool to find the correct IMDb page for each title in my list. | The system should navigate to the IMDb search or use Google search to locate the correct page for each title. |
| FR006 | Multiple Results Handling | As a user, I want the tool to intelligently select the most relevant result when multiple matches are found. | The system should use LLM (Gemini Flash 2.0) to determine which search result is most likely the intended title. |
| FR007 | Adding to "Watched" List | As a user, I want titles to be added to my "Watched" list on IMDb. | The system should find and click the option to add each title to the "Watched" list on IMDb. |
| FR008 | Marking as Watched | As a user, I want the system to click the "Mark as watched" button for each title. | The system should locate and click the "Mark as watched" button on each title's page. |
| FR009 | Cross-Browser Compatibility | As a user, I want the tool to work with multiple browsers, not just Chrome. | The system should be designed to work with various browsers, starting with Chrome for testing and extending to others. |
| FR010 | Error Handling | As a user, I want the tool to gracefully handle errors such as titles not found or network issues. | The system should implement robust error handling to prevent crashes and provide meaningful error messages. |
| FR011 | Asynchronous Processing | As a user, I want the tool to process multiple titles efficiently using asynchronous operations. | The system should implement asyncio or similar technology to process multiple titles concurrently where applicable. |
| FR012 | Detailed Reporting | As a user, I want a comprehensive report of which actions were successful for each title. | The system should generate a report showing: titles successfully added to the "Watched" list, titles marked as watched, titles where both actions succeeded, titles where neither action succeeded, and overall statistics including percentages and counts. |
| FR013 | Progress Tracking | As a user, I want to see the progress of the automation as it runs. | The system should display real-time progress information including current title being processed and completion percentage. |
| FR014 | Session Persistence | As a user, I want the tool to work with my already logged-in browser session. | The system should be able to use an existing Chrome session where the user is already logged into IMDb. |
| FR015 | Retry Mechanism | As a user, I want the tool to retry failed operations a reasonable number of times. | The system should implement a retry mechanism for failed operations with appropriate backoff strategy. |

## Non-Functional Requirements

| Requirement ID | Description | Expected Behavior/Outcome |
|----------------|-------------|---------------------------|
| NFR001 | Performance | The tool should process at least 10 titles per minute (depending on network conditions). |
| NFR002 | Reliability | The tool should successfully process at least 90% of valid titles provided. |
| NFR003 | Usability | The tool should be easy to run with minimal setup beyond the virtual environment creation. |
| NFR004 | Maintainability | The code should be well-documented and modular to facilitate future enhancements. |
| NFR005 | Security | The tool should not store or transmit any user credentials. |

## Technical Specifications

### Technology Stack
- Python 3.8+
- Selenium WebDriver
- Asyncio (for concurrent processing)
- Pandas (for CSV handling)
- Gemini Flash 2.0 API (for intelligent title matching)
- ChromeDriver (and other browser drivers eventually)

### Architecture Components
1. **Title Importer**: Reads and validates the CSV input file
2. **Browser Controller**: Manages browser automation
3. **Search Strategist**: Determines whether to use direct IMDb search or Google search
4. **Title Matcher**: Uses LLM to identify the correct title among search results
5. **Action Performer**: Executes the "Add to Watched list" and "Mark as watched" actions
6. **Report Generator**: Creates detailed success/failure reports

### Data Flow
1. User provides CSV with titles and runs the tool
2. Tool reads titles from CSV
3. For each title:
   - Tool searches on IMDb
   - If CAPTCHA detected, switches to Google search
   - LLM identifies correct title from results
   - Tool attempts to add to "Watched" list
   - Tool attempts to mark as watched
   - Results are recorded
4. Comprehensive report is generated and displayed to user

## Future Enhancements (v2.0)
- GUI for easier operation
- Scheduling capability for regular runs
- Ability to process other IMDb actions (ratings, reviews, etc.)
- Export/import of successful/failed titles for batch processing