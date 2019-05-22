from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class HomePage(Page):
    body = RichTextUploadingField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class StandardPage(Page):
    body = RichTextUploadingField(blank=True)

    sidebar_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    sidebar_caption = models.CharField(max_length=250, blank=True)

    search_fields = Page.search_fields + (  # Inherit search_fields from Page
        index.SearchField('body'),
        index.FilterField('sidebar_caption'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('sidebar_image'),
        FieldPanel('sidebar_caption'),
    ]

    def get_template(self, request, *args, **kwargs):
        parent = self.get_parent()
        print parent
        if parent is None:
            return "pagecontent/home_page.html"
        elif parent.content_type.model == 'standardpage':
            return "pagecontent/standard_subpage.html"
        else:
            return super(StandardPage, self).get_template(request, *args, **kwargs)


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]
