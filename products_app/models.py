from django.db import models
import uuid


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.category_name

class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=500)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_content = models.TextField()
    product_price = models.IntegerField()
    remaining_amount = models.IntegerField()
    addition_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product_name