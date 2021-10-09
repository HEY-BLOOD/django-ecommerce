from django.utils.text import slugify

from markdown import Markdown


def unique_slugify(instance, value):
    default_slug = slugify(value)
    slug = default_slug
    Klass = instance.__class__
    num = 0
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=default_slug, num=num)
    return slug


def md_to_html(value):
    md = Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    result = md.convert(value)
    return result
