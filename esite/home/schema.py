from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from esite.home.models import HomePage

from django.db import models

class ArticleNode(DjangoObjectType):
    class Meta:
        model = HomePage
        only_fields = ['id', 'title', 'date', 'intro', 'body']


class Query(graphene.AbstractType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return HomePage.objects.live()
