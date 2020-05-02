from django.shortcuts import render
from .forms import Symbol
from . import fetch

# Create your views here.
def home(request):
	if request.method == "POST":
		try:
			form = Symbol(request.POST)
			if form.is_valid():
				code = (form.cleaned_data["name"]).upper()
				data = fetch.data_fetch(code)
				data.update({'form' : form})
				data.update({'run' : True})
				data.update({'code' : code})
				return render(request, 'stock_data_app/home.html', data)
		except Exception as e:
			dictionary = {
				"form":form, 
				"run":False
			}
			return render(request, 'stock_data_app/home.html', dictionary)
	else:
		form = Symbol()
		dictionary = {
				"form":form, 
				"run":False
			}
		return render(request, 'stock_data_app/home.html', dictionary)