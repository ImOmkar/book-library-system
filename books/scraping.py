import requests
from bs4 import BeautifulSoup


def scrape_books(category_slug):

    url = f"http://books.toscrape.com/catalogue/category/books/{category_slug}/index.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    items = soup.select("article.product_pod")

    for item in items:

        title = item.h3.a["title"]
        
        print(item.select_one(".price_color"))

        price = item.select_one(".price_color").text.replace("Â£", "")
        
        print(price)

        book_link = item.h3.a["href"]

        book_url = "http://books.toscrape.com/catalogue/" + book_link

        detail = requests.get(book_url)

        detail_soup = BeautifulSoup(detail.text, "html.parser")

        description = ""

        desc_tag = detail_soup.select_one("#product_description")

        if desc_tag:
            description = desc_tag.find_next_sibling("p").text

        books.append({
            "title": title,
            "price": price,
            "description": description
        })

    return books