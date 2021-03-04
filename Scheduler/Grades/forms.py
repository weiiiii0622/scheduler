from django.forms import ModelForm
from .models import Link  
from django import forms
from mainsite.models import User
from .widgets import MyWidget
import datetime

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
        now = datetime.datetime.now()
        self.fields['date'].widget.attrs['placeholder'] = '{}'.format(now.strftime("%Y/%m/%d"))
        self.fields['scope'].widget.attrs['placeholder'] = '1~3冊'
        self.fields['grade'].widget.attrs['placeholder'] = '98'


    grades_subject_choices = (
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
        choices=grades_subject_choices, required=True
    )
    #grades_test_choices = (User.grades_test_option)
    create_option = forms.ChoiceField(
        label="類型",
        widget=forms.Select(attrs={'class': 'form-control','data-toggle': 'select'}),           
        choices=(), required=True
    )
    新增類型 = forms.CharField(widget=MyWidget())
    date = forms.CharField(max_length=20,label='日期')
    scope = forms.CharField(max_length=20,label='範圍',required=True)
    grade = forms.CharField(max_length=20,label='成績',required=True)
    widget = {
        'date' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        'scope' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
        'grade' : forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
    }
    
    #article = Article.objects.get(pk=1)
    #form = ArticleForm(instance=article)

    
# ,widget=forms.TextInput(attrs={'yyyy/mm/dd'})
# ,widget=forms.TextInput(attrs={'Ch.1'})
# ,widget=forms.TextInput(attrs={'100'})
