from django import forms
from .models import BotManager

class BotForm(forms.ModelForm):
    class Meta:
        model = BotManager
        exclude = ['session'] 
        fields = [
            'name', 'token', 'secret_token', 'endpoint', 'proxy', 'proxy_url', 'object'
        ]
        widgets = {
            'token': forms.PasswordInput(render_value=True),
            'secret_token': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Empty for the system to produce'}),
        }
        
        help_texts = {
            'secret_token': 'If left blank, a secure random token will be generated.',
        }
        
    
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.session = None  # یا {}
        if commit:
            instance.save()
        return instance