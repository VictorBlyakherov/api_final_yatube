from posts.models import Follow


def get_following(user: str):
    return Follow.objects.filter(user=user).all()
