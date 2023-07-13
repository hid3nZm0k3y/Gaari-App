from django import forms
from .models import Autos, Make, Review, Message

class AutosForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = "__all__"

        labels = {
            "make": "brand"
        }

class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']