# app.py

from scraper import WebScraper

def display_titles(titles):
    if titles:
        print("\nScraped Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title}")
    else:
        print("No titles found on the page.")

def main():
    print("Welcome to the Web Scraper App!")

    while True:
        url = input("Enter the URL to scrape (or 'exit' to quit): ")

        if url.lower() == "exit":
            print("Goodbye!")
            break

        scraper = WebScraper(url)
        titles = scraper.scrape_titles()
        display_titles(titles)

if __name__ == "__main__":
    main()
