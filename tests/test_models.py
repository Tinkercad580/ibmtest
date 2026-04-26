def test_read_product(self):
    product = ProductFactory()
    product.create()
    found = Product.find(product.id)
    self.assertIsNotNone(found)
    self.assertEqual(found.id, product.id)

def test_update_product(self):
    product = ProductFactory()
    product.create()
    product.name = "Updated Name"
    product.update()
    updated = Product.find(product.id)
    self.assertEqual(updated.name, "Updated Name")

def test_delete_product(self):
    product = ProductFactory()
    product.create()
    product.delete()
    deleted = Product.find(product.id)
    self.assertIsNone(deleted)

def test_list_all_products(self):
    for _ in range(3):
        ProductFactory().create()
    all_products = Product.all()
    self.assertEqual(len(all_products), 3)

def test_find_by_name(self):
    ProductFactory(name="TestItem").create()
    ProductFactory(name="Other").create()
    found = Product.find_by_name("TestItem")
    self.assertEqual(len(found), 1)
    self.assertEqual(found[0].name, "TestItem")

def test_find_by_category(self):
    ProductFactory(category="Electronics").create()
    ProductFactory(category="Books").create()
    found = Product.find_by_category("Electronics")
    self.assertEqual(len(found), 1)
    self.assertEqual(found[0].category, "Electronics")


def test_find_by_availability(self):
    ProductFactory(availability=True).create()
    ProductFactory(availability=False).create()
    available = Product.find_by_availability(True)
    self.assertEqual(len(available), 1)
    self.assertTrue(available[0].availability)
