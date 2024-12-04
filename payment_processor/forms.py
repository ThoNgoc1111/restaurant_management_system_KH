from django import forms

class CardPaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiry_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

class PayPalPaymentForm(forms.Form):
    paypal_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class ShippingAddressForm(forms.Form):
    address_line_1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_line_2 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))