from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Meldung, Kommentar

def meldungen(request):
    zeilen =[]
    for m in Meldung.objects.all():
        zeilen.append("Meldung: '{}' vom {}".format(
            m.titel, m.zeitstempel.strftime('%d.%m.%Y um %H:%M')
        ))
        zeilen.append('Text: {}'.format(m.text))
        zeilen.append('Anzahl Kommentare: {}'.format(m.kommentar_set.count()))
        zeilen += ['', '-' * 30, '']
    antwort = HttpResponse('\n'.join(zeilen))
    antwort['Content-Type'] = 'text/plain'
    return antwort
