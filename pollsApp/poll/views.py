from django.shortcuts import render

from .models import Quiestion
# Create your views here.
def home(request):
    questions = Quiestion.objects.all()
    return render(
        request,
        'poll/home.html',
        {
            "questions": questions
        }
    )

def vote(request, q_id):
    q=Quiestion.objects.get(pk=q_id)
    return render(request, 'poll/vote.html', {

    })
def result(request, q_id):
    pass