from django import forms

class  DateInput(forms.DateInput):
    input_type = 'date'

class cardForm(forms.Form):
    des = forms.CharField(label="Add a description", widget = forms.TextInput(
        attrs = {
            'class' : 'form-control mb-5',

        }
    ))
    deadline = forms.DateField(label="Add a deadline", widget = DateInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter date of journey',
            'label' : 'Date of Journey'
        }
    ))