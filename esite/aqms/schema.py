import graphene

from graphene_django.types import DjangoObjectType

from esite.aqms.models import Messdaten


class MessdatenType(DjangoObjectType):
    class Meta:
        model = Messdaten

class Query(graphene.AbstractType):

    a_messdaten = graphene.Field(MessdatenType,
                                UID=graphene.String(),
                                Datum=graphene.String())

    all_messdaten = graphene.List(MessdatenType,
                                Datum=graphene.String())

    def resolve_a_messdaten(self, info, **kwargs):
        kUID = kwargs.get('UID')
        kDatum = kwargs.get('Datum')

        if kUID is not None:
            return Messdaten.objects.get(UID=kUID)

        if kDatum is not None:
            return Messdaten.objects.get(Datum=kDatum)

        return Messdaten.objects.all()

    def resolve_all_messdaten(self, info, **kwargs):
        kDatum = kwargs.get('Datum')

        if kDatum is not None:
            return Messdaten.objects.filter(Datum=kDatum).order_by('-DatumZeit')

        return Messdaten.objects.all().order_by('-DatumZeit')
