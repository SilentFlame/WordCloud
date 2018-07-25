from os import path
from wordcloud import WordCloud
import codecs
import matplotlib.pyplot as plt
from bidi.algorithm import get_display

text = open('test.txt').read()

wordcloud = WordCloud(font_path= 'NotoSansDevanagari-CondensedLight.ttf').generate(text) 

#generate_from_frequencies(linklist)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


