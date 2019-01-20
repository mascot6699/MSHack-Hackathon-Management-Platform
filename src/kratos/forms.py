from django import forms

from .models import AmbassadorInfo


class AmbassadorInfoForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), input_formats=["%d/%m/%Y"], label='Date of Birth')

    class Meta:
        model = AmbassadorInfo
        exclude = ('user', 'created_date', 'status')