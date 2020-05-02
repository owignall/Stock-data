from django.shortcuts import render
from .forms import Symbol
from . import fetch

# Create your views here.
def home(request):
	if request.method == "POST":
		form = Symbol(request.POST)
		if form.is_valid():
			code = (form.cleaned_data["name"]).upper()
			data = fetch.data_fetch(code)
			# dictionary = {
			# 	"form":form, 
			# 	"run":True,
			# 	"close":'Test',
			# 	"high":'Test',
			# 	'low':'Test',
			# 	'open':'Test',
			# 	'previous_close':'Test',
			# 	'code':code
			# }
			data.update({'form' : form})
			data.update({'run' : True})
			data.update({'code' : code})
			return render(request, 'stock_data_app/home.html', data)
	else:
		form = Symbol()
		dictionary = {
				"form":form, 
				"run":False
			}
		return render(request, 'stock_data_app/home.html', dictionary)