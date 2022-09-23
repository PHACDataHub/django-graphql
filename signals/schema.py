"""
GraphSL Schema for the Signals App
"""
from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from signals.models import Signal, Contact, Hazard, Quality, Program, SignalContact, SignalLocation
from cities_light.models import City


class SignalContactNode(DjangoObjectType):
    class Meta:
        model = SignalContact
        filter_fields = ['contact', 'signal', 'creator', 'primary']
        interfaces = (relay.Node,)


class SignalLocationNode(DjangoObjectType):
    class Meta:
        model = SignalLocation
        name = "pickes"
        filter_fields = ['signal', 'city', 'date_of_detection']
        interfaces = (relay.Node,)


class ContactNode(DjangoObjectType):
    class Meta:
        model = Contact
        filter_fields = ['first_name']
        interfaces = (relay.Node, )


class SignalNode(DjangoObjectType):
    class Meta:
        model = Signal
        # filter_fields = {
        #     'title': ['exact', 'icontains', 'istartswith'],
        #     'location': ['exact', 'icontains', 'istartswith'],
        #     'contact': ['exact', 'icontains', 'istartswith'],
        #     'source': ['exact', 'icontains', 'istartswith'],
        #     'notes': ['exact', 'icontains'],
        #     'category': ['exact'],
        #     'category__name': ['exact'],
        # }
        filter_fields = ['title']
        interfaces = (relay.Node, )


class HazardNode(DjangoObjectType):
    class Meta:
        model = Hazard
        filter_fields = ['name']
        interfaces = (relay.Node, )


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        filter_fields = ['name']
        interfaces = (relay.Node, )


class QualityNode(DjangoObjectType):
    class Meta:
        model = Quality
        filter_fields = ['name']
        interfaces = (relay.Node, )


class ProgramNode(DjangoObjectType):
    class Meta:
        model = Program
        filter_fields = ['name']
        interfaces = (relay.Node, )


class Query(ObjectType):
    signal = relay.Node.Field(SignalNode)
    all_signals = DjangoFilterConnectionField(SignalNode)

    contact = relay.Node.Field(ContactNode)
    all_contacts = DjangoFilterConnectionField(ContactNode)

    hazard = relay.Node.Field(HazardNode)
    all_hazards = DjangoFilterConnectionField(HazardNode)

    city = relay.Node.Field(CityNode)
    all_cities = DjangoFilterConnectionField(CityNode)

    quality = relay.Node.Field(QualityNode)
    all_qualities = DjangoFilterConnectionField(QualityNode)

    program = relay.Node.Field(ProgramNode)
    all_programs = DjangoFilterConnectionField(ProgramNode)


schema = Schema(query=Query)
