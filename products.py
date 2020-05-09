import json
products = [
        {
            "id": 1,
            "name": 'Lays',
            "price": 100,
            "stock": 500
        },
        {
            "id": 2,
            "name": 'Twix',
            "price": 35,
            "stock": 10
        },
        {
            "id": 3,
            "name": 'Snickers',
            "price": 42,
            "stock": 53
        },
        {
            "id": 4,
            "name": 'Coca Cola',
            "price": 80,
            "stock": 1399
        },
        {
            "id": 5,
            "name": 'Fanta',
            "price": 75,
            "stock": 999
        },
        {
            "id": 6,
            "name": 'Sprite',
            "price": 78,
            "stock": 1200
        },
        {
            "id": 7,
            "name": 'Mamba',
            "price": 29,
            "stock": 2000
        },
        {
            "id": 8,
            "name": 'Dirol',
            "price": 35,
            "stock": 233
        },
        {
            "id": 9,
            "name": 'Pepsi',
            "price": 55,
            "stock": 500
        },
        {
            "id": 10,
            "name": 'Russian potato',
            "price": 49,
            "stock": 845
        }
]
with open("products.json", "w") as write_file:
    json.dump(products, write_file, indent=3)