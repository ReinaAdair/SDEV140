# -*- Coding: utf-8 -*-
from django.shortcuts import render
# View for index page. 
def home(request):
	my_variable = "Hello World !"
	years_old = 24
	array_city_capital = ["Paris", "London", "Washington"]
	return render(request, 'en/public/index.html', {"my_var":my_variable, "years":years_old, "array_city":array_city_capital})