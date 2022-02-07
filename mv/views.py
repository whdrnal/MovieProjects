from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .forms import QuestionForm
from .models import Question, Movie
from . import forms


def index(request):
    search_keyword = request.GET.get('search_keyword', '')  # 검색어

    movie_list = Movie.objects.order_by('-id')
    if search_keyword.lower() != "none":
        movie_list = movie_list.filter(
            Q(display_name__icontains=search_keyword) |
            Q(name__icontains=search_keyword)
        ).distinct()
    question_list = Question.objects.order_by('-create_date')

    context = {'question_list': question_list, 'movie_list': movie_list, 'search_keyword': search_keyword}
    return render(request, 'mv/movie_list.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    question_list = movie.question_set.order_by('-create_date')
    form = forms.QuestionForm()
    context = {'movie': movie, 'form': form, 'movie_id': movie_id, 'question_list': question_list, }
    return render(request, 'mv/movie_detail.html', context)


@login_required(login_url='common:login')
def question_create(request, movie_id):
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.movie_id = movie_id
            question.user = request.user
            question.score
            question.save()
            messages.success(request, "질문이 등록되었습니다.")
            return redirect('mv:detail', movie_id=movie_id)
    return redirect('mv:detail', movie_id=movie_id)


@login_required(login_url='common:login')
def question_modify(request, movie_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    movie = Movie.objects.get(id=movie_id)
    if request.user != request.user:
        messages.error(request, '수정권한이 없습니다')

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.update_date = timezone.now()
            question.save()
            messages.success(request, "질문이 수정되었습니다.")
            return redirect('mv:detail', movie_id=movie_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'movie': movie, 'question': question}
    return render(request, 'mv/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, movie_id, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != request.user:
        messages.error(request, '수정권한이 없습니다')
    else:
        question.delete()
        messages.success(request, "질문이 삭제되었습니다.")
        return redirect("mv:detail", movie_id=movie_id)


@login_required(login_url='common:login')
def vote_question(request, movie_id):
    question = get_object_or_404(Question, pk=movie_id)
    if request.user == question.user:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('mv:detail', movie_id=movie_id)


@login_required(login_url='common:login')
def vote_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.voter.add(request.user)
    messages.success(request, movie.voter)

    return redirect('mv:detail', movie_id=movie_id)

