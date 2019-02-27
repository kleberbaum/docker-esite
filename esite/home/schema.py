from __future__ import unicode_literals
import graphene
from django.db import models
from graphene_django import DjangoObjectType
from esite.home import graphene_wagtail
from esite.home.models import HomePage, User
from graphene.types.generic import GenericScalar



class UserNode(DjangoObjectType):
    class Meta:
        model = User

class ParagraphBlock(graphene.ObjectType):
    value = GenericScalar()

class HeadingBlock(graphene.ObjectType):
    value = GenericScalar()

class UserBlock(graphene.ObjectType):
    value = GenericScalar()
    user = graphene.Field(UserNode)

    def resolve_user(self, info):
        return User.objects.get(id=self.value)

class HomePageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, UserBlock)

class ArticleNode(DjangoObjectType):
    body = graphene.List(HomePageBody)

    class Meta:
        model = HomePage
        only_fields = ['id', 'title', 'date', 'intro']

    def resolve_body(self, info):
        repr_body = []
        for block in self.body.stream_data:
            block_type = block.get('type')
            value = block.get('value')
            if block_type == 'paragraph':
                repr_body.append(ParagraphBlock(value=value))
            elif block_type == 'heading':
                repr_body.append(HeadingBlock(value=value))
            elif block_type == 'user':
                repr_body.append(UserBlock(value=value))
        return repr_body

class Query(graphene.AbstractType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return HomePage.objects.live()