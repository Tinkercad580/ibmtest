from behave import given
from service.models import Product

@given("the following products")
def step_impl(context):
    for row in context.table:
        product = Product(
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            availability=row["availability"].lower() == "true"
        )
        product.create()


