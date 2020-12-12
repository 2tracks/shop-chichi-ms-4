from django.shortcuts import render


def view_chart(request):
    """ Shows the shopping chart """

    return render(request, 'chart/chart.html')
