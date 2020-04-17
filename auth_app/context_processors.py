"""Context processor for auth_app"""


def auth_app_context(request):
    """Returns context for auth_app"""
    user = request.user
    return {
        'username': 'Anonymous' if user.is_anonymous else str(user),
    }
