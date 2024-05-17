def user_context(request):
    return {
        'user_type': request.session.get('user_type'),
        'is_authenticated': request.session.get('is_authenticated'),
    }