from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view,renderer_classes
from app.serializers import UserSerializer, GroupSerializer, ProductSerializer,SupplierSerializer
from app.models import Product, Supplier
from django_filters.rest_framework import DjangoFilterBackend
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.renderers import JSONRenderer
from app.tasks import add

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def whatsAppmsg(request):
    incoming_msg = request.data['Body'].lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if incoming_msg:
        if 'hi' in incoming_msg:
            quote = 'Hello'
            msg.body(quote)
            responded = True
        if 'order' in incoming_msg:
            quote = 'order details'
            msg.body(quote)
            # return a cat pic
            # msg.media('https://cataas.com/cat')
            responded = True
    if not responded:
        msg.body('Sorry!')
    return HttpResponse(str(resp))

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def testsqs(self):
    add.delay(3,5)
    status="true"
    return Response(status)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'sku']

class SupplierList(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
