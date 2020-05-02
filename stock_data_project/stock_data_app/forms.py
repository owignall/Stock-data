from django import forms

class Symbol(forms.Form):
	name = forms.CharField(label="Stock Code", max_length=20)