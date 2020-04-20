"""Module for saving user profile at authentification"""
from collections import OrderedDict
from urllib.parse import urlencode, urlunparse
import requests


def save_user_profile(backend, user, response, *args, **kwargs):
    """Function for saving user profile at authentification"""
    if backend.name == 'vk-oauth2':
        api_url_1 = urlunparse(('https',
                                'api.vk.com',
                                '/method/friends.get',
                                None,
                                urlencode(
                                    OrderedDict(count=5,
                                                order='random',
                                                name_case='nom',
                                                fields='domain',
                                                access_token=response['access_token'],
                                                v='5.92')),
                                None))
        resp_1 = requests.get(api_url_1)
        if resp_1.status_code != 200:
            print('Сервер VK API ответил ошибкой', resp_1, sep='\n')
            return

        friends = []
        for friend in resp_1.json()['response']['items']:
            if len(friends) == 5:
                break
            if friend["deactivated"] is None:
                friends.append(f'{friend["first_name"]} {friend["last_name"]}')
        if friends:
            user.customuserprofile.friends = ','.join(friends)
