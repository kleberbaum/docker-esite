# Generated by Django 2.1.7 on 2019-05-29 19:50

from django.db import migrations
import esite.home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190529_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniquepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_why', wagtail.core.blocks.StructBlock([('why_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('why_collum1', wagtail.core.blocks.StructBlock([('collum_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('collum_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('why_collum2', wagtail.core.blocks.StructBlock([('collum_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('collum_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('why_collum3', wagtail.core.blocks.StructBlock([('collum_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('collum_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('why_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='group', null=True)), ('s_individual', wagtail.core.blocks.StructBlock([('individual_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('individual_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('individual_lead', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('individual_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('individual_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='user', null=True)), ('s_experts', wagtail.core.blocks.StructBlock([('experts_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('experts_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('experts_lead', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('experts_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('experts_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='pick', null=True)), ('s_lab', wagtail.core.blocks.StructBlock([('lab_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('lab_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('lab_lead', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('lab_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('lab_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='snippet', null=True)), ('s_method', wagtail.core.blocks.StructBlock([('method_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('method_sphere1', wagtail.core.blocks.StructBlock([('sphere_step', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('method_sphere2', wagtail.core.blocks.StructBlock([('sphere_step', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('method_sphere3', wagtail.core.blocks.StructBlock([('sphere_step', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('method_sphere4', wagtail.core.blocks.StructBlock([('sphere_step', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='cogs', null=True)), ('method_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='site', null=True)), ('s_services', wagtail.core.blocks.StructBlock([('services_services', wagtail.core.blocks.StreamBlock([('service', wagtail.core.blocks.StructBlock([('service_head', wagtail.core.blocks.CharBlock()), ('service_content', wagtail.core.blocks.RichTextBlock())], blank=False, icon='doc-full', null=True))], blank=False, null=True)), ('services_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, icon='openquote', null=True)), ('s_reviews', wagtail.core.blocks.StructBlock([('reviews_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('reviews_reviews', wagtail.core.blocks.StreamBlock([('review', wagtail.core.blocks.StructBlock([('review_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('review_quote', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('review_name', wagtail.core.blocks.CharBlock(blank=False, classname='full', null=True)), ('review_info', wagtail.core.blocks.CharBlock(blank=False, classname='full', null=True))], blank=False, null=True))], blank=False, null=True))], blank=False, icon='form', null=True)), ('s_facebook', wagtail.core.blocks.StructBlock([('facebook_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('facebook_urls', wagtail.core.blocks.StreamBlock([('facebook', wagtail.core.blocks.StructBlock([('facebook_url', wagtail.core.blocks.URLBlock(blank=False, classname='full', null=True))], blank=False, null=True))], blank=False, max_num=3, null=True))], blank=False, icon='form', null=True)), ('s_instagram', wagtail.core.blocks.StructBlock([('instagram_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('instagram_captions', wagtail.core.blocks.BooleanBlock(blank=True, help_text='Activate to show texts and hashtags of the given Instagram post on the website.', null=True)), ('instagram_urls', wagtail.core.blocks.StreamBlock([('instagram', wagtail.core.blocks.StructBlock([('instagram_url', wagtail.core.blocks.URLBlock(blank=False, classname='full', null=True))], blank=False, null=True))], blank=False, max_num=3, null=True))], blank=False, icon='form', null=True)), ('s_pricing', wagtail.core.blocks.StructBlock([('pricing_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('pricing_pricingcards', wagtail.core.blocks.StreamBlock([('pricingcard', wagtail.core.blocks.StructBlock([('pricingcard_title', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('pricingcard_description', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True)), ('pricingcard_price', wagtail.core.blocks.DecimalBlock(blank=False, decimal_places=2, null=True)), ('pricingcard_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button))], blank=False, null=True))], blank=False, max_num=3, null=True))], blank=False, icon='home', null=True)), ('s_about', wagtail.core.blocks.StructBlock([('about_image', wagtail.images.blocks.ImageChooserBlock(blank=False, null=True)), ('about_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', null=True)), ('about_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'], null=True))], blank=False, icon='fa-quote-left', null=True)), ('code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True),
        ),
    ]
