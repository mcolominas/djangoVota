from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Encuesta, Opcion, Voto
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    latest_question_list = Encuesta.objects.order_by('-inicio')
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    try:
        selected_choice = question.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        v = Voto()
        v.usuario = get_object_or_404(User, pk=1)
        v.opcion = selected_choice
        v.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))