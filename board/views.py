from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
from tag.models import Tag


def board_list(request):
    all_boards = Board.objects.all().order_by(
        "-id")  # - : 역순 정렬, 가장 최신 정보부터 보이도록 설정

    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)  # 한 페이지에 두개씩

    boards = paginator.get_page(page)

    return render(request, "board_list.html", {"boards": boards})


def board_write(request):
    if not request.session.get("user"):  # 로그인을 하지 않은 상태일경우
        return redirect("/fcuser/login/")  # 로그인 페이지로 이동

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            user_id = request.session.get("user")
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data.get("tags").split(",")
            board = Board()
            board.title = form.cleaned_data.get("title")
            board.contents = form.cleaned_data.get("contents")
            board.writer = fcuser
            board.save()  # 데이터베이스에 저장

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(
                    name=tag)  # 있는 태그면 가져오고 없는 태그면 새로 생성
                board.tags.add(_tag)  # 먼저 보드를 저장을 한후에 태그 추가

            return redirect("/board/list/")  # 게시판 목록으로 이동

    else:
        form = BoardForm()

    return render(request, "board_write.html", {"form": form})


def board_detail(request, pk):  # 주소로부터 몇번째 글인지 검색하기 : /detail/n번째 글
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(request, "board_detail.html", {"board": board})
