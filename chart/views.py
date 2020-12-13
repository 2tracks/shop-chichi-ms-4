from django.shortcuts import render, redirect


def view_chart(request):
    """ Shows the shopping chart """

    return render(request, 'chart/chart.html')


def add_to_chart(request, item_id):
    """ Add quantity of the specified product to the shopping chart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    chart = request.session.get('chart', {})

    if item_id in list(chart.keys()):
        chart[item_id] += quantity
    else:
        chart[item_id] = quantity

    request.session['chart'] = chart
    return redirect(redirect_url)
