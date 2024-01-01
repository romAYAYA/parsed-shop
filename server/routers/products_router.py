from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from parser import parser

router = APIRouter()


@router.get("/api/products", response_class=JSONResponse)
def get_products():
    url = "https://aliexpress.ru/store/1102958512?g=y&page=1&spm=a2g2w.detail.0.1.244f778bsfyGft"

    try:
        products = parser(url)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
