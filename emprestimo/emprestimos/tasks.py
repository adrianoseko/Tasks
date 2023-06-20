from celery import shared_task
from .models import Propostas
import random

@shared_task
def evaluate_proposal(propostas_id):
    print(propostas_id)
    propostas = Propostas.objects.get(pk=propostas_id)
    if random.choice([True, False]):
        propostas.status = 'Aprovada'
    else:
        propostas.status = 'Negada'
    propostas.save()


