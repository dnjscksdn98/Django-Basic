from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={"required": "아이디를 입력해주세요"},
        max_length=64,
        label="사용자 이름"
    )

    password = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요"},
        widget=forms.PasswordInput,  # forms.PasswordInput : 비밀번호 입력을 안보이게 설정
        label="비밀번호"
    )

    # 로그인 데이터 검증
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:  # 아이디와 비밀번호를 둘다 입력했을때
            try:
                fcuser = Fcuser.objects.get(username=username)  # 해당 사용자 객체 반환
            except Fcuser.DoesNotExist:
                self.add_error("username", "아이디가 없습니다.")
                return

            if not check_password(password, fcuser.password):  # 비밀번호 불일치
                self.add_error("password", "비밀번호를 틀렸습니다")

            else:  # 비밀번호 일치
                self.user_id = fcuser.id
