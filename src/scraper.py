import requests
from bs4 import BeautifulSoup


class SimpleWebScraper:
    """A simple web scraper using requests and BeautifulSoup."""

    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        """Download a webpage and return its HTML content."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
        }

        try:
            response = requests.get(
                self.url,
                headers=headers,
                timeout=15
            )
            response.raise_for_status()
            return response.text

        except requests.RequestException as error:
            print(f"Error fetching webpage: {error}")
            return None

    def get_book_title(self, soup):
        """Extract the book title from the webpage."""
        title = soup.find("title")

        if title:
            return title.get_text(strip=True)

        return "Title not found"

    def get_chapter_titles(self, soup):
        """Extract chapter titles from the table of contents."""
        chapters = []

        for link in soup.find_all("a"):
            text = link.get_text(" ", strip=True)

            if text.startswith("Chapter "):
                chapters.append(text)

        return chapters

    def scrape(self):
        """Fetch the webpage and extract book and chapter titles."""
        html = self.fetch_page()

        if html is None:
            return None

        soup = BeautifulSoup(html, "html.parser")

        return {
            "book_title": self.get_book_title(soup),
            "chapter_titles": self.get_chapter_titles(soup)
        }