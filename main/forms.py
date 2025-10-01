from django.forms import ModelForm
from main.models import Shop
from django.utils.html import strip_tags

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["name", "price", "thumbnail", "description", "category", "is_featured", "stok"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)