from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Meldung, Kommentar

def meldungen(request):
    template = loader.get_template('news/meldungen.html')
    context = {'meldungen' : Meldung.objects.all()}
    return HttpResponse(template.render(context))


def meldungen_detail(request, meldungs_id):
    try:
        m = Meldung.objects.get(id=meldungs_id)
    except Meldung.DoesNotExist:
        raise Http404
    zeilen =[]
    zeilen.append("Meldung: '{}' vom {}".format(
        m.titel, m.zeitstempel.strftime('%d.%m.%Y um %H:%M')
    ))
    zeilen.append('Text: {}'.format(m.text))
    zeilen.append('Anzahl Kommentare: {}'.format(m.kommentar_set.count()))
    zeilen += ['', '-' * 30,
    'Kommentare:', '']
    zeilen += ['{}: {}'.format(k.autor, k.text) for k in m.kommentar_set.all()]
    antwort = HttpResponse('\n'.join(zeilen))
    antwort['Content-Type'] = 'text/plain'
    return antwort

