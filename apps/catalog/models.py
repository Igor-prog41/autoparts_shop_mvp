from django.db import models
from django.templatetags.static import static
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def short_description(self):
        return ' '.join(self.description.split()[:20]) + '…'

    @property
    def stock_status(self):
        if self.stock > 0:
            return {
                "text": "In stock",
                "css": "bg-success",
            }
        return {
            "text": "Out of stock — call to check availability",
            "css": "bg-warning text-dark",
        }

    @property
    def image_or_placeholder(self):
        return self.image_url or static('images/part-placeholder.png')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, db_index=True)

    class Meta:
        unique_together = ("product", "tag")

    def __str__(self):
        return f"{self.product.title} — {self.tag.name}"

