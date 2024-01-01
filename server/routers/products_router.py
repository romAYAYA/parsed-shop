from fastapi import APIRouter

from parser import parser

router = APIRouter()


@router.get("/products")
def get_products():
    url = "https://aliexpress.ru/store/1102958512?g=y&page=1&spm=a2g2w.detail.0.1.244f778bsfyGft"

    products = parser(url)

    return products
