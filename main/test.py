from django.test import TestCase, Client
from .models import Product   # <--- ubah

class ProductTest(TestCase):  # <--- ubah nama kelas test juga biar konsisten
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/this_page_does_not_exist/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Sepatu Bola",
            price=500000,
            description="Sepatu bola kualitas premium",
            thumbnail="http://example.com/sepatu.jpg",
            category="Olahraga",
            is_featured=True
        )
        self.assertEqual(product.name, "Sepatu Bola")
        self.assertEqual(product.price, 500000)
        self.assertEqual(product.category, "Olahraga")
        self.assertTrue(product.is_featured)

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Bola Basket",
            price=200000,
            description="Bola basket standar FIBA",
            category="Olahraga"
        )
        self.assertFalse(product.is_featured)   # default False
        self.assertIsNone(product.thumbnail)    # karena null=True
        self.assertEqual(str(product), "Bola Basket")