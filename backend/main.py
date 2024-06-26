from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from client import get_db_connection
from typing import List

app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 必要に応じて許可するオリジンを設定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 商品モデル
class Product(BaseModel):
    product_code: int

class ProductResponse(BaseModel):
    product_code: int
    product_name: str
    price: int

@app.post("/get_product/", response_model=ProductResponse)
def get_product(product: Product):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT product_code, product_name, price FROM products WHERE product_code = %s", (product.product_code,))
    product_data = cursor.fetchone()

    cursor.close()
    connection.close()

    if product_data:
        return product_data
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.get("/products/", response_model=List[ProductResponse])
def get_all_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT product_code, product_name, price FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products

@app.get("/products/{product_code}", response_model=ProductResponse)
def get_product_by_code(product_code: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT product_code, product_name, price FROM products WHERE product_code = %s", (product_code,))
    product_data = cursor.fetchone()

    cursor.close()
    connection.close()

    if product_data:
        return product_data
    else:
        raise HTTPException(status_code=404, detail="Product not found")