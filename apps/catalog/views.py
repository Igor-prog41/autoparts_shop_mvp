
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from pathlib import Path
import markdown
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
from .models import Product


# Create your views here.

# catalog with paginator
def catalog(request):

    page_number = request.GET.get('page')
    question = request.GET.get('q')
    products = Product.objects.all()

    if question:
        products = products.filter(title__icontains=question)

    products = products.order_by("id")
    paginator = Paginator(products, 12)  # 12 products per page
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/catalog.html', {
        'page_obj': page_obj,
        'products': page_obj.object_list,
    })


def about(request):
    readme_html = "<p>README.md not found.</p>"

    readme_path = os.path.join(settings.BASE_DIR, "README.md")

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            readme_html = markdown.markdown(
                f.read(),
                extensions=["extra", "tables", "toc"]
            )

    return render(
        request,
        "catalog/about.html",
        {"readme_content": readme_html}
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'catalog/product_detail.html', {
        'product': product
    })


