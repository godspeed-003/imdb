import pandas as pd

# Updated to handle CSV parsing errors gracefully.
def read_titles_from_csv(file_path):
    """Reads a CSV file and returns a list of titles."""
    try:
        df = pd.read_csv(file_path, usecols=[0], on_bad_lines='skip')  # Skip problematic lines
        return df.iloc[:, 0].dropna().tolist()  # Drop empty rows
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Example Usage (replace with your file path)
# titles = read_titles_from_csv("D:\\AI\\agent\\imdb\\titles.csv")
# print(titles)