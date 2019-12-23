from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm


def home(request):
    return render(request, "home.html")


def logout(request):
    if request.session.get("user"):  # 현재 로그인한 세션 아이디가 있을경우
        del(request.session["user"])  # sessionid 삭제

    return redirect("/")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session["user"] = form.user_id  # session
            return redirect("/")  # home으로 이동

    else:
        form = LoginForm()  # 로그인 페이지 띄우기

    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")  # 회원가입 페이지 띄우기

    elif request.method == "POST":
        # get : 키에 대한 값이 없다면 기본값으로 설정한 값을 반환
        username = request.POST.get("username", None)  # username 반환
        useremail = request.POST.get("useremail", None)  # email 반환
        password = request.POST.get("password", None)  # password 반환
        re_password = request.POST.get("re-password", None)  # re-password 반환

        res_data = {}

        # 예외 처리
        if not (username and useremail and password and re_password):
            res_data["error"] = "모든 값을 입력해야합니다."

        elif password != re_password:
            res_data["error"] = "비밀번호가 다릅니다."

        else:
            # 사용자 객체 생성
            fcuser = Fcuser(username=username,
                            useremail=useremail,
                            password=make_password(password))  # make_password : 비밀번호를 암호화시켜서 저장
            fcuser.save()  # 데이터 저장

        return render(request, "register.html", res_data)
