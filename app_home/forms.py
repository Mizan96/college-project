from django import forms

from app_home.models import ResultUpload

class UploadResultForm(forms.ModelForm):
    class Meta:
        model = ResultUpload
        fields = ('result_upload',)