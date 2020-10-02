from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

class MyWidget(forms.Widget):
	template_name = 'Grades/button.html'
	def render(self,name,value,attrs=None,renderer=None):
		# super().render(name,value,attrs,renderer)
		# flat_attrs = flatatt(attrs)
		html = '''
		<button onclick="prompt_test()" id="prompt_input">＋</button>
		'''
		return mark_safe(html)
