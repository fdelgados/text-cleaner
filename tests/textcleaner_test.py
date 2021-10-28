import unittest

from textcleaner import TextCleaner
from textgenerator import TextGenerator


class TextCleanerTest(unittest.TestCase):
    def test_if_text_html_tags_are_removed(self) -> None:
        text = TextGenerator.html_text()
        expected_text = TextGenerator.clean_html_text()

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_html_tags"]))

    def test_if_html_entities_are_decoded(self) -> None:
        text = "&oacute; &atilde; cami&oacute;n &ntilde;o&ntilde;o"
        expected_text = "ó ã camión ñoño"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["decode_html_entities"]))

    def test_if_accented_characters_are_replaced(self) -> None:
        text = "A b c áéíóú àèìîïòôùüûñç ÁÉÍÓÚ ÑÇ ß $ €"
        expected_text = "A b c aeiou aeiiioouuunc AEIOU NC ss $ EUR"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["replace_accented"]))

    def test_if_unicode_spaces_are_replaced(self) -> None:
        text = "16\xa0kg on 24th\xa0June 2021"
        expected_text = "16 kg on 24th June 2021"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["replace_unicode_nbsp"]))

    def test_if_newlines_and_tabs_are_replaced(self) -> None:
        text = "This is her \\ first day at this place.\n Please,\t Be nice to her.\\n"
        expected_text = "This is her   first day at this place.  Please,  Be nice to her. "

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["replace_newlines_tabs"]))

    def test_if_extra_quotation_is_removed(self) -> None:
        text = "The Simpsons is an American ''animated sitcom' created by '''Matt Groening''"
        expected_text = "The Simpsons is an American 'animated sitcom' created by 'Matt Groening'"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_extra_quotation"]))

        text = 'The Simpsons is an American ""animated sitcom" created by """Matt Groening""'
        expected_text = 'The Simpsons is an American "animated sitcom" created by "Matt Groening"'

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_extra_quotation"]))

    def test_if_extra_whitespace_is_removed(self) -> None:
        text = "The   Simpsons is an American          animated sitcom created by Matt  Groening"
        expected_text = "The Simpsons is an American animated sitcom created by Matt Groening"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_extra_whitespaces"]))

    def test_if_urls_are_removed(self) -> None:
        text = "Visit my site www.mysite.com or https://mysite.com\nhttp://www.mysite.ar"
        expected_text = "Visit my site  or \n"

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_urls"]))

    def test_if_punctuation_is_removed(self) -> None:
        text = "¿Ser o no ser? ¡Esa es la cuestión! Foo, bar. @#()"
        expected_text = "Ser o no ser Esa es la cuestión Foo bar "

        cleaner = self._create_instance(text)

        self.assertEqual(expected_text, cleaner.clean(steps=["remove_punctuation"]))

    @staticmethod
    def _create_instance(text: str) -> TextCleaner:
        return TextCleaner(text)
