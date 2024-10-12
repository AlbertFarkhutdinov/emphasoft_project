"""Context processor for auth_app."""


def auth_app_context(request):
    """Returns context for auth_app."""
    user = request.user
    username = 'username'
    if user.is_anonymous:
        return {username: 'Anonymous'}
    return {username: str(user)}
