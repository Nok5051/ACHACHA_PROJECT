from django.shortcuts import render
from django.core.paginator import Paginator
from . models import LostItems
from hdfs import InsecureClient
# Create your views here.

def all_index(request):
    lost_items_list = LostItems.objects.all()

    paginator = Paginator(lost_items_list, 5)
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    client = InsecureClient('http://localhost:50070/')
    with client.read('/user/service_img/'):
        return render(request, 'all_search/all_index.html', {'lost_items_list': lost_items_list,
                                                         'posts': posts})