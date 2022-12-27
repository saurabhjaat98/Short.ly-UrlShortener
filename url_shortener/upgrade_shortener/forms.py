from django.forms import ModelForm
from .models import LinkInfo


class LinkForm(ModelForm):
    class Meta:
        model = LinkInfo
        fields = ['destination', 'title', 'domain', 'custom_half']
        # help_texts = {'short_link': 'if you went to create your custom link then write you link title after short.ly'}
        labels = {
            'custom_half': 'Custom Back-half',
            'title': 'Title(optional)'
        }
