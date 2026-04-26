@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id {product_id} not found")
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)
    data = request.get_json()
    product.deserialize(data)
    product.update()
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if product:
        product.delete()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("availability")

    products = Product.all()

    if name:
        products = [p for p in products if p.name == name]
    if category:
        products = [p for p in products if p.category == category]
    if availability is not None:
        avail_bool = availability.lower() == "true"
        products = [p for p in products if p.availability == avail_bool]

    return jsonify([p.serialize() for p in products]), 200
