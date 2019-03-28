from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

@register_snippet
class Button(models.Model):
    button_title = models.CharField(max_length=255)
    button_id = models.CharField(blank=True, max_length=255)
    button_class = models.CharField(blank=True, max_length=255)
    button_link = models.CharField(blank=True, max_length=255)
    
    panels = [
      FieldPanel('button_title'),
      FieldPanel('button_id'),
      FieldPanel('button_class'),
      FieldPanel('button_link'),   
    ]

    def __str__(self):
      return self.button_title


class _H_HeroBlock(blocks.StructBlock):
    hero_image = ImageChooserBlock(required=False)
    hero_head = blocks.CharBlock(blank=True, classname="full title")
    hero_subhead = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    hero_button = SnippetChooserBlock(Button)

class Why_CollumBlock(blocks.StructBlock):
    collum_image = ImageChooserBlock(required=False, classname="full")
    collum_paragraph = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")

class _S_WhyBlock(blocks.StructBlock):
    why_head = blocks.CharBlock(blank=True, classname="full title")
    why_collum_1 = Why_CollumBlock(icon='cogs')
    why_collum_2 = Why_CollumBlock(icon='cogs')
    why_collum_3 = Why_CollumBlock(icon='cogs')
    why_button = SnippetChooserBlock(Button)

class _S_IndividualBlock(blocks.StructBlock):
    individual_head = blocks.CharBlock(blank=True, classname="full title")
    individual_image = ImageChooserBlock(required=False, classname="full")
    individual_lead = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    individual_paragraph = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    individual_button = SnippetChooserBlock(Button)

class _S_ExpertsBlock(blocks.StructBlock):
    experts_head = blocks.CharBlock(blank=True, classname="full title")
    experts_image = ImageChooserBlock(required=False, classname="full")
    experts_lead = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    experts_paragraph = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    experts_button = SnippetChooserBlock(Button)

class _S_LabBlock(blocks.StructBlock):
    lab_head = blocks.CharBlock(blank=True, classname="full title")
    lab_image = ImageChooserBlock(required=False, classname="full")
    lab_lead = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    lab_paragraph = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    lab_button = SnippetChooserBlock(Button)

class Method_SphereBlock(blocks.StructBlock):
    sphere_step = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")

class _S_MethodBlock(blocks.StructBlock):
    method_head = blocks.CharBlock(blank=True, classname="full title")
    method_sphere_1 = Method_SphereBlock(icon='cogs')
    method_sphere_2 = Method_SphereBlock(icon='cogs')
    method_sphere_3 = Method_SphereBlock(icon='cogs')
    method_sphere_4 = Method_SphereBlock(icon='cogs')
    method_button = SnippetChooserBlock(Button)

class Quotes_QuoteBlock(blocks.StructBlock):
    quote_head = blocks.CharBlock(blank=True, classname="full title")
    quote_content = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")

class _S_QuotesBlock(blocks.StructBlock):
    quotes_quotes = blocks.StreamBlock([
      ('quotes', Quotes_QuoteBlock(icon='doc-full'))
    ])
    reviews_button = SnippetChooserBlock(Button)

class Reviews_ReviewBlock(blocks.StructBlock):
    review_image = ImageChooserBlock(required=False, classname="full")
    review_quote = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    review_name = blocks.CharBlock(blank=True, classname="full")
    review_info = blocks.CharBlock(blank=True, classname="full")

class _S_ReviewsBlock(blocks.StructBlock):
    reviews_head = blocks.CharBlock(blank=True, classname="full title")
    reviews_reviews = blocks.StreamBlock([
      ('review', Reviews_ReviewBlock())
    ])

class Pricing_PricingcardBlock(blocks.StructBlock):
    pricingcard_title = blocks.CharBlock(blank=True, classname="full title")
    pricingcard_description = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")
    pricingcard_price = blocks.DecimalBlock(blank=True, decimal_places=2)
    pricingcard_button = SnippetChooserBlock(Button)

class _S_PricingBlock(blocks.StructBlock):
    pricing_head = blocks.CharBlock(blank=True, classname="full title")
    pricing_pricingcards = blocks.StreamBlock([
      ('pricingcard', Pricing_PricingcardBlock())
    ], max_num=3)

class _S_AboutBlock(blocks.StructBlock):
    about_image = ImageChooserBlock(required=False, classname="full")
    about_head = blocks.CharBlock(blank=True, classname="full title")
    about_paragraph = blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")

class _F_InfoBlock(blocks.StructBlock):
    info_placeholder = blocks.CharBlock(blank=True, classname="full")


class UniquePage(Page):
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

    privacy = RichTextField(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'])

    sociallinks = StreamField([
      ('sociallink', blocks.StructBlock([
        ('icon', blocks.CharBlock(classname="full")),
        ('link', blocks.CharBlock(classname="full"))
      ], icon='doc-full'))
    ])

    headers = StreamField([
      ('h_hero', _H_HeroBlock(icon='image'))
    ])

    sections = StreamField([
      ('s_why', _S_WhyBlock(icon='group')),
      ('s_individual', _S_IndividualBlock(icon='user')),
      ('s_experts', _S_ExpertsBlock(icon='pick')),
      ('s_lab', _S_LabBlock(icon='snippet')),
      ('s_method', _S_MethodBlock(icon='site')),
      ('s_quotes', _S_QuotesBlock( icon='openquote')),
      ('s_reviews', _S_ReviewsBlock(icon='form')),
      ('s_pricing', _S_PricingBlock(icon='home')),
      ('s_about', _S_AboutBlock(icon='home'))
    ])

    footers = StreamField([
      ('f_info', _F_InfoBlock(icon='placeholder'))
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
      StreamFieldPanel('sociallinks'),
      MultiFieldPanel(
        [
          FieldPanel('privacy')
        ],
        heading="legal",
        classname="collapsible collapsed"
      )
    ]

    token_panel = [
      FieldPanel('token')
    ]
 
    edit_handler = TabbedInterface([
      ObjectList(Page.content_panels + main_content_panels, heading='Main'),
      ObjectList(imprint_panels, heading='Imprint'),
      ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractForm):
    thank_you_text = models.TextField(blank=True)

    content_panels = AbstractForm.content_panels + [
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
    ]