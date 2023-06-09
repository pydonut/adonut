from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question, Comment


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    # 마지막 페이지 번호 계산
    last_page = paginator.count // 10 + 1 if (paginator.count % 10) else paginator.count // 10
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'last_page': last_page}  # <------ so 추가
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    so = request.GET.get('so', 'recent')  # 정렬기준

    question = get_object_or_404(Question, pk=question_id)

    # 정렬
    if so == 'recommend':
        comment_list = Comment.objects.filter(question=question).annotate(num_voter=Count('question_comment_voter')).order_by('-num_voter', '-create_date')
    else:  # recent
        comment_list = Comment.objects.filter(question=question).order_by('-create_date')

    # 페이징처리
    paginator = Paginator(comment_list, 3)  # 페이지당 3개씩 보여주기
    page_obj = paginator.get_page(page)
    # 마지막 페이지 번호 계산
    last_page = paginator.count // 3 + 1 if (paginator.count % 3) else paginator.count // 3
    context = {'question': question, 'comment_list': page_obj, 'so': so, 'last_page': last_page}
    return render(request, 'pybo/question_detail.html', context)
