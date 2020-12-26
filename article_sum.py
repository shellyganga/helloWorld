import requests
from bs4 import BeautifulSoup


from helloWorld.sum_text import Summarizer

def getTextFromURL(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
  text = text.replace(u"Â", u"").replace(u"â", u"")
  unparsed_sentences = text.split(". ")
  parsed_sentences = []
  for sentence in unparsed_sentences:
    parsed_sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
  parsed_sentences.pop()
  return parsed_sentences

def summarizeURL(url, total_pars):
  url_text = getTextFromURL(url)
  fs = Summarizer()
  final_summary = fs.generate_summary(url_text, total_pars)
  return " ".join(final_summary)

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Chess'
    # url_text = getTextFromURL(url)
    # print(url_text)
    print(summarizeURL(url, 2))




