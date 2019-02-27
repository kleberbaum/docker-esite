from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock

class BlogPage(Page):

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('recipe', SnippetChooserBlock(Recipe)), # Add this line
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

@register_snippet
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ingredients = StreamField([
        ('ingredient', blocks.StructBlock([
            ('name', blocks.CharBlock()),
            ('quantity', blocks.DecimalBlock()),
            ('unit', blocks.ChoiceBlock(choices=[
                ('none', '(no unit)'),
                ('g', 'Grams (g)'),
                ('ml', 'Millilitre (ml)'),
                ('tsp', 'Teaspoon (tsp.)'),
                ('tbsp', 'Tablespoon (tbsp.)'),
            ]))
        ]))
    ])
    instructions = StreamField([
        ('instruction', blocks.TextBlock()),
    ])

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        StreamFieldPanel('ingredients'),
        StreamFieldPanel('instructions'),        
    ]

    def __str__(self):
        return self.title