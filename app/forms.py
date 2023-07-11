from django import forms

def validate_of_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('First letter should not be a')


def validate_of_length(name):
    if len(name)<=5:
        raise forms.ValidationError('len is less than 5')

class studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_of_a,validate_of_length])
    sage=forms.IntegerField()
    semail=forms.EmailField(max_length=100)
  

