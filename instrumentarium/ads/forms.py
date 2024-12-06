from django import forms
from instrumentarium.ads.models import Ad, Message


class AdBaseForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image', 'condition']


class UploadAdForm(AdBaseForm):
    pass


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', )
