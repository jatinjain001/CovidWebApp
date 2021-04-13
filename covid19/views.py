from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4ea9ab505cmshfca94dd3382c7ffp1ba48ejsnc77898480081",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def helloworldview(request):
    mylist = []
    noofresults = int(response['results'])
    for i in range(0, noofresults):
        # print(response['response'][i]['country'])
        mylist.append(response['response'][i]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        # print(selectedcountry)
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                active = response['response'][x]['cases']['active']
                deaths = int(total) - int(active) - int(recovered)
                print(new,critical,recovered,total,deaths,active)
                context = {'selectedcountry':selectedcountry,'mylist':mylist,'new': new, 'critical': critical, 'recovered': recovered,'total': total, 'active': active, 'deaths': deaths}
                return render(request, 'helloworldview.html', context)
    # print(response['response'][x]['cases'])
    # print(response['response'][0])
    context = {'mylist': mylist}
    return render(request, 'helloworldview.html', context)
    # return render(request, 'helloworldview.html', {'response': response['response'][0]})


def home(request):
    # return HttpResponse('Hello World')
    mylistitems = ['it1', 'it2', 'it3']
    context = {'name': 'Vanshika', 'mylistitems': mylistitems}
    return render(request, 'hello.html', context)


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
