import requests
from bs4 import BeautifulSoup


BASE_URL = "http://books.toscrape.com/"


def scrape_books(category_slug):

    books_data = []

    url = f"{BASE_URL}catalogue/category/books/{category_slug}/index.html"

    while url:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select(".product_pod")

        for book in books:

            title = book.h3.a["title"]

            price = book.select_one(".price_color").text.replace("Â£", "")

            detail_url = BASE_URL + "catalogue/" + book.h3.a["href"].replace("../", "")

            detail_response = requests.get(detail_url)
            detail_soup = BeautifulSoup(detail_response.text, "html.parser")

            # Description
            description = ""
            desc_tag = detail_soup.find("div", id="product_description")

            if desc_tag:
                description = desc_tag.find_next_sibling("p").text.strip()

            # Image
            image_tag = detail_soup.find("img")
            image_url = BASE_URL + image_tag["src"].replace("../../", "")

            books_data.append({
                "title": title,
                "price": price,
                "description": description,
                "image_url": image_url
            })

        # Pagination
        next_button = soup.select_one(".next")

        if next_button:
            next_page = next_button.a["href"]
            url = url.rsplit("/", 1)[0] + "/" + next_page
        else:
            url = None

    return books_data