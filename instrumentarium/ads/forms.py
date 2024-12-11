from django import forms
from instrumentarium.ads.models import Ad, Message


class AdBaseForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image', 'condition']


class UploadAdForm(AdBaseForm):
    pass


class AddUpdateForm(AdBaseForm):
    class Meta(AdBaseForm.Meta):
        fields = ['description', 'price', 'image', 'condition']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', )
