def test_get_product(self):
    product = ProductFactory()
    product.create()
    response = self.client.get(f"/products/{product.id}")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json["name"], product.name)

def test_update_product(self):
    product = ProductFactory()
    product.create()
    new_data = {"name": "NewName", "price": 99.99}
    response = self.client.put(f"/products/{product.id}", json=new_data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json["name"], "NewName")

def test_delete_product(self):
    product = ProductFactory()
    product.create()
    response = self.client.delete(f"/products/{product.id}")
    self.assertEqual(response.status_code, 204)

def test_list_all_products(self):
    for _ in range(3):
        ProductFactory().create()
    response = self.client.get("/products")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.json), 3)

def test_list_by_name(self):
    ProductFactory(name="UniqueName").create()
    ProductFactory(name="Other").create()
    response = self.client.get("/products?name=UniqueName")
    self.assertEqual(len(response.json), 1)
    self.assertEqual(response.json[0]["name"], "UniqueName")

def test_list_by_category(self):
    ProductFactory(category="Gadgets").create()
    ProductFactory(category="Other").create()
    response = self.client.get("/products?category=Gadgets")
    self.assertEqual(len(response.json), 1)
    self.assertEqual(response.json[0]["category"], "Gadgets")

def test_list_by_availability(self):
    ProductFactory(availability=True).create()
    ProductFactory(availability=False).create()
    response = self.client.get("/products?availability=true")
    self.assertEqual(len(response.json), 1)
    self.assertTrue(response.json[0]["availability"])

