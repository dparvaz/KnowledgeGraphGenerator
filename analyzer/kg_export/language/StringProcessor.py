""" StringProcessor class handles language specific string functions"""

import re
import sys

sys.path.append('./../')
from .Lemmatize import Lemmatizer


class StringProcessor(object):

    """ language specific string operations"""

    SPECIAL_CHARACTERS = "|".join(["\?", "\.", "!", ":", ",", "،", "؟", "<", ">", "/", ";", "\{", "\}", "\[", "\]",
                                   "\(", "\)", "\\\\", "\|", "_", "-", "\+", "=", "!", "~", "`"])

    def __init__(self):
        self.contractions_dict = {
            "can't've": "cannot have",
            "couldn't've": "could not have",
            "hadn't've": "had not have",
            "he'd've": "he would have",
            "he'll've": "he will have",
            "how'd'y": "how do you",
            "I'd've": "I would have",
            "I'll've": "I will have",
            "it'd've": "it would have",
            "it'll've": "it will have",
            "mightn't've": "might not have",
            "mustn't've": "must not have",
            "needn't've": "need not have",
            "oughtn't've": "ought not have",
            "sha'n't": "shall not",
            "shan't've": "shall not have",
            "she'd've": "she would have",
            "she'll've": "she will have",
            "shouldn't've": "should not have",
            "that'd've": "that would have",
            "there'd've": "there would have",
            "they'd've": "they would have",
            "they'll've": "they will have",
            "we'd've": "we would have",
            "we'll've": "we will have",
            "what'll've": "what will have",
            "who'll've": "who will have",
            "won't've": "will not have",
            "wouldn't've": "would not have",
            "y'all'd": "you all would",
            "y'all're": "you all are",
            "y'all've": "you all have",
            "you'd've": "you would have",
            "you'll've": "you will have",
            "ain't": "is not",
            "aren't": "are not",
            "can't": "cannot",
            "'cause": "because",
            "could've": "could have",
            "couldn't": "could not",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he would",
            "he'll": "he will",
            "he's": "he is",
            "how'd": "how did",
            "how'll": "how will",
            "how's": "how is",
            "i'd": "I would",
            "i'll": "I will",
            "i'm": "I am",
            "i've": "I have",
            "isn't": "is not",
            "it'd": "it would",
            "it'll": "it will",
            "it's": "it is",
            "let's": "let us",
            "ma'am": "madam",
            "mayn't": "may not",
            "might've": "might have",
            "mightn't": "might not",
            "must've": "must have",
            "mustn't": "must not",
            "needn't": "need not",
            "o'clock": "of the clock",
            "oughtn't": "ought not",
            "shan't": "shall not",
            "she'd": "she would",
            "she'll": "she will",
            "she's": "she is",
            "should've": "should have",
            "shouldn't": "should not",
            "so've": "so have",
            "so's": "so is",
            "that'd": "that had",
            "that's": "that is",
            "there'd": "there would",
            "there's": "there is",
            "they'd": "they would",
            "they'll": "they will",
            "they're": "they are",
            "they've": "they have",
            "to've": "to have",
            "wasn't": "was not",
            "we'd": "we would",
            "we'll": "we will",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what'll": "what will",
            "what're": "what are",
            "what's": "what is",
            "what've": "what have",
            "when's": "when is",
            "when've": "when have",
            "where'd": "where did",
            "where's": "where is",
            "where've": "where have",
            "who'll": "who will",
            "who's": "who is",
            "who've": "who have",
            "why's": "why is",
            "why've": "why have",
            "will've": "will have",
            "won't": "will not",
            "would've": "would have",
            "wouldn't": "would not",
            "y'all": "you all",
            "you'd": "you would",
            "you'll": "you will",
            "you're": "you are",
            "you've": "you have"""
        }

        self.contractions_re = re.compile(
            '(%s)' %
            '|'.join(list(self.contractions_dict.keys())), re.IGNORECASE)

        self.lemmatizer = Lemmatizer()

    def expand_contractions(self, input_string):
        """ exapand standard english language contractions """
        try:
            def replace(match):
                """ replace matched string"""
                return self.contractions_dict[match.group(0).lower()]

            return self.contractions_re.sub(replace, input_string)
        except:
            return input_string

    def normalize(self, input_string, language_code):
        """ clean and leammatize string"""
        self.lemmatizer.set_language(language_code)
        return_string = input_string
        if language_code == 'en':
            expanded_string = self.expand_contractions(input_string)
            if expanded_string.find("'") != -1:
                expanded_string = self.expand_contractions(expanded_string)

            return_string = re.sub(
                StringProcessor.SPECIAL_CHARACTERS,
                ' ',
                expanded_string)  # Remove Non AlphaNumeric Character

        return self.lemmatizer(return_string)


if __name__ == "__main__":
    stringProcessor = StringProcessor()
    # print(stringProcessor.normalize("what's the \working PURPOSE    |in  OF#$ # BANKing LIfe? in {india}=china", 'en'))
    print(stringProcessor.fuzzy_match('what is india', 'what is india'))