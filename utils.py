# coding: utf-8


def user_can_add_content(user):
    if not user.is_authenticated():
        return False
    return user.is_staff or user.is_superuser
