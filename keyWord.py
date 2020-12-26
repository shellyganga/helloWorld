import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
# To get keyword phrases ranked highest to lowest.

# def main(url):
#     url = "https://www.whitehouse.gov/articles/first-lady-melania-trump-personal-experience-covid-19/"
#
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")
#     text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
#
#     r = Rake()
#     text = text.replace(',', '')
#     r.extract_keywords_from_text(text)
#
#     return r.get_ranked_phrases()[0]

from sklearn.feature_extraction.text import CountVectorizer

n_gram_range = (5, 5)
stop_words = "english"

# Extract candidate words/phrases
count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
candidates = count.get_feature_names()

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distilbert-base-nli-mean-tokens')
doc_embedding = model.encode([doc])
candidate_embeddings = model.encode(candidates)

from sklearn.metrics.pairwise import cosine_similarity

top_n = 5
distances = cosine_similarity(doc_embedding, candidate_embeddings)
keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
print(keywords)
