from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

from .models import Kit, Tag, Author, KitHit

def index(request):
	top_kits_list = Kit.objects.order_by('-pub_date')[:6]
	latest_kits_list = Kit.objects.order_by('-pub_date')[:3]
	tags = Tag.objects.all()
	context = {
		'latest_kits_list': latest_kits_list,
		'top_kits_list' : top_kits_list,
		'tags': tags,
	}
	return render(request, 'kits/index.html', context)

def detail(request, kit_id):
	kit = get_object_or_404(Kit, pk=kit_id)
	ip = KitHit.get_client_ip(request)
	kithit = KitHit(pub_date=timezone.now(), kit=kit, ip=ip)
	kithit.save()

	return render(request, 'kits/detail.html', {'kit': kit})

def maker(request, maker_name):
	maker = get_object_or_404(Author, name=maker_name)
	return render(request, 'kits/maker.html', {'maker': maker})

def donate(request, maker_name):
	maker = get_object_or_404(Author, name=maker_name)
	return render(request, 'kits/donate.html', {'maker': maker})

def handler404(request, *args, **argv):
    response = render(request, 'kits/404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'kits/404.html', {})
    response.status_code = 500
    return response