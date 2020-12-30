from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_chart(request):
    """ Shows the shopping chart """

    return render(request, 'chart/chart.html')


def add_to_chart(request, item_id):
    """ Add quantity of the specified product to the shopping chart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    chart = request.session.get('chart', {})

    if size:
        if item_id in list(chart.keys()):
            if size in chart[item_id]['items_by_size'].keys():
                chart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {chart[item_id]["items_by_size"][size]}')
            else:
                chart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your chart')
        else:
            chart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your chart')
    else:
        if item_id in list(chart.keys()):
            chart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {chart[item_id]}')
        else:
            chart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your chart')

    request.session['chart'] = chart
    return redirect(redirect_url)


def adjust_chart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    chart = request.session.get('chart', {})

    if size:
        if quantity > 0:
            chart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {chart[item_id]["items_by_size"][size]}')
        else:
            del chart[item_id]['items_by_size'][size]
            if not chart[item_id]['items_by_size']:
                chart.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your chart')
    else:
        if quantity > 0:
            chart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {chart[item_id]}')
        else:
            chart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your chart')

    request.session['chart'] = chart
    return redirect(reverse('view_chart'))


def remove_from_chart(request, item_id):
    """Remove item from the shopping chart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        chart = request.session.get('chart', {})

        if size:
            del chart[item_id]['items_by_size'][size]
            if not chart[item_id]['items_by_size']:
                chart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your chart')
        else:
            chart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your chart')

        request.session['chart'] = chart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
