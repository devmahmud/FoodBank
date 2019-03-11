from django.utils.text import slugify

choices = (
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
    (5, 'Five'),
    (6, 'Six'),
    (7, 'Seven'),
    (8, 'Eight'),
    (9, 'Nine'),
    (10, 'Ten'),
)

def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug
