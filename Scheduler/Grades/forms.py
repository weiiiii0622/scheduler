from django.forms import ModelForm
from .models import Link  
from django import forms

class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        # widgets = {
        #     'date' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        #     'test' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        #     'scope' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        #     'grade' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        # }
        # labels = {
        #     'date' : '日期：',
        #     'test' : '考試類型：',
        #     'scope': '範圍：',
        #     'grade': '成績：'
        # }
form = LinkModelForm()

class GradesChoicesForm(forms.Form):
    def __init__(self, options, *args, **kwargs):
        super(GradesChoicesForm, self).__init__(*args, **kwargs)
        self.fields['create_option'].choices = options

    grades_form_choices = (
        ("1","國文"),
        ("2","數學"),
        ("3","英文"),
        ("4","物理"),
        ("5","化學"),
        ("6","生物"),
        ("7","地科"),
        ("8","地理"),
        ("9","歷史"),
        ("0","公民"),
    )
    grades_subject = forms.ChoiceField(
        label="科目",
        widget=forms.Select(attrs={'class': 'form-control','data-toggle': 'select'}),
        choices=grades_form_choices, required=True
    )
    create_option = forms.ChoiceField(
        label="類型",
        widget=forms.Select(attrs={'class': 'form-control','data-toggle': 'select'}),
        choices=(), required=True
    )

    #article = Article.objects.get(pk=1)
    #form = ArticleForm(instance=article)

    



