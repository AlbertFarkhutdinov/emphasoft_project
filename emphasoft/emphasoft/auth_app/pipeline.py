"""Module for saving user profile at authentification."""
from collections import OrderedDict
from urllib.parse import urlencode, urlunparse

import requests


def save_user_profile(
    backend,
    user,
    response,
    *args,
    **kwargs,
):
    """Function for saving user profile at authentification."""
    if backend.name == 'vk-oauth2':
        api_url1 = urlunparse(
            (
                'https',
                'api.vk.com',
                '/method/friends.get',
                None,
                urlencode(
                    OrderedDict(
                        order='random',
                        name_case='nom',
                        fields='domain',
                        access_token=response['access_token'],
                        v='5.92',
                    ),
                ),
                None,
            ),
        )
        resp1 = requests.get(api_url1)
        if resp1.status_code != 200:
            print('Error', resp1, sep='\n')
            return

        friends = []
        for friend in resp1.json()['response']['items']:
            if len(friends) == 5:
                break
            first_name = friend['first_name']
            last_name = friend['last_name']
            deactivated = friend.get('deactivated', None)
            if deactivated is None and first_name != 'DELETED':
                friends.append('{0} {1}'.format(first_name, last_name))
        if friends:
            user.customuserprofile.friends = ','.join(friends)
