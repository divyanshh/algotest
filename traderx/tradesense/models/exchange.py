from django.core.exceptions import ValidationError
from django.db import models


class Exchange(models.Model):
    """
    Exchange Model
    """

    id = models.AutoField(primary_key=True)
    exchange_name = models.CharField(max_length=300, unique=True)
    slug = models.CharField(max_length=300, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if any(ele.isupper() for ele in str(self.slug)):
            raise ValidationError("Slug cannot contain uppercase values.")
