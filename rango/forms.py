from django import forms
from rango.models import Category, Page
class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.", required=True)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # is it necessary for the form to work? 
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ("name",)

class PageForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter the title of the page.")
    url = forms.URLField(help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # this is overwriting the clean method of the form which takes place before the form is saved
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get("url")
        if url and not url.startswith("http://"):
            url = f"http://{url}"
            cleaned_data["url"] = url
    class Meta:
        model = Page
        exclude = ("category",)
