from django import forms


class LinksForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Video's name"
    )
    links = forms.URLField(
        label="Video's link",
        required=False,
        widget=forms.URLInput
    )