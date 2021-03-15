from django import template

register = template.Library()

@register.simple_tag

def name_of_page(request):
	return pagename