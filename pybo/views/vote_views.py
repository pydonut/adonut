from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def vote_question_comment(request, comment_id):
    """
    pybo 질문 댓글 추천 등록
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 댓글은 추천할수 없습니다')
    else:
        comment.question_comment_voter.add(request.user)
    return redirect('pybo:detail', question_id=comment.question.id)

@login_required(login_url='common:login')
def vote_answer_comment(request, comment_id):
    """
    pybo 답변 댓글 추천 등록
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 댓글은 추천할수 없습니다')
    else:
        comment.answer_comment_voter.add(request.user)
    return redirect('pybo:detail', question_id=comment.answer.question.id)

@login_required(login_url='common:login')
def cancel_vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.voter.remove(request.user)
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def cancel_vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.voter.remove(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def cancel_vote_question_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.question_comment_voter.remove(request.user)
    return redirect('pybo:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def cancel_vote_answer_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    answer = get_object_or_404(Answer, pk=comment.answer_id)
    comment.answer_comment_voter.remove(request.user)
    return redirect('pybo:detail', question_id=answer.question_id)


