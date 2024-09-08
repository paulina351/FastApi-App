from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4


app = FastAPI()


class Product(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    availability: bool = False
    completed: bool = False

products = []

@app.post("/products/", response_model=Product)
def create_task(product: Product):
    product.id = uuid4()
    products.append(product)
    return product


@app.get("/products/", response_model=List[Product])
def read_products():
    return products


@app.get("/products/{product_id}", response_model=Product)
def read_product(task_id: UUID):
    for product in products:
        if product.id == product.id:
            return product
    return HTTPException(status_code=404, detail="Task not found")

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, product_update: Product):
    for idx, product in enumerate(products):
        if products.id == product.id:
            updated_product = product.copy(update=product_update.dict(exclude_unset=True))
            products[idx] = updated_product
            return updated_product
    return HTTPException(status_code=404, detail="Task not found")


@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id):
    for idx, product in enumerate(products):
        if product.id == product.id:
            return products.pop(idx)
    return HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)