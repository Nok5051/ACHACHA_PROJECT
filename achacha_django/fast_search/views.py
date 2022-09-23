import time
from urllib import request
from django.shortcuts import render, redirect

# 추가
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
import json
from requests.exceptions import ConnectionError
import requests
import base64
from .models import LostItems, Images
from pyhdfs import HdfsClient
from hdfs import InsecureClient
from hdfs.client import Client
from django.core.paginator import Paginator

# Create your views here.

# 1_fast_index.html
def fast_index(request):
    return render(request, 'fast_search/1_fast_index.html')

# 2_fast_image.html
def image_search(request):
    return render(request, 'fast_search/2_fast_image.html')

# 3_fast_keyword.html
def keyword_search(request):
    return render(request, 'fast_search/3_fast_keyword.html')

# 2-1.result.html
def uploaded_image(request):
    if request.method == "POST":
        image = request.FILES['uploadfile'] # 업로드 된 이미지 가져오기
        base64_bytes = base64.b64encode(image.read())   # 이미지 데이터 bytes로 변환
        base64_string = base64_bytes.decode('utf-8')    # bytes 데이터 string 변환(bytes자체를 보내면 안 보내져서 일단 str로 변환했음)
        
        category = request.POST.getlist('category') # 선택된 카테고리 데이터 가져오기
        category = category[0]  # 리스트에서 추출
        
        data = {
            'image' : base64_string,
            'category' : category
        }
        
        response = requests.post('http://localhost:5001/', data=data)
                
        ## flask에서 넘어온 데이터 처리하기
        
        result = response.text
        result = eval(result) # string to list
        
        # image_id 값 추출 / src 찾기 / image 가져오기
        
        image_src_list = []
        image_info = []

        for i in range(len(result)):
            image_name = result[i][:-4]
        
            # mysql - image 테이블에서 src 찾아오기
            Images.objects.filter(images_id_fk1 = image_name).values('src')
            image = Images.objects.filter(images_id_fk1 = image_name).values('src')
            # # 중복값이 있는 경우가 있어서, 그 경우 하나만 가져오도록
            # if image.count() >= 2:
            #     image = image.first()
            
            image_src = image[0]['src']
            
            image_src_list.append(image_src)

            
            # mysql - 분실물명, 날짜 가져오기
            lost_item_data = LostItems.objects.filter(lost_items_id_pk = image_name)[0]
            image_info.append(lost_item_data)
        
        # 페이지네이션
        paginator = Paginator(image_info, 6)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        # AWS에서 실행, hdfs 접속
        client = InsecureClient("http://54.64.90.112:9870/", user="ubuntu")
        
        # 유사 이미지 output for문으로 대조하여 이미지 가져오기
        ## image_src_list : /user/ubuntu/service_image/XXXX.jpg
        download_list=[]
        for img in image_src_list:
                    download = client.download(img, './media/result_image/', overwrite=True, n_threads = 1)
                    download
                    media_route = download[-43:]
                    download_list.append(media_route)

        list = zip(download_list, posts)
        context = {
            "list" : list,
            "post" : posts,
        }
    return render(request, 'fast_search/2-1.result.html', context)