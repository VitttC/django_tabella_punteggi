## LOOPING NELL'OGGETTO ##

Una volta avviata la shell con 
$ python3 manage.py shell

importare l'oggetto Punti
$from punti.models import Punti

popolo l'oggetto con
$punteggio = Punti(name='', value='').save()

creo una variabile che contenga tutti i punteggi:
$punteggi = Punti.objects.all()

per visualizzare e formattare i dati:
$for punteggio in punteggi:
     print("{} ha totalizzato {} punti".format(punteggio.name, punteggio.value))


OUTPUT:
Bobby ha totalizzato 97 punti
Gavino ha totalizzato 70 punti
Franco ha totalizzato 60 punti
Juanne ha totalizzato 55 punti

A questo punto si possono riordinare in maniera crescente:
$for punteggio in punteggi.order_by('value'): 
     print("{} ha totalizzato {} punti".format(punteggio.name, punteggio.value))

o decrescente usando .order_by('-value')

## FILTERING ##

Creo una nuova variabile per i punteggi più alti:
$ high_scores = Punti.objects.filter(value__gte=80)

$ for punteggio in high_scores.order_by('value'):
      print("{} ha totalizzato {} punti".format(punteggio.name, punteggio.value))

OUTPUT:
Bobby ha totalizzato 97 punti

Per filtrare per nome:
$ nomi_j = Punti.objects.filter(name__startswith='J')

$ for punteggio in nomi_J.order_by('value'):
      print("{} ha totalizzato {} punti".format(punteggio.name, punteggio.value))