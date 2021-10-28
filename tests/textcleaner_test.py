import unittest

from textcleaner import TextCleaner
from textgenerator import TextGenerator


class TextCleanerTest(unittest.TestCase):
    def test_if_text_html_tags_are_removed(self) -> None:
        text = TextGenerator.html_text()
        expected_text = TextGenerator.clean_html_text()

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_HTML_TAGS]))

    def test_if_html_entities_are_decoded(self) -> None:
        text = "&oacute; &atilde; cami&oacute;n &ntilde;o&ntilde;o"
        expected_text = "ó ã camión ñoño"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.DECODE_HTML_ENTITIES]))

    def test_if_accented_characters_are_replaced(self) -> None:
        text = "A b c áéíóú àèìîïòôùüûñç ÁÉÍÓÚ ÑÇ ß $ €"
        expected_text = "A b c aeiou aeiiioouuunc AEIOU NC ss $ EUR"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REPLACE_ACCENTED]))

    def test_if_unicode_spaces_are_replaced(self) -> None:
        text = "16\xa0kg on 24th\xa0June 2021"
        expected_text = "16 kg on 24th June 2021"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REPLACE_UNICODE_NBSP]))

    def test_if_newlines_and_tabs_are_replaced(self) -> None:
        text = "This is her \\ first day at this place.\n Please,\t Be nice to her.\\n"
        expected_text = "This is her   first day at this place.  Please,  Be nice to her. "

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REPLACE_NEWLINES_TABS]))

    def test_if_extra_quotation_is_removed(self) -> None:
        text = "The Simpsons is an American ''animated sitcom' created by '''Matt Groening''"
        expected_text = "The Simpsons is an American 'animated sitcom' created by 'Matt Groening'"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_EXTRA_QUOTATION]))

        text = 'The Simpsons is an American ""animated sitcom" created by """Matt Groening""'
        expected_text = 'The Simpsons is an American "animated sitcom" created by "Matt Groening"'

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_EXTRA_QUOTATION]))

    def test_if_extra_whitespace_is_removed(self) -> None:
        text = "The   Simpsons is an American          animated sitcom created by Matt  Groening"
        expected_text = "The Simpsons is an American animated sitcom created by Matt Groening"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_EXTRA_WHITESPACES]))

    def test_if_urls_are_removed(self) -> None:
        text = "Visit my site www.mysite.com or https://mysite.com\nhttp://www.mysite.ar"
        expected_text = "Visit my site  or \n"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_URLS]))

    def test_if_punctuation_is_removed(self) -> None:
        text = "¿Ser o no ser? ¡Esa es la cuestión! Foo, bar. @#()"
        expected_text = "Ser o no ser Esa es la cuestión Foo bar "

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_PUNCTUATION]))

    def test_if_text_is_lowercased(self) -> None:
        text = "A B CD"
        expected_text = "a b cd"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.LOWERCASE]))

    def test_if_digits_are_removed(self) -> None:
        text = "abcd1234efg567"
        expected_text = "abcdefg"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=[TextCleaner.REMOVE_DIGITS]))

    @staticmethod
    def _create_instance(text: str) -> TextCleaner:
        return TextCleaner(text)
