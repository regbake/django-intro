from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader

from .models import Question

def index(request):
    # looks like this is pulling from DB?
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    
    context = {
        'latest_questions_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does no exist")
    """
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the results of question %s"
    # a rather interesting way of appending the question_id
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)