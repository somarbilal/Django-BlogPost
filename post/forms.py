# add validation to the form fields to ensure that the data entered by the user is valid before saving it to the database.


from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'author', 'date_published')
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title should be at least 5 characters long.")
        return title

