from src.scraper import SimpleWebScraper


def main():
    url = "https://automatetheboringstuff.com/2e/"

    scraper = SimpleWebScraper(url)
    result = scraper.scrape()

    if result is None:
        print("Failed to scrape the webpage.")
        return

    print("=" * 60)
    print("WEB SCRAPING RESULTS")
    print("=" * 60)

    print(f"\nBook Title: {result['book_title']}")

    print("\nChapter Titles:")
    if result["chapter_titles"]:
        for index, title in enumerate(result["chapter_titles"], start=1):
            print(f"{index}. {title}")
    else:
        print("No chapter titles found.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()