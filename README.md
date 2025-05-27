# IMDb Watchlist Agent

An automated agent that helps manage and analyze IMDb watchlists using AI-powered title matching and browser automation.

## Features

- Automated title matching using Google's Gemini AI
- Browser automation for IMDb interactions using Selenium
- CSV report generation
- Environment-based configuration
- Command-line interface for easy interaction

## Prerequisites

- Python 3.8 or higher
- Google Cloud Project with Gemini API enabled
- Chrome or Chromium browser installed
- IMDb account (for watchlist management)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Prepare your list of titles in a `titles.csv` file (one title per line)
2. Run the main script:
   ```bash
   python watch.py
   ```
3. Follow the on-screen instructions to log in to your IMDb account when prompted

The script will:
- Process titles from `titles.csv`
- Use Gemini AI to find the best matching IMDb titles
- Generate a report in `report.csv` with the results
- (Future) Store any screenshots or images in the `images` directory

## Project Structure

- `watch.py` - Main entry point and orchestration
- `gemini_api.py` - Integration with Google's Gemini AI for title matching
- `browser_controller.py` - Selenium-based browser automation
- `title_matcher.py` - Title matching utilities
- `report_generator.py` - CSV report generation
- `titles.csv` - Input file containing titles to process
- `report.csv` - Output file with processing results
- `images/` - Directory for storing screenshots (future use)

## Configuration

You can customize the following environment variables in your `.env` file:

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `ANONYMIZED_TELEMETRY`: Set to "false" to disable telemetry (default: false)


## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license here]

## Acknowledgments

- Google Gemini API
- IMDb
- Selenium WebDriver
