from django.shortcuts import redirect, render, get_object_or_404

from .models import Quiestion, Choice
import json

# Create your views here.
def home(request):
    questions = Quiestion.objects.all()
    return render( 
        request, 
        'poll/home.html',
        {
            "questions": questions
         })

def vote(request, q_id):
    q= get_object_or_404(Quiestion, pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choise')
            choice = q.choice_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll:result', q_id)
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'poll/vote.html', {
                    "question": q,
                    "error_message": "Debes elegir algo! XD"
                })
    return render(
        request, 
        'poll/vote.html', 
        {
            "question": q
         })

def result(request, q_id):
    q = get_object_or_404(Quiestion, pk=q_id)
    choices = q.choice_set.all()
    choice_texts = json.dumps([choice.choice_text for choice in choices])
    votes = json.dumps([choice.votes for choice in choices])

    print(choice_texts, votes)  

    return render(request, 'poll/result.html', {
        "question": q,
        "choice_texts": choice_texts,
        "votes": votes
    })
    