
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.conf import settings
from pathlib import Path
import markdown

from .models import Product


# Create your views here.

# catalog with paginator
def catalog(request):
    products = Product.objects.all().order_by('id')

    paginator = Paginator(products, 12)  # 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/catalog.html', {
        'page_obj': page_obj,
        'products': page_obj.object_list,
    })


def about(request):
    readme_path = Path(settings.BASE_DIR) / "README.md"

    if readme_path.exists():
        md_text = readme_path.read_text(encoding="utf-8")
        html_content = markdown.markdown(
            md_text,
            extensions=["fenced_code", "tables"]
        )
    else:
        html_content = "<p>README.md not found.</p>"

    return render(request, 'catalog/about.html', {
        "content": html_content
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'catalog/product_detail.html', {
        'product': product
    })


