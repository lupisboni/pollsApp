from django.shortcuts import redirect, render, get_object_or_404

from .models import Quiestion

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
        choice_id = request.POST.get('choise')
        print(choice_id)
        choice = q.choice_set.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('poll:result', q_id)
    return render(
        request, 
        'poll/vote.html', 
        {
            "question": q
         })

def result(request, q_id):
    try:
        q = Quiestion.objects.get(pk=q_id)
    except Quiestion.DoesNotExist:
        return redirect('poll:home')
    return render(request, 'poll/result.html', {
        "question": q
    })