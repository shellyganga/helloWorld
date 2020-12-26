import requests
from bs4 import BeautifulSoup

from helloWorld.sum_text import Summarizer

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib import urlopen

import json
import sys
import spacy
from collections import Counter
# from string import punctuation
# import en_core_web_lg
# nlp = en_core_web_lg.load()
from gensim.summarization import keywords

url = "https://factchecktools.googleapis.com/v1alpha1/claims:search?languageCode=en-US&pageSize=3&query=the%20earth%20is%20flat&key=AIzaSyC-PX-31ru9Y3O4RCKOwloQplLgJ2LTCl8"


# def get_hotwords(text):
#     result = []
#     pos_tag = ['PROPN', 'ADJ', 'NOUN']  # 1
#     doc = nlp(text.lower())  # 2
#     for token in doc:
#         # 3
#         if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
#             continue
#         # 4
#         if (token.pos_ in pos_tag):
#             result.append(token.text)
#
#     return result  # 5
# #text = "I don’t want to take anyone else’s word for it. I don’t know if the Earth is flat or round … I just couldn’t dismiss it (flat Earth theory) after four to five months researching this."
# from summa import summarizer
# print(summarizer.summarize(text))
# def get_jsonparsed_data(url):
#     response = urlopen(url)
#     data = response.read().decode("utf-8")
#     return json.loads(data)

def getTextFromURL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))

    # for sentence in article:
    #     print(sentence)
    #     sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    # sentences.pop()
    #
    # return sentences
    # return text




def summarizeURL(text):
    # url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")
    s = Summarizer()
    final_summary = s.generate_summary(text, 2)
    return final_summary

def get_json_data(json):
    for claim in json["claims"]:
        claimu = claim['text']
        claiment = claim['claimant']
        for line in claim["claimReview"]:
            title = line['title']
            j_url = line['url']
            rating = line['textualRating']
    return claimu, claiment, title, j_url, rating


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Chess'
    #text_to_sum = getTextFromURL(url)
    #print(text_to_sum)
    text_to_sum =  """
        In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills.
    """
    sentences = []


    print(summarizeURL(text_to_sum))

# def main(url_json):
#     json = get_jsonparsed_data(url_json)
#     a = [get_json_data(json)]
#     return a
# def splitTextToTriplet(string):
#     words = string.split()
#     grouped_words = [' '.join(words[i: i + 2]) for i in range(0, len(words), 2)]
#     return grouped_words


# main(sys.argv)

# claim = main(flatearth)
# for index, tuple in enumerate(claim):
# 	print(claim[index])


#
#         # for thing in line['textualRating']:
#         #     print(thing)
#         # print(k['claimReview']['textualRating'])
#         # # #print(v['address']['addressLine2'])
#         # # print ('')
# falsec = 0
# truec = 0
# #print(info)
# somethin = []
# false = ["False", "Falso", "Distorts the Facts", "Misleading", "Mostly False", "Pants on Fire"]
# true = ["True"]
