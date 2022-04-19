from flask import Flask, jsonify

app = Flask(__name__)

product_details = [{"product_id": "0",
                    "name": "Blue T-Shirt",
                    "category": "Clothing",
                    "price": "400",
                    "brand": "Denim",
                    "rating": "4.2"},
                   {"product_id": "1",
                    "name": "OnePlus 6T",
                    "category": "Smartphone",
                    "price": "32990",
                    "brand": "Redmi",
                    "rating": "4.5"},
                   {
                   "product_id": "2",
                   "name": "Smart Cam",
                   "category": "Clothing",
                   "price": "2600",
                   "brand": "Realme",
                   "rating": "3.9"},
                   {"product_id": "3",
                    "name": "Banana Chips",
                    "category": "Food",
                    "price": "550",
                    "brand": "Calicut Kerala",
                    "rating": "4.7"}
                   ]


@app.route('/')
def index():
    """Displays text in the webpage."""
    return "<h3>Welcome to Ecommerce Page</h3>"


@app.route("/product_details", methods = ['GET'])
def get():
    """Displaying product details in the webpage."""
    return jsonify({'product_details': product_details})


@app.route("/product_details/<int:product_id>", methods=['GET'])
def get_id(product_id):
    """Displays single product details in the webpage by taking id.
        Parameters:
            product_id (int): An integer
        Returns:
            json object: contains product details of a given id
    """
    return jsonify({'product_details': product_details[product_id]})


@app.route("/product_details", methods=['POST'])
def create():
    """Creates a product and added ino the dictionary and showing the product details in the webpage."""
    detail = {"product_id": "4",
              "name": "Black Jeans",
              "category": "Clothing",
              "price": "800",
              "brand": "Puma",
              "rating": "4.3"}
    product_details.append(detail)
    return jsonify({'Created': detail})


@app.route("/product_details/<int:product_id>", methods=['PUT'])
def detail_update(product_id):
    """Update price of the product by taking id of the product and displays that product in the webpage.
        Parameters:
            product_id (int): An integer
        Returns:
            json object: display the updated product details
    """
    product_details[product_id]["price"] = "200"
    return jsonify({'product_detail': product_details[product_id]})


@app.route("/product_details/<int:product_id>", methods=['DELETE'])
def delete(product_id):
    """Delete the product in the product details dictionary by taking id of the product
       and displays the text in the webpage.
        Parameters:
            product_id (int): An integer
        Returns:
            str: text
    """
    product_details.remove(product_details[product_id])
    return jsonify({'result': "Successfully Deleted"})


app.run(debug=True)
