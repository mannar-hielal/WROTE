from modeltranslation.translator import register, TranslationOptions
from .models import Post

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields= ('title', 'body')
    required_languages = ('en',)
