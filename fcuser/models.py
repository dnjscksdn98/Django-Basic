from django.db import models


class Fcuser(models.Model):
    objects = models.Manager()  # objects 관련 오류를 처리하기 위해 선언

    # 멤버 변수 선언
    # verbose_name : 화면에서 보이는 이름 지정
    username = models.CharField(max_length=64, verbose_name="사용자명")
    useremail = models.EmailField(max_length=128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")

    # dttm : date time
    # auto_now_add : 생성되는 시기를 자동 등록
    register_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="등록시간")

    # 사용자 추가시 username으로 사용자명을 저장
    def __str__(self):
        return self.username

    # 문서 세부 설정
    class Meta:
        # 테이블명 지정 - 구분하기 위해
        db_table = "fastcampus_fcuser"

        verbose_name = "패스트캠퍼스 사용자"
        verbose_name_plural = "패스트캠퍼스 사용자"
