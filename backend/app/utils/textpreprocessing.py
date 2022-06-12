import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')


def penn2morphy(tag):
    morphy_tag = {'NN': 'n', 'JJ': 'a',
                  'VB': 'v', 'RB': 'r'}
    try:
        return morphy_tag[tag]
    except:
        return 'n'  # if mapping isn't found, fall back to Noun.


def text_preprocessing(corpus):
    print(corpus)
    # Tokenize the given document
    tokenized = word_tokenize(corpus)

    # Lower case all words
    tokenized = [word.lower() for word in tokenized]

    # Remove stopwords
    stopwords_en = set(stopwords.words("english"))
    stopwords_en = stopwords_en.union(set(punctuation))
    tokenized_without_sw = [word for word in tokenized if not word in stopwords_en]

    # Stemming
    # porter = PorterStemmer()
    # tokenized_without_sw = [porter.stem(word) for word in tokenized_without_sw]

    # POS tagging
    doc_tagged = pos_tag(tokenized_without_sw)

    # Lemmatizer
    wnl = WordNetLemmatizer()
    result = [wnl.lemmatize(word, pos=penn2morphy(tag[:2])) for word, tag in doc_tagged]

    return result
