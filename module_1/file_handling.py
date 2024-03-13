import os

def read_urls_from_file(file_path):
    """Read URLs from a text file and return a list."""
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        return [url.strip() for url in urls]
    except FileNotFoundError:
        print("File not found.")
        return []

def save_content_to_file(file_path, url, content):
    """Save the content to a text file."""
    try:
        with open(file_path, 'a') as output_file:
            output_file.write(f"URL: {url}\n")
            output_file.write(content)
            output_file.write("\n\n")
        print("Content saved to file.")
    except IOError:
        print("Error writing to file.")
