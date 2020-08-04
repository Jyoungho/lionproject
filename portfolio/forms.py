from django import forms
from .models import Portfolio, Portfolio_img

class PortfolioForm(forms.ModelForm):
    cont = forms.CharField(max_length=2000, label="내용", widget=forms.Textarea)
    class Meta:
        model = Portfolio
        fields = ('cont', ) # 입력받을 필드들
        widgets = {
            'cont': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'write content',
                },
            ),
        }
        
class PortfolioImgForm(forms.ModelForm):
    # image = forms.ImageField(label='사진 첨부')    
    class Meta:
        model = Portfolio_img
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