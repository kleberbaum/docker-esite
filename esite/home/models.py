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
class Button(models.Model):
    button = StreamField([
      ('title', blocks.CharBlock(blank=True, classname="full", icon='title')),
      ('id', blocks.CharBlock(blank=True, classname="full", icon='title')),
      ('class', blocks.CharBlock(blank=True, classname="full", icon='title')),
      ('link', blocks.CharBlock(blank=True, classname="full", icon='title'))
    ])

    panels = [
      FieldPanel('button')   
    ]

    def __str__(self):
      return self.name

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

    infos = StreamField([
      ('logo', ImageChooserBlock(classname="full")),
      ('companyinfos', blocks.StructBlock([
        ('city', blocks.CharBlock(classname="full")),
        ('zip', blocks.DecimalBlock(classname="full")),
        ('address', blocks.CharBlock(classname="full")),
        ('phone', blocks.CharBlock(classname="full")),
        ('email', blocks.CharBlock(classname="full")),
        ('copyrightholder', blocks.CharBlock(classname="full"))
      ])),
      ('sociallinks', blocks.StreamBlock([
        ('img', ImageChooserBlock(classname="full"))
        ('link', blocks.CharBlock(classname="full"))
      ], required=False, icon='doc-full'))
    ])
    
    headers = StreamField([
        ('h_hero', blocks.StructBlock([
          ('hero', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('button', blocks.StructBlock([
                ('btn', SnippetChooserBlock(Button))
              ]))
            ], icon='doc-full'))
          ], icon='cogs'))
        ], icon='image')),
      ])

    sections = StreamField([
        ('s_why', blocks.StructBlock([
          ('why', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
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
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='group')),
        ('s_individual', blocks.StructBlock([
          ('individual', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('lead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='user')),
        ('s_experts', blocks.StructBlock([
          ('experts', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('lead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='pick')),
        ('s_lab', blocks.StructBlock([
          ('lab', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('lead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='snippet')),
        ('s_method', blocks.StructBlock([
          ('method', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='site')),
        ('s_method', blocks.StructBlock([
          ('method', blocks.StructBlock([
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
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='site')),
        ('s_quotes', blocks.StructBlock([
          ('quotes', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('quote', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='doc-full'))
          ])),
          ('button', blocks.StructBlock([
            ('btn', SnippetChooserBlock(Button))
          ]))
        ], icon='openquote')),
        ('s_reviews', blocks.StructBlock([
          ('reviews', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('quote', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('name', blocks.CharBlock(blank=True, classname="full", icon='title')),
              ('title', blocks.CharBlock(blank=True, classname="full", icon='title'))
            ]))
          ])),
          ('button', blocks.StructBlock([
            ('btn', SnippetChooserBlock(Button))
          ]))
        ], icon='form')),
        ('s_pricing', blocks.StructBlock([
          ('pricing', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('cards', blocks.StreamBlock([
              ('card', blocks.StructBlock([
              ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('subhead', blocks.CharBlock(blank=True, classname="full", icon='title')),
              ('price', blocks.CharBlock(blank=True, classname="full", icon='title')),
              ('button', blocks.StructBlock([
                ('btn', SnippetChooserBlock(Button))
              ]))
            ]))
            ]))
          ]))
        ], icon='home')),
        ('s_about', blocks.StructBlock([
          ('about', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),('head', blocks.CharBlock(blank=True, classname="full title", icon='title')),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('subhead', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='home'))
      ])

    footers = StreamField([
        ('f_info', blocks.StructBlock([
          ('info', blocks.StructBlock([
            ('placeholder', blocks.CharBlock(blank=True, classname="full", icon='title'))
          ]))
        ], icon='placeholder'))
    ])

    main_content_panels = [
      StreamFieldPanel('headers'),
      StreamFieldPanel('sections'),
      StreamFieldPanel('footers')
    ]
 
    edit_handler = TabbedInterface([
      ObjectList(Page.content_panels + main_content_panels, heading='Main'),
      ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])