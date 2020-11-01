from django import forms


class UploadProfilePicForm(forms.Form):
    image_field = forms.FileField()
