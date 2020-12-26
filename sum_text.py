#!/usr/bin/env python
# coding: utf-8

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
class Summarizer():

    def sentence_similarity(self, sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []

        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1

        return 1 - cosine_distance(vector1, vector2)


    def build_similarity_matrix(self, sentences, stop_words):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2:  # ignore if both are same sentences
                    continue
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix


    def generate_summary(self, text, top_n=5):
        stop_words = stopwords.words('english')
        summarize_text = []


        sentences = text


        sentence_similarity_martix = self.build_similarity_matrix(sentences, stop_words)


        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

        #Sort the rank and pick top sentences
        ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        #print("Indexes of top ranked_sentence order are ", ranked_sentence)

        for i in range(top_n):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        return summarize_text






