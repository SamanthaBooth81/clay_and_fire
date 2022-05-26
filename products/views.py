"""Products app views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Products, Category, Review
from .forms import AddProductForm, ReviewForm


def all_products(request):
    """View to show all products for  sale and sort/filter items"""
    # Code Institutes Boutique Ado project code
    # used to create search and sort functions
    products = Products.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Products, pk=product_id)

    reviews = Review.objects.filter(product_id=product.id, status=True)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """Add a product to the store - Super User Only"""
    if not request.user.is_superuser:
        # Redirect back to homepage if not a superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'{product.name} Successfully Added!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Opps! Please ensure the form is valid.')
    else:
        form = AddProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product on the store - Super User Only"""
    if not request.user.is_superuser:
        # Redirect back to homepage if not a superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{product.name} successfully updated!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        form = AddProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        # Redirect back to homepage if not a superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, f'{product.name} deleted!')
        return redirect(reverse('products'))

    return render(request, 'products/confirm_delete.html')


@login_required
def submit_review(request, product_id):
    """Sumbit a product review"""
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = Review()
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.product = product
            data.user_id = request.user.id
            data.save()
            messages.success(
                request, 'Thank you! Your review has been submitted.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, "Sorry your review could not be submitted.")
            return redirect(reverse('product_details', args=[product.id]))
    else:
        form = ReviewForm()

    template = 'products/product_details.html'

    return render(request, template)
