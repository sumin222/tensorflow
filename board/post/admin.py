from django.contrib import admin
from .models import Post
# 관리자 페이지에 Post 추가
admin.site.register(Post)