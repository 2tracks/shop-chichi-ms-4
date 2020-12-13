from django.shortcuts import render, redirect, reverse, HttpResponse


def view_chart(request):
    """ Shows the shopping chart """

    return render(request, 'chart/chart.html')


def add_to_chart(request, item_id):
    """ Add quantity of the specified product to the shopping chart """

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
            else:
                chart[item_id]['items_by_size'][size] = quantity
        else:
            chart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(chart.keys()):
            chart[item_id] += quantity
        else:
            chart[item_id] = quantity

    request.session['chart'] = chart
    return redirect(redirect_url)


def adjust_chart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    chart = request.session.get('chart', {})

    if size:
        if quantity > 0:
            chart[item_id]['items_by_size'][size] = quantity
        else:
            del chart[item_id]['items_by_size'][size]
            if not chart[item_id]['items_by_size']:
                chart.pop(item_id)
    else:
        if quantity > 0:
            chart[item_id] = quantity
        else:
            chart.pop(item_id)

    request.session['chart'] = chart
    return redirect(reverse('view_chart'))


def remove_from_chart(request, item_id):
    """Remove item from the shopping chart"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        chart = request.session.get('chart', {})

        if size:
            del chart[item_id]['items_by_size'][size]
            if not chart[item_id]['items_by_size']:
                chart.pop(item_id)
        else:
            chart.pop(item_id)

        request.session['chart'] = chart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
