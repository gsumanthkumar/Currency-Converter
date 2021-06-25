from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    if request.method=='POST':
        d=request.POST['amount']
        fcur=request.POST.get('fcurrency')
        tcur=request.POST.get('tcurrency')
        url = f"https://free.currconv.com/api/v7/convert?q={fcur}_{tcur}&compact=ultra&apiKey=ec75664150b09651dd82"
        user=requests.get(url).json()
        j=float(user[f'{fcur}_{tcur}'])*float(d)
        return render(request,'first/home.html',context={'j':j,'tcur':tcur})
    else:
        return render(request,'first/home.html')