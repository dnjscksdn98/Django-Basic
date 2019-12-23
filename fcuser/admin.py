from django.contrib import admin
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    # 리스트에서 보일 값들 지정
    list_display = ("username", "password")


admin.site.register(Fcuser, FcuserAdmin)  # admin에 사용자 정보 등록
