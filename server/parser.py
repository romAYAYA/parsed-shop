from bs4 import BeautifulSoup
import requests


def parser(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    products = soup.find_all(
        "div", class_="product-snippet_ProductSnippet__content__1d372b"
    )
    for product in products:
        name = product.find('div', class_='product-snippet_ProductSnippet__name__1d372b').text.strip()
        price = product.find('div', class_='snow-price_SnowPrice__mainM__1cmks6').text.strip()
        img = product.find("img", class_="gallery_Gallery__image__1gsooe").get("data-src")
        print(img)
        print(name)
        print(price)


# soup = BeautifulSoup(page.text, "html.parser")
#
# filtered_images = soup.find_all("img", {"data-idx": "0"})
# print(page.status_code)
#
# for source_tag in filtered_images:
#     src_value = source_tag.get("data-src")
#     print(src_value)


if __name__ == "__main__":
    parser(
        url="https://aliexpress.ru/store/1102958512?g=y&page=1&spm=a2g2w.detail.0.1.244f778bsfyGft"
    )
