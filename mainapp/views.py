from django.shortcuts import render
from .models import Product,Slider

def home(request):
    p_data = Product.objects.all()
    s_data = Slider.objects.all()
   
    return render(request,'index.html',{'p_data': p_data,'s_data':s_data})
