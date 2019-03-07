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




# Blocks
class ParagraphBlock(graphene.ObjectType):
    value = GenericScalar()

class HeadingBlock(graphene.ObjectType):
    value = GenericScalar()

class UserBlock(graphene.ObjectType):
    value = GenericScalar()
    user = graphene.Field(UserNode)

    def resolve_user(self, info):
        return User.objects.get(id=self.value)




# Objects
class HomePageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, UserBlock)

class ArticleNode(DjangoObjectType):
    body = graphene.List(HomePageBody)
    header = graphene.List(HomePageBody)
    main = graphene.List(HomePageBody)
    footer = graphene.List(HomePageBody)

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

    def resolve_header(self, info):
        repr_header = []
        for block in self.header.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_header.append(ParagraphBlock(value=value))
            elif block_type == 'h':
                repr_header.append(HeadingBlock(value=value))
            elif block_type == 'f':
                repr_header.append(HeadingBlock(value=value))
            elif block_type == 'u':
                repr_header.append(UserBlock(value=value))
        return repr_header

    def resolve_main(self, info):
        repr_main = []
        for block in self.main.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_main.append(ParagraphBlock(value=value))
            elif block_type == 'h':
                repr_main.append(HeadingBlock(value=value))
            elif block_type == 'f':
                repr_main.append(HeadingBlock(value=value))
            elif block_type == 'u':
                repr_main.append(UserBlock(value=value))
        return repr_main

    def resolve_footer(self, info):
        repr_footer = []
        for block in self.footer.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_footer.append(ParagraphBlock(value=value))
            elif block_type == 'h':
                repr_footer.append(HeadingBlock(value=value))
            elif block_type == 'f':
                repr_footer.append(HeadingBlock(value=value))
            elif block_type == 'u':
                repr_footer.append(UserBlock(value=value))
        return repr_footer


# Query
class Query(graphene.AbstractType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return HomePage.objects.live()
