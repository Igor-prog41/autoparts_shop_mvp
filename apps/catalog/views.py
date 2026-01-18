
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from pathlib import Path
from urllib.parse import urlencode
import markdown
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
from .models import Product


# Create your views here.

# catalog with paginator
def catalog(request):

    # --- Get all product ---
    products = Product.objects.all()

    # --- Search filtering ---
    question = request.GET.get('q', '').strip()
    if question:
        products = products.filter(title__icontains=question)

    # --- Sorting ---
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('id')

    # --- Pagination ---
    paginator = Paginator(products, 12)  # 12 product per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # --- QueryDict for passing GET parameters to the template ---
    querydict = request.GET.copy()
    querydict.pop('page', None)
    query_string = querydict.urlencode()

    context = {
        'page_obj': page_obj,
        'query_string': query_string,
        'current_sort': sort,
        'current_q': question,
    }

    return render(request, 'catalog/catalog.html', context)


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


