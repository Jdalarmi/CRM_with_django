from django import forms
from.models import Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class DateInput(forms.DateInput):
    input_type = "date"

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        )
    last_name = forms.CharField(label="Sobrenome")
    email = forms.EmailField()
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    area_code = forms.CharField(
        label="DDD",
        #regex=r"^/+?1?[0-9]{3}",
        error_messages={"invalid": "Numero de DDD inválido"}
        )
    phone_number = forms.CharField(
        label="Numero de telefone",
        #regex=r"^/+?1?[0-9]{9, 15}",
        error_messages={"invalid": "Numero de telefone inválido"},
        )
        
    country = forms.CharField(label="Pais")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")


    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )
