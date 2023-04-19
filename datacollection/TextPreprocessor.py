from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import unicodedata
from bs4 import BeautifulSoup
import warnings
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')


warnings.filterwarnings("ignore")


class TextPreprocessor:

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.tokenizer = word_tokenize

    def __call__(self, text):
        # make text lowercase
        text.lower()
        # remove any extra white spaces
        text = re.sub(r'^\s*|\s\s*', ' ', text).strip()
        # remove any html tags from text
        text = BeautifulSoup(text, 'html.parser').get_text()
        # remove any URLs from text
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        # remove any accented characters from text
        text = unicodedata.normalize('NFKD', text).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        # separate numbers from words in text
        text = re.sub(r"([0-9]+(\.[0-9]+)?)", r" \1 ", text).strip()
        # remove any numbers and punctuations from text
        # text = re.sub(r'[^a-zA-Z]', ' ', text)
        text = re.sub(r'[0-9]', ' ', text)
        text = re.sub(r'\[.*\]', ' ', text)
        return text
