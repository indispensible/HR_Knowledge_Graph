from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from knowledgeGraph.migrations.get_knowledge import find_type_category, get_all_detail_click, get_all_detail, \
    find_type_potential, get_DNN_score_eng, get_DNN_score_ch


def index(request):
    return render(request, 'index.html', {'List': '成功'})


def get_all_jobs(request):
    res = request.GET['category']
    name_dict = find_type_category(res)
    # print(name_dict)
    return JsonResponse(name_dict)


def get_details_by_click(request):
    res = request.GET['title']
    name_dict = get_all_detail_click(res)
    # print(name_dict)
    return JsonResponse(name_dict)


def get_details_by_search(request):
    res = request.GET['title']
    name_dict = get_all_detail(res)
    # print(name_dict)
    return JsonResponse(name_dict)


def find_type_potential_search(request):
    res = request.GET['title']
    print(res)
    name_dict = find_type_potential(res)
    # print(name_dict)
    return JsonResponse(name_dict)


def test(request):
    return render(request, 'test.html', {'List': '成功'})


def DNN_english(request):
    res = request.GET['title']
    print(res)
    name= get_DNN_score_eng(res)
    name_dict = {'title': name}
    # print(name_dict)
    return JsonResponse(name_dict)


def DNN_chinese(request):
    res = request.GET['title']
    print(res)
    name= get_DNN_score_ch(res)
    name_dict = {'title': name}
    # print(name_dict)
    return JsonResponse(name_dict)