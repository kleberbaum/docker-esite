from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock

@register_snippet
class User(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    infos = StreamField([
        ('infos', blocks.StructBlock([
            ('hauttyp', blocks.CharBlock()),
            ('leiden', blocks.DecimalBlock()),
            ('status', blocks.ChoiceBlock(choices=[
                ('none', '(no unit)'),
                ('Kunde', 'klein (>0)'),
                ('Kunde', 'mittel (>5)'),
                ('Kunde', 'groß (>10)'),
                ('Stammkunde', 'stammkunde (>50)'),
            ]))
        ]))
    ])
    instructions = StreamField([
        ('instruction', blocks.RichTextBlock()),
    ])

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image'),
        StreamFieldPanel('infos'),
        StreamFieldPanel('instructions'),        
    ]

    def __str__(self):
        return self.name

class HomePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('user', SnippetChooserBlock(User)), # Add this line
    ])

    header = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
    ])

    main = StreamField([
        ('why-us', blocks.RichTextBlock()),
        ('individual', blocks.RichTextBlock()),
        ('experts', blocks.RichTextBlock()),
        ('lab', blocks.RichTextBlock()),
        ('method', blocks.RichTextBlock()),
        ('quotes', blocks.RichTextBlock()),
        ('reviews', SnippetChooserBlock(User)),
        ('pricing', blocks.RichTextBlock()),
        ('about-us', blocks.RichTextBlock()),
    ])

    footer = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
    ])

    main_content_panels = [
      FieldPanel('date'),
      FieldPanel('intro'),
      StreamFieldPanel('body'),
      StreamFieldPanel('header'),
      StreamFieldPanel('main'),
      StreamFieldPanel('footer'),
    ]

    edit_handler = TabbedInterface([
      ObjectList(Page.content_panels + main_content_panels, heading='Main'),
      ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])