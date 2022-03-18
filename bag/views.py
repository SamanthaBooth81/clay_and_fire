"""Shopping Bag Views"""

from django.shortcuts import render, redirect


def view_bag(request):
    """View to return the shopping bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add to Bag View"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # The below checks if there is a bag variable in
    # the session and if not, creates one.
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
