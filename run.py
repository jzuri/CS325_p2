from Modules import file_handling, data_processing

def main():
    # Reads URLs from the text file
    urls = file_handling.read_urls_from_file('Data/raw/article_urls.txt')

    # Scrapes content/text for each URL
    for url in urls:
        article_content = data_processing.scrape_article(url)
        if article_content:
            # Save the content to a text file
            file_handling.save_content_to_file('Data/processed/articles.txt', url, article_content)

if __name__ == "__main__":
    main()
