from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock


@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)

    button_id = models.CharField(null=True, blank=True, max_length=255)
    button_class = models.CharField(null=True, blank=True, max_length=255)

    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    panels = [
      FieldPanel('button_title'),
      FieldPanel('button_id'),
      FieldPanel('button_class'),
      FieldPanel('button_link'),
      PageChooserPanel('button_page')
    ]

    def __str__(self):
      return self.button_title


class Hero_SlideBlock(blocks.StructBlock):
    slide_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    slide_subhead = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    slide_image = ImageChooserBlock(null=True, blank=False)
    slide_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class  _H_HeroBlock(blocks.ListBlock):
    def __init__(self, **kwargs): 
        super(_H_HeroBlock, self).__init__(Hero_SlideBlock(), **kwargs) 
    
class Why_CollumBlock(blocks.StructBlock):
    collum_image = ImageChooserBlock(null=True, blank=False)
    collum_paragraph = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")

class _S_WhyBlock(blocks.StructBlock):
    why_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    why_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    why_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    why_collum1 = Why_CollumBlock(null=True, blank=False, icon='cogs')
    why_collum2 = Why_CollumBlock(null=True, blank=False, icon='cogs')
    why_collum3 = Why_CollumBlock(null=True, blank=False, icon='cogs')
    why_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class _S_IndividualBlock(blocks.StructBlock):
    individual_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    individual_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    individual_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    individual_image = ImageChooserBlock(null=True, blank=False)
    individual_lead = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    individual_paragraph = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    individual_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class _S_ExpertsBlock(blocks.StructBlock):
    experts_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    experts_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    experts_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    experts_image = ImageChooserBlock(null=True, blank=False)
    experts_lead = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    experts_paragraph = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    experts_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class _S_LabBlock(blocks.StructBlock):
    lab_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    lab_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    lab_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    lab_image = ImageChooserBlock(null=True, blank=False)
    lab_lead = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    lab_paragraph = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    lab_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class Method_SphereBlock(blocks.StructBlock):
    sphere_step = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")

class _S_MethodBlock(blocks.StructBlock):
    method_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    method_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    method_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    method_sphere1 = Method_SphereBlock(null=True, blank=False, icon='cogs')
    method_sphere2 = Method_SphereBlock(null=True, blank=False, icon='cogs')
    method_sphere3 = Method_SphereBlock(null=True, blank=False, icon='cogs')
    method_sphere4 = Method_SphereBlock(null=True, blank=False, icon='cogs')
    method_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class Services_ServiceBlock(blocks.StructBlock):
    service_head = blocks.CharBlock()
    service_content = blocks.RichTextBlock()

class _S_ServicesBlock(blocks.StructBlock):
    services_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    services_services  = blocks.StreamBlock([
      ('service', Services_ServiceBlock(null=True, blank=False, icon='doc-full'))
    ], null=True, blank=False)
    services_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class Reviews_ReviewBlock(blocks.StructBlock):
    review_image = ImageChooserBlock(null=True, blank=False)
    review_quote = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    review_name = blocks.CharBlock(null=True, blank=False, classname="full")
    review_info = blocks.CharBlock(null=True, blank=False, classname="full")

class _S_ReviewsBlock(blocks.StructBlock):
    reviews_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    reviews_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    reviews_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    reviews_reviews = blocks.StreamBlock([
      ('review', Reviews_ReviewBlock(null=True, blank=False))
    ], null=True, blank=False)

class Facebook_PostBlock(blocks.StructBlock):
    facebook_url = blocks.URLBlock(null=True, blank=False, classname="full")

class _S_FacebookBlock(blocks.StructBlock):
    facebook_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    facebook_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    facebook_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    facebook_urls = blocks.StreamBlock([
      ('facebook', Facebook_PostBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=3)

class Instagram_PostBlock(blocks.StructBlock):
    instagram_url = blocks.URLBlock(null=True, blank=False, classname="full")

class _S_InstagramBlock(blocks.StructBlock):
    instagram_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    instagram_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    instagram_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    instagram_captions = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Activate to show texts and hashtags of the given Instagram post on the website.")
    instagram_urls = blocks.StreamBlock([
      ('instagram',Instagram_PostBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=3)

class Pricing_PricingcardBlock(blocks.StructBlock):
    pricingcard_title = blocks.CharBlock(null=True, blank=False, classname="full title")
    pricingcard_description = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")
    pricingcard_price = blocks.DecimalBlock(null=True, blank=False, decimal_places=2)
    pricingcard_button = SnippetChooserBlock(Button, null=True, blank=True, required=False)

class _S_PricingBlock(blocks.StructBlock):
    pricing_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    pricing_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    pricing_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    pricing_pricingcards = blocks.StreamBlock([
      ('pricingcard', Pricing_PricingcardBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=3)

class _S_AboutBlock(blocks.StructBlock):
    about_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    about_image = ImageChooserBlock(null=True, blank=False)
    about_displayhead = blocks.BooleanBlock(null=True, blank=True, required=False, help_text="Display block head if it fits the design context")
    about_head = blocks.CharBlock(null=True, blank=False, classname="full title")
    about_paragraph = blocks.RichTextBlock(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], classname="full")

class _F_InfoBlock(blocks.StructBlock):
    info_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    info_placeholder = blocks.CharBlock(null=True, blank=False, classname="full")


class UniquePage(Page):
    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(null=True, blank=False, max_length=255)
    telefax = models.CharField(null=True, blank=False, max_length=255)
    vat_number = models.CharField(null=True, blank=False, max_length=255)
    tax_id = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    court_of_registry = models.CharField(null=True, blank=False, max_length=255)
    place_of_registry = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    ownership = models.CharField(null=True, blank=False, max_length=255)
    email = models.CharField(null=True, blank=False, max_length=255)
    sociallinks = models.CharField(null=True, blank=False, max_length=255)

    copyrightholder = models.CharField(null=True, blank=False, max_length=255)

    privacy = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])

    sociallinks = StreamField([
      ('link', blocks.URLBlock())
    ])

    headers = StreamField([
      ('h_hero', _H_HeroBlock(null=True, blank=False, icon='image')),
      ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    sections = StreamField([
      ('s_why', _S_WhyBlock(null=True, blank=False, icon='group')),
      ('s_individual', _S_IndividualBlock(null=True, blank=False, icon='user')),
      ('s_experts', _S_ExpertsBlock(null=True, blank=False, icon='pick')),
      ('s_lab', _S_LabBlock(null=True, blank=False, icon='snippet')),
      ('s_method', _S_MethodBlock(null=True, blank=False, icon='site')),
      ('s_services', _S_ServicesBlock(null=True, blank=False, icon='openquote')),
      ('s_reviews', _S_ReviewsBlock(null=True, blank=False, icon='form')),
      ('s_facebook', _S_FacebookBlock(null=True, blank=False, icon='fa-facebook-official')),
      ('s_instagram', _S_InstagramBlock(null=True, blank=False, icon='fa-instagram')),
      ('s_pricing', _S_PricingBlock(null=True, blank=False, icon='home')),
      ('s_about', _S_AboutBlock(null=True, blank=False, icon='fa-quote-left')),
      ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    footers = StreamField([
      ('f_info', _F_InfoBlock(null=True, blank=False, icon='placeholder')),
      ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    token = models.CharField(null=True, blank=False, max_length=255)

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
      ),
      StreamFieldPanel('sociallinks'),
      MultiFieldPanel(
        [
          FieldPanel('privacy')
        ],
        heading="privacy",
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
    registration_head = models.CharField(null=True, blank=False, max_length=255)
    registration_newsletter_text = models.CharField(null=True, blank=False, max_length=255)
    registration_privacy_text = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])
    registration_info_text = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])
    registration_button = models.ForeignKey(
        'home.Button',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    registration_step_text = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])
    thank_you_text = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])

    content_panels = AbstractForm.content_panels + [
      MultiFieldPanel(
        [
          FieldPanel('registration_head', classname="full title"),
          FieldPanel('registration_newsletter_text', classname="full"),
          FieldPanel('registration_privacy_text', classname="full"),
          FieldPanel('registration_info_text', classname="full"),
          FieldPanel('registration_step_text', classname="full"),
          SnippetChooserPanel('registration_button', classname="full"),
          FieldPanel('thank_you_text', classname="full")
        ],
        heading="content",
      ),
      MultiFieldPanel(
        [
          InlinePanel('form_fields', label="Form fields")
        ],
        heading="data",
      )
    ]