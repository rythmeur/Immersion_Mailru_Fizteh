# encoding: utf-8
import codecs
from googletrans import Translator

translator = Translator()

#
# import argparse
#
# import six
#
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\pinyin to subtitles-70c303470e17.json"
#
#
# def detect_language(text):
#     # [START translate_detect_language]
#     """Detects the text's language."""
#     from google.cloud import translate_v3 as translate
#     translate_client = translate.Client()
#
#     # Text can also be a sequence of strings, in which case this method
#     # will return a sequence of results for each text.
#     result = translate_client.detect_language(text)
#
#     print('Text: {}'.format(text))
#     print('Confidence: {}'.format(result['confidence']))
#     print('Language: {}'.format(result['language']))
#     # [END translate_detect_language]
#
#
# def list_languages():
#     # [START translate_list_codes]
#     """Lists all available languages."""
#     from google.cloud import translate_v2 as translate
#     translate_client = translate.Client()
#
#     results = translate_client.get_languages()
#
#     for language in results:
#         print(u'{name} ({language})'.format(**language))
#     # [END translate_list_codes]
#
#
# def list_languages_with_target(target):
#     # [START translate_list_language_names]
#     """Lists all available languages and localizes them to the target language.
#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """
#     from google.cloud import translate_v2 as translate
#     translate_client = translate.Client()
#
#     results = translate_client.get_languages(target_language=target)
#
#     for language in results:
#         print(u'{name} ({language})'.format(**language))
#     # [END translate_list_language_names]
#
#
# def translate_text_with_model(target, text, model='nmt'):
#     # [START translate_text_with_model]
#     """Translates text into the target language.
#     Make sure your project is whitelisted.
#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """
#     from google.cloud import translate_v2 as translate
#     translate_client = translate.Client()
#
#     if isinstance(text, six.binary_type):
#         text = text.decode('utf-8')
#
#     # Text can also be a sequence of strings, in which case this method
#     # will return a sequence of results for each text.
#     result = translate_client.translate(
#         text, target_language=target, model=model)
#
#     print(u'Text: {}'.format(result['input']))
#     print(u'Translation: {}'.format(result['translatedText']))
#     print(u'Detected source language: {}'.format(
#         result['detectedSourceLanguage']))
#     # [END translate_text_with_model]
#
#
# def translate_text(target, text, source=None):
#     # [START translate_translate_text]
#     """Translates text into the target language.
#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """
#     from google.cloud import translate_v2 as translate
#     translate_client = translate.Client()
#
#     if isinstance(text, six.binary_type):
#         text = text.decode('utf-8')
#
#     # Text can also be a sequence of strings, in which case this method
#     # will return a sequence of results for each text.
#     result = translate_client.translate(
#         text, target_language=target, source_language=source, )
#
#     print(u'Text: {}'.format(result['input']))
#     print(u'Translation: {}'.format(result['translatedText']))
#     print(u'Detected source language: {}'.format(
#         result['detectedSourceLanguage']))
#     for _ in result:
#         print(_)
#     # [END translate_translate_text]
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description=__doc__,
#         formatter_class=argparse.RawDescriptionHelpFormatter)
#     subparsers = parser.add_subparsers(dest='command')
#
#     detect_langage_parser = subparsers.add_parser(
#         'detect-language', help=detect_language.__doc__)
#     detect_langage_parser.add_argument('text')
#
#     list_languages_parser = subparsers.add_parser(
#         'list-languages', help=list_languages.__doc__)
#
#     list_languages_with_target_parser = subparsers.add_parser(
#         'list-languages-with-target', help=list_languages_with_target.__doc__)
#     list_languages_with_target_parser.add_argument('target')
#
#     translate_text_parser = subparsers.add_parser(
#         'translate-text', help=translate_text.__doc__)
#     translate_text_parser.add_argument('target')
#     translate_text_parser.add_argument('text')
#
#     args = parser.parse_args()
#
#     if args.command == 'detect-language':
#         detect_language(args.text)
#     elif args.command == 'list-languages':
#         list_languages()
#     elif args.command == 'list-languages-with-target':
#         list_languages_with_target(args.target)
#     elif args.command == 'translate-text':
#         translate_text(args.target, args.text)
#
#
# list_languages()
# translate_text('zh-CN', '我这儿有个活')

# with open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\The.Mandalorian.srt",
#           "r") as f:
#     content = f.read()
# with open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\new_file.srt",
#           "w") as f:
#     f.write(content)
# Получилась фигня, надо забирать текст, отдавать его в пхинин

with codecs.open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\The.Mandalorian.srt",
          "r", "gb2312") as f:

# with codecs.open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\29_Chinese.srt",
#                  "r", "utf_8_sig") as f:
    content = f.readlines()
    text = str()
    for line in content:
        if line is not None:
            text = text + line
            try: # detect langugage, if Chinese - add pinyin from google translate
                lang_detected = translator.detect(line)
                print(line)
                print(lang_detected)
                if 'zh' in lang_detected.lang:
                    result = translator.translate(line, src='zh-CN', dest='zh-CN')
                    print(result.pronunciation)
                    if result.pronunciation is not None:
                        text = text + result.pronunciation + ' \n'
            except:
                pass

with codecs.open(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week4\Chinese.srt",
                 "w", 'utf_8_sig') as f:
    f.write(text)
