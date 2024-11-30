from django.shortcuts import render

## TEST INSTALLAZIONE SENZA FILE HTML ##

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('Hello, World!')

from punti.models import Punti
from punti.forms import ScoreForm


def index(request):
    context = {}
    form = ScoreForm()
    punteggi = Punti.objects.all()
    context['punteggi'] = punteggi
    context['titolo'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ScoreForm(request.POST)
            else:
                punteggio = Punti.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=punteggio)
            form.save()
            form=ScoreForm()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            punteggio = Punti.objects.get(id=pk)
            punteggio.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            punteggio = Punti.objects.get(id=pk)
            form = ScoreForm(instance=punteggio)
    context['form'] = form

    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['titolo'] = 'About'
    return render(request, 'about.html', context)