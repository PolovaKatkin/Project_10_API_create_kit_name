import configuration
import requests
import data


# Функция авторизации нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.AUTH,
                         json=body, headers=data.headers)


token = post_new_user(data.user_body_auth).json()['authToken']


# Функция создания нового набору у конкретного пользователя
def post_new_client_kit(kit_body):
    auth_token = data.auth_token.copy()
    auth_token['Authorization'] = 'Bearer ' + token
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         json=kit_body, headers=auth_token)


