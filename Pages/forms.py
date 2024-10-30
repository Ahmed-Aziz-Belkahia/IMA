from django import forms

from Pages.models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    company = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    BUDGET_CHOICES = [
        ('5000-15000', '$5,000-15,000'),
        ('15000-30000', '$15,000-30,000'),
        ('30000-50000', '$30,000-50,000'),
        ('50000+', '$50,000+'),
    ]
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, required=True)
    project_details = forms.CharField(widget=forms.Textarea, required=True)
    privacy_policy = forms.BooleanField(required=True)
    attachment = forms.FileField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Your Comment*', 'rows': 5}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*'}),
        }