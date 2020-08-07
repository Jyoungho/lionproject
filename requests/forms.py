from django import forms
from .models import Request, Request_img

class RequestForm(forms.ModelForm):
    cont = forms.CharField(max_length=2000, label="내용", widget=forms.Textarea)
    class Meta:
        model = Request
        fields = ('cont', ) # 입력받을 필드들
        widgets = {
            'cont': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'write content',
                },
            ),
        }
        
class RequestImgForm(forms.ModelForm):
    # image = forms.ImageField(label='사진 첨부')    
    class Meta:
        model = Request_img
        fields = ('img', )
        widgets = {
            'img': forms.ClearableFileInput(
                attrs = {
                    'class' : 'form-control',
                    'label' : '사진 첨부',
                    'multiple' : True,
                },
            ),
        }