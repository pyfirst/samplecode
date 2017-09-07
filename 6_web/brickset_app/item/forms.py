from django.forms import ModelForm

from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'name', 'image_url', 'rating', 'piece_count',
            'minifig_count', 'us_price', 'owner_count', 'want_it_count'
        ]
