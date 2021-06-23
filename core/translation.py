from modeltranslation.translator import TranslationOptions, translator

from core.models import FAQ


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


translator.register(FAQ, FAQTranslationOptions)
