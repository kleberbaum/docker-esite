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

    body = StreamField([
        ('heading', blocks.StructBlock([
          ('about_pages', blocks.StreamBlock([
            ('about', blocks.StructBlock([
              ('blink', blocks.CharBlock(blank=True, classname="full")),
              ('use_image', blocks.BooleanBlock(default=False, help_text="Use picture instead of blink", required=False, classname="full")),
              ('image', ImageChooserBlock(required=False, classname="full")),
              ('boxes', blocks.StreamBlock([
                ('title', blocks.CharBlock(blank=True, classname="full title", icon='title')),
                ('content', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
              ]))
            ], icon='doc-full'))
          ], icon='cogs')),
        ], icon='image')),
        ('paragraph', blocks.RichTextBlock()),
        ('user', SnippetChooserBlock(User)), # Add this line
    ])

    header = StreamField([
        ('h_hero', blocks.StructBlock([
          ('hero', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ])),
              ('btn', blocks.StructBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='image')),
      ])

    main = StreamField([
        ('s_why', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
          ('why', blocks.StructBlock([
            ('collum_1', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('collum_2', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('collum_3', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('btn', blocks.StructBlock([
             ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
             ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
            ]))
          ], icon='cogs'))
        ], icon='group')),
        ('s_individual', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
          ('individual', blocks.StructBlock([
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='user')),
        ('s_experts', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
          ('experts', blocks.StructBlock([
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='pick')),
        ('s_lab', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
          ('lab', blocks.StructBlock([
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='snippet')),
        ('s_method', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
          ('method', blocks.StructBlock([
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='site')),
        ('s_method', blocks.StructBlock([
          ('method', blocks.StreamBlock([
            ('sphere_1', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_2', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_3', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_4', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('btn', blocks.StructBlock([
             ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
             ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
            ]))
          ], icon='cogs'))
        ], icon='openquote')),
        ('s_quotes', blocks.StructBlock([
          ('quotes', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('quote', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='doc-full')),
            ('btn', blocks.StreamBlock([
              ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
              ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
            ]))
          ], icon='cogs'))
        ], icon='form')),
        ('s_reviews', blocks.StructBlock([
          ('reviews', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ])),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='grip')),
        ('s_pricing', blocks.StructBlock([
          ('pricing', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ])),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='home')),
        ('s_about', blocks.StructBlock([
          ('about', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ])),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='placeholder'))
      ])

    footer = StreamField([
        ('f_about', blocks.StructBlock([
          ('about', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ])),
              ('btn', blocks.StreamBlock([
                ('btntext', blocks.CharBlock(blank=True, classname="full", icon='title')),
                ('btnhref', blocks.CharBlock(blank=True, classname="full", icon='title'))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='placeholder'))
    ])

    main_content_panels = [
      StreamFieldPanel('header'),
      StreamFieldPanel('main'),
      StreamFieldPanel('footer'),
      StreamFieldPanel('body'),
    ]
 
    edit_handler = TabbedInterface([
      ObjectList(Page.content_panels + main_content_panels, heading='Main'),
      ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])