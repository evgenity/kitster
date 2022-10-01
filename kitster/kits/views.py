from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Kit, Tag, Author


def index(request):
	latest_kits_list = Kit.objects.order_by('-pub_date')[:5]
	output = ', '.join([k.title for k in latest_kits_list])
	tags = Tag.objects.all()
	context = {
		'latest_kits_list': latest_kits_list,
		'tags': tags,
	}
	return render(request, 'kits/index.html', context)

def detail(request, kit_id):
	kit = get_object_or_404(Kit, pk=kit_id)
	return render(request, 'kits/detail.html', {'kit': kit})

def maker(request, maker_name):
	maker = get_object_or_404(Author, name=maker_name)
	return render(request, 'kits/maker.html', {'maker': maker})
