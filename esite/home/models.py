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

    _title = models.CharField(max_length=255)
    _id = models.CharField(blank=True, max_length=255)
    _class = models.CharField(blank=True, max_length=255)
    _link = models.CharField(blank=True, max_length=255)
    
    panels = [
      FieldPanel('_title'),
      FieldPanel('_id'),
      FieldPanel('_class'),
      FieldPanel('_link'),   
    ]

    def __str__(self):
      return self._title

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
            ('leiden', blocks.DecimalBlock(blank=True, decimal_places=2)),
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
  
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    telefax = models.CharField(blank=True, max_length=255)
    vat_number = models.CharField(blank=True, max_length=255)
    tax_id = models.CharField(blank=True, max_length=255)
    trade_register_number = models.CharField(blank=True, max_length=255)
    court_of_registry = models.CharField(blank=True, max_length=255)
    place_of_registry = models.CharField(blank=True, max_length=255)
    trade_register_number = models.CharField(blank=True, max_length=255)
    ownership = models.CharField(blank=True, max_length=255)
    email = models.CharField(max_length=255)
    sociallinks = models.CharField(max_length=255)

    copyrightholder = models.CharField(max_length=255)

    sociallinks = StreamField([
      ('sociallinks', blocks.StreamBlock([
        ('sociallink', blocks.StructBlock([
          ('icon', blocks.CharBlock(classname="full")),
          ('link', blocks.CharBlock(classname="full"))
        ], icon='doc-full'))
      ], required=False))
    ])

    headers = StreamField([
        ('h_hero', blocks.StructBlock([
          ('hero', blocks.StreamBlock([
            ('slide', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('head', blocks.CharBlock(blank=True, classname="full title")),
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
            ('head', blocks.CharBlock(blank=True, classname="full title")),
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
            ('head', blocks.CharBlock(blank=True, classname="full title")),
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
            ('head', blocks.CharBlock(blank=True, classname="full title")),
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
            ('head', blocks.CharBlock(blank=True, classname="full title")),('head', blocks.CharBlock(blank=True, classname="full title")),
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
            ('head', blocks.CharBlock(blank=True, classname="full title")),
            ('sphere_1', blocks.StructBlock([
              ('step', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_2', blocks.StructBlock([
              ('step', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_3', blocks.StructBlock([
              ('step', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('sphere_4', blocks.StructBlock([
              ('step', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='cogs')),
            ('button', blocks.StructBlock([
              ('btn', SnippetChooserBlock(Button))
            ]))
          ], icon='cogs'))
        ], icon='site')),
        ('s_quotes', blocks.StructBlock([
          ('quotes', blocks.StreamBlock([
            ('quote', blocks.StructBlock([
              ('head', blocks.CharBlock(blank=True, classname="full title")),
              ('quote', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ], icon='doc-full'))
          ])),
          ('button', blocks.StructBlock([
            ('btn', SnippetChooserBlock(Button))
          ]))
        ], icon='openquote')),
        ('s_reviews', blocks.StructBlock([
          ('head', blocks.CharBlock(blank=True, classname="full title")),
          ('reviews', blocks.StreamBlock([
            ('review', blocks.StructBlock([
              ('img', ImageChooserBlock(required=False, classname="full")),
              ('quote', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
              ('name', blocks.CharBlock(blank=True, classname="full")),
              ('title', blocks.CharBlock(blank=True, classname="full"))
            ]))
          ])),
          ('button', blocks.StructBlock([
            ('btn', SnippetChooserBlock(Button))
          ]))
        ], icon='form')),
        ('s_pricing', blocks.StructBlock([
          ('pricing', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title")),
            ('cards', blocks.StreamBlock([
              ('card', blocks.StructBlock([
                ('description', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
                ('price', blocks.DecimalBlock(blank=True, decimal_places=2)),
                ('button', blocks.StructBlock([
                  ('btn', SnippetChooserBlock(Button))
                ]))
              ]))
            ]))
          ]))
        ], icon='home')),
        ('s_about', blocks.StructBlock([
          ('about', blocks.StructBlock([
            ('head', blocks.CharBlock(blank=True, classname="full title")),
            ('img', ImageChooserBlock(required=False, classname="full")),
            ('paragraph', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
          ], icon='cogs'))
        ], icon='home'))
      ])

    footers = StreamField([
      ('f_info', blocks.StructBlock([
        ('info', blocks.StructBlock([
          ('placeholder', blocks.CharBlock(blank=True, classname="full"))
        ]))
      ], icon='placeholder'))
    ])

    token = models.CharField(blank=True, max_length=255)

    main_content_panels = [
      StreamFieldPanel('headers'),
      StreamFieldPanel('sections'),
      StreamFieldPanel('footers')
    ]

    imprint_panels = [
        MultiFieldPanel(
        [
          FieldPanel('city'),
          FieldPanel('zip_code'),
          FieldPanel('address'),
          FieldPanel('telephone'),
          FieldPanel('telefax'),
          FieldPanel('email'),
          FieldPanel('copyrightholder')
        ],
        heading="contact",
        classname="collapsible collapsed"
      ),
      MultiFieldPanel(
        [
          FieldPanel('vat_number'),
          FieldPanel('tax_id'),
          FieldPanel('trade_register_number'),
          FieldPanel('court_of_registry'),
          FieldPanel('place_of_registry'),
          FieldPanel('trade_register_number'),
          FieldPanel('ownership')
        ],
        heading="legal",
        classname="collapsible collapsed"
      ),
      StreamFieldPanel('sociallinks')
    ]

    token_panel = [
      FieldPanel('token')
    ]
 
    edit_handler = TabbedInterface([
      ObjectList(Page.content_panels + main_content_panels, heading='Main'),
      ObjectList(imprint_panels, heading='Imprint'),
      ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])
