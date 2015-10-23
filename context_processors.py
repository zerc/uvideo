# coding: utf-8
from utils import user_can_add_content


def user_perms(request):
    return {'IS_USER_CAN_ADD_CONTENT': user_can_add_content(request.user)}
