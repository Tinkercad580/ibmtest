import factory
from tests.models import Product  # update this import

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    category = factory.Faker('word')
    availability = factory.Faker('boolean')
