from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	restaurants =  Restaurant.objects.all()
	context = {
		"restaurants":restaurants, 
	}
	return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
	det = Restaurant.objects.get(id=restaurant_id)
	context = {
		"restaurant": det,
	}
	return render(request, 'detail.html', context)
