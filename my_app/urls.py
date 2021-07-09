from django.urls import path
from .views import (
    indexView,
    postFriend,
    checkNickName,
)

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname")
    # ...
]