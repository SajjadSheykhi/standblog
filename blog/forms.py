from django import forms
from django.core.validators import ValidationError
from . models import Message


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='please insert your name')
    text = forms.CharField(widget=forms.TextInput(), label='please insert your problem')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code='name_text_same')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


