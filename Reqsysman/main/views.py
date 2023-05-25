import base64
import json
from urllib.parse import urlparse, parse_qs

from github import Github
import requests
from rest_framework import viewsets
from .models import *
from .serializers import RequirementSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
#from requests_oauthlib import OAuth2Session

from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from requests_oauthlib import OAuth2Session

def index(request):
    return render(request, 'main/structured/index.html')

def requirements(request):
    requirements = Requirement.objects.all()
    context = {'requirements': requirements}
    return render(request, 'main/structured/requirements.html', context)


# def add_requirement(request):
#     if request.method == 'POST':
#         form = RequirementForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохранение данных формы в базе данных
#             #save_requirement_as_json(form.cleaned_data)  # Конвертирование данных формы в JSON и сохранение в файле
#             #send_requirement_to_github()  # Отправка файла с данными формы на GitHub
#             return redirect('success')  # Перенаправление на страницу успешного сохранения
#     else:
#         form = RequirementForm()
#     return render(request, 'new_requirements.html', {'form': form})

def save_requirement_as_json(requirement):# Конвертирование данных формы в JSON и сохранение в файле
    data = {
        'id': requirement.id,
        'description': requirement.description,
        'type': requirement.type.title,
        'priority': requirement.priority,
        'status': requirement.status
    }
    json_data = json.dumps(data, indent=4)
    # Запись в файл
    with open('requirements.json', 'a') as f:
        f.write(json_data)
        f.write('\n')

#GITHUB_API_URL = 'https://api.github.com'
GITHUB_REPO_OWNER = 'Requirements-Management'
GITHUB_REPO_NAME = 'Storage'
GITHUB_ACCESS_TOKEN = '059b15f854ed6ca42275da246137c16b60ef9cd2'









def send_requirement_to_github():
    g = Github(GITHUB_ACCESS_TOKEN)
    repo_owner = GITHUB_REPO_OWNER
    repo_name = GITHUB_REPO_NAME
    repo = g.get_user(repo_owner).get_repo(repo_name)

    # Путь к файлу, который будет отправлен
    file_path = 'requirement.json'

    # Чтение содержимого файла
    with open(file_path, 'r') as file:
        content = file.read()

    # Загрузка файла на GitHub
    repo.create_file(file_path, 'Добавление файла requirement.json', content)

    print('Файл успешно отправлен на репозиторий GitHub.')


import requests
import webbrowser

from flask import Flask, request



# Определите свои клиентские данные

# OAuth endpoints
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'




from django.shortcuts import render
from django.http import HttpResponse


def callback_view(request):
    authorization_response = request.get_full_path()
    print('HI')
    # Обработка полученного AUTHORIZATION_RESPONSE
    # Вы можете сохранить его или передать его в ваше приложение для обмена на токен доступа

    return HttpResponse('Callback received')


import re

client_id = '9ad99ddd97d473537f3e'
client_secret = '059b15f854ed6ca42275da246137c16b60ef9cd2'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


# Константы, которые вы получите после создания OAuth-приложения на GitHub
CLIENT_ID = '9ad99ddd97d473537f3e'
CLIENT_SECRET = '059b15f854ed6ca42275da246137c16b60ef9cd2'
REDIRECT_URI = 'http://127.0.0.1:8000/new_requirement/callback'  # URL, на который GitHub будет возвращать пользователей

# GitHub использует нестандартную схему авторизации, поэтому нам нужно передать это в OAuth2Session
auth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)

# URL авторизации и токена GitHub
AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'


def login(request):
    authorization_url, state = auth.authorization_url(AUTHORIZATION_URL)

    # Сохраняем state в сессии пользователя для последующей защиты от CSRF
    request.session['oauth_state'] = state

    # Перенаправляем пользователя на GitHub для авторизации
    return redirect(authorization_url)






def oauth():
        client_id = '9ad99ddd97d473537f3e'
        client_secret = '059b15f854ed6ca42275da246137c16b60ef9cd2'
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'

        github = OAuth2Session(client_id)

        # Redirect user to GitHub for authorization
        authorization_url, state = github.authorization_url(authorization_base_url)
        print('Please go here and authorize: ', authorization_url)
        return redirect(authorization_url)
        # token = github.fetch_token(token_url, client_secret=client_secret,
        #                                    authorization_response='AUTHORIZATION_RESPONSE')

        # Get the authorization verifier code from the callback url
        #redirect_response = input('Paste the full redirect URL here: ')
        # parsed_response = urlparse(redirect_response)
        # authorization_code = parse_qs(parsed_response.query)['code'][0]
        # print('redirect_response')
        # print(authorization_code)

        # # Используем регулярное выражение для поиска значения code
        # match = re.search(r"code=([a-zA-Z0-9]+)", redirect_response)
        #
        # code = match.group(1)
        # print(code)
        #
        #
        # # Fetch the access token
        # github.fetch_token(token_url, client_secret=client_secret,
        #                    authorization_response=code)
        # print("sdfsdfa")
        # # Fetch a protected resource, i.e. user profile
        # r = github.get('https://api.github.com/user')
        #
        # print(r.content)




def new_requirement(request):
    if request.method == 'GET':
        redirect_response = request
        code = request.GET.get('code')
        print(code)
        print('Это победа!!!')
        token = auth.fetch_token(TOKEN_URL,
                                 client_secret=CLIENT_SECRET,
                                 authorization_response=code)
        print('Это победа!!!')



        # # # Сохраняем токен доступа в сессии пользователя
        # request.session['oauth_token'] = token
        #
        # # Возвращаем пользователя на главную страницу, или туда, куда вы хотите
        # print('jiji')
        form = RequirementForm()
        return render(request, 'main/structured/new_requirement.html', {'form': form})

    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            #requirement.save() # сохраниение в бд
            # Отправка файла с данными формы на GitHub
            #send_requirement_to_github()
            oauth()
            # Конвертирование в JSON и сохранение в файл
            save_requirement_as_json(requirement)
            return HttpResponse('Требование успешно добавлено!')
    else:
        form = RequirementForm()
    return render(request, 'main/structured/new_requirement.html', {'form': form})

# -----------

def Reqsysman(request):
    return render(request, 'main/Reqsysman.html')


def github(request):
    return render(request, 'main/github.html' )


def requirements_list(request):
    requirements = Requirement.objects.all()
    print(requirements)
    context = {'requirements': requirements}
    return render(request, 'main/requirements_list.html', context)

# def admin(request):
#     return render(request, 'main/admin.html' )


# def requirement_list_view(request):
#     requirements = Requirement.objects.all()
#
#     # Логика для фильтрации и сортировки requirements
#
#     return render(request, 'requirement_list.html', {'requirements': requirements})
#
#
# def requirement_detail_view(request, requirement_id):
#     requirement = get_object_or_404(Requirement, pk=requirement_id)
#
#     # Логика для отображения связанных требований
#
#     return render(request, 'requirement_detail.html', {'requirement': requirement})


# def add_requirement(request):
#     if request.method == 'POST':
#         form = RequirementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('requirements_list')
#     else:
#         form = RequirementForm()
#     return render(request, 'add_requirement.html', {'form': form})





class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementController:
    def create_requirement(request):
        # Получение данных из запроса
        type = request.POST.get('type')
        description = request.POST.get('description')

        # Создание нового объекта требования
        requirement = Requirement(type=type, description=description)
        requirement.save()

        # Возврат ответа с созданным объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def update_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору
        requirement = get_object_or_404(Requirement, pk=requirement_id)

        # Обновление данных требования
        requirement.type = request.POST.get('type')
        requirement.description = request.POST.get('description')
        requirement.save()

        # Возврат ответа с обновленным объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def delete_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору и удаление его из базы данных
        requirement = get_object_or_404(Requirement, pk=requirement_id)
        requirement.delete()

        # Возврат ответа с сообщением об успешном удалении
        return JsonResponse({'message': 'Requirement deleted successfully'})

    def get_requirement(request, requirement_id):
        # Получение объекта требования по его идентификатору
        requirement = get_object_or_404(Requirement, pk=requirement_id)

        # Возврат ответа с объектом требования в JSON формате
        return JsonResponse({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

    def get_requirements(request):
        # Получение всех объектов требований из базы данных
        requirements = Requirement.objects.all()

        # Создание списка объектов требований в формате JSON
        requirements_list = []
        for requirement in requirements:
            requirements_list.append({'id': requirement.id, 'type': requirement.type, 'description': requirement.description})

        # Возврат ответа со списком объектов требований в JSON формате
        return JsonResponse({'requirements': requirements_list})





class RequirementTypeController:

    def create_requirement_type(self, request):
        # Получение данных из запроса
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Создание нового объекта типа требований
        requirement_type = RequirementType(name=name, description=description)
        requirement_type.save()

        # Возврат ответа с созданным объектом типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def get_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Возврат ответа с данными объекта типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def update_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Обновление данных объекта типа требований на основе данных из запроса
        requirement_type.name = request.POST.get('name')
        requirement_type.description = request.POST.get('description')
        requirement_type.save()

        # Возврат ответа с обновленными данными объекта типа требований в JSON формате
        return JsonResponse(
            {'id': requirement_type.id, 'name': requirement_type.name, 'description': requirement_type.description})

    def delete_requirement_type(self, request, type_id):
        # Получение объекта типа требований по его идентификатору
        requirement_type = RequirementType.objects.get(id=type_id)

        # Удаление объекта типа требований
        requirement_type.delete()

        # Возврат ответа об успешном удалении объекта типа требований
        return JsonResponse({'message': 'Requirement type has been deleted successfully.'})

