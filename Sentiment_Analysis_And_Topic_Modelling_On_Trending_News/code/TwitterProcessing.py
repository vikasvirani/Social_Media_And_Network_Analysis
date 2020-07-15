"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, 2019

@Edited - s3715555 - Vikas Virani

"""

import re

class TwitterProcessing:
    """
    This class is used to pre-process tweets.  This centralises the processing to one location.
    """

    def __init__(self, tokeniser, lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """

        self.tokeniser = tokeniser
        self.lStopwords = lStopwords



    def process(self, text, lemmatizer):
        """
        Perform the processing.
        @param text: the text (tweet) to process
        @param lemmatizer: the lemmatizer from nltk to do lemmatization
        
        @returns: list of (valid) tokens in text
        """

        text = text.lower()
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]

        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        # regex pattern for http & user mentions
        regexHttp = re.compile("^http|^@")

        return [lemmatizer.lemmatize(tok) for tok in tokensStripped if tok not in self.lStopwords and regexDigit.match(tok) == None and regexHttp.match(tok) == None]