#created forms.py 

from django import forms

from .models import Tweet;

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']  # Include other fields as needed
        
        widgets = {
            'text': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'file-input file-input-bordered w-full'}),}