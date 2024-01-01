from bs4 import BeautifulSoup
import requests
import uuid

from models.products_model import Product


def parser(url: str) -> list[Product]:
    products_list = []

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        products = soup.find_all(
            "div", class_="product-snippet_ProductSnippet__content__1d372b"
        )
        for product in products:
            product_id = str(uuid.uuid4())

            name = product.find(
                "div", class_="product-snippet_ProductSnippet__name__1d372b"
            ).text.strip()
            price = product.find(
                "div", class_="snow-price_SnowPrice__mainM__1cmks6"
            ).text.strip()
            img = product.find("img", class_="gallery_Gallery__image__1gsooe").get(
                "data-src"
            )
            products_list.append(
                Product(product_id=product_id, name=name, price=price, img=img)
            )

    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    return products_list


if __name__ == "__main__":
    print(
        parser(
            url="https://aliexpress.ru/store/1102958512?g=y&page=1&spm=a2g2w.detail.0.1.244f778bsfyGft"
        )
    )
