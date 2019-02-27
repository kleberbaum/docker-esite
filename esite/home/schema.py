from __future__ import unicode_literals
import graphene
from django.db import models
from graphene_django import DjangoObjectType
from esite.home import graphene_wagtail
from esite.home.models import HomePage, Recipe
from graphene.types.generic import GenericScalar

class Query(graphene.AbstractType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return HomePage.objects.live()

class RecipeNode(DjangoObjectType):
    class Meta:
        model = Recipe

class ParagraphBlock(graphene.ObjectType):
    value = GenericScalar()

class HeadingBlock(graphene.ObjectType):
    value = GenericScalar()

class RecipeBlock(graphene.ObjectType):
    value = GenericScalar()
    recipe = graphene.Field(RecipeNode)

    def resolve_recipe(self, info):
        return Recipe.objects.get(id=self.value)

class HomePageBody(graphene.Union):
    class Meta:
        types = (ParagraphBlock, HeadingBlock, RecipeBlock)

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
            elif block_type == 'recipe':
                repr_body.append(RecipeBlock(value=value))
        return repr_body