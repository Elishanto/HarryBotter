from yandex_translate import YandexTranslate
from pycountry import languages
from utils.text import detect_language
from .baseprovider import BaseProvider


class TranslateProvider(BaseProvider):
    @staticmethod
    def get(query, config, params={}, lang='en'):
        translator = YandexTranslate(key=config['yandex_translate_key'])
        lang = detect_language(config, list(translator.langs), query[0])
        to_translate = query[0]
        try:
            to_lang = languages.get(
                name=translator.translate(query[1], 'en')['text'][0].replace('in ', '').capitalize()).iso639_1_code
        except KeyError:
            return {
                'content': 'nan'
            }
        return {
            'type': 'text',
            'content': ' '.join(translator.translate(to_translate, '{}-{}'.format(lang, to_lang))['text'])
        }
