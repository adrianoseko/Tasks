from django.shortcuts import render
import pika 

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Propostas
from .serializers import PropostasSerializer

class PropostasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Propostas.objects.all()
    serializer_class = PropostasSerializer


class PropostasListView(ListCreateAPIView):
    queryset = Propostas.objects.all()
    serializer_class = PropostasSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_to_queue(instance)

    def send_to_queue(self, proposal):
        connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
        channel = connection.channel()
        channel.queue_declare(queue='proposals')
        channel.basic_publish(exchange='', routing_key='proposals', body=str(proposal.id))
        connection.close()