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
class HeaderBlock(graphene.ObjectType):
    value = GenericScalar()

class SectionBlock(graphene.ObjectType):
    value = GenericScalar()

class FooterBlock(graphene.ObjectType):
    value = GenericScalar()

class UserBlock(graphene.ObjectType):
    value = GenericScalar()
    user = graphene.Field(UserNode)

    def resolve_user(self, info):
        return User.objects.get(id=self.value)




# Objects
class HomePageBody(graphene.Union):
    class Meta:
        types = (HeaderBlock, SectionBlock, FooterBlock,UserBlock)

class HomePageNode(DjangoObjectType):
    headers = graphene.List(HomePageBody)
    sections = graphene.List(HomePageBody)
    footers = graphene.List(HomePageBody)

    class Meta:
        model = HomePage
        only_fields = ['id', 'title', 'date', 'intro']

    def resolve_headers(self, info):
        repr_headers = []
        for block in self.headers.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_headers.append(SectionBlock(value=value))
            elif block_type == 'h':
                repr_headers.append(HeaderBlock(value=value))
            elif block_type == 'f':
                repr_headers.append(FooterBlock(value=value))
            elif block_type == 'u':
                repr_headers.append(UserBlock(value=value))
        return repr_headers

    def resolve_sections(self, info):
        repr_sections = []
        for block in self.sections.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_sections.append(SectionBlock(value=value))
            elif block_type == 'h':
                repr_sections.append(HeaderBlock(value=value))
            elif block_type == 'f':
                repr_sections.append(FooterBlock(value=value))
            elif block_type == 'u':
                repr_sections.append(UserBlock(value=value))
        return repr_sections

    def resolve_footers(self, info):
        repr_footers = []
        for block in self.footers.stream_data:
            block_type = block.get('type')[0]
            value = block.get('value')
            if block_type == 's':
                repr_footers.append(SectionBlock(value=value))
            elif block_type == 'h':
                repr_footers.append(HeaderBlock(value=value))
            elif block_type == 'f':
                repr_footers.append(FooterBlock(value=value))
            elif block_type == 'u':
                repr_footers.append(UserBlock(value=value))
        return repr_footers


# Query
class Query(graphene.AbstractType):
    homepage = graphene.List(HomePageNode)

    @graphene.resolve_only_args
    def resolve_homepage(self):
        return HomePage.objects.live()
