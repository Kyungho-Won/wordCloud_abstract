#%%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nltk # extract noun from string
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#%%

def filter_strings(string_list, words_to_remove):
    filtered_list = [s for s in string_list if not any(word in s for word in words_to_remove)]
    return filtered_list

#%% Example: List of abstracts (replace with your actual data)
df = pd.read_csv('./data/scopus_all.csv')

"""
abstracts = [
    "This is the first abstract about...",
    "The second abstract discusses...",
    "Another abstract with detailed information..."
    # Add more abstracts as needed
]
"""

list_exclude = ['EEG', 'brain', 'BCI', 'brain-computer interface', 'interface', 'neurofeedbac', 'result', 'method',
                'study', 'system']

# Available fields: 'Abstract' or 'Title'
abstracts = df['Title']
# Combine the abstracts into a single string
all_abstracts = " ".join(abstracts)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_abstracts)

# Display the generated word cloud using matplotlib
"""
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
"""

# Extract noun
nouns_extracted = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(all_abstracts)) if pos[0] == 'N']
nouns_filtered = filter_strings(nouns_extracted, list_exclude)
all_nouns = " ".join(nouns_filtered)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_nouns)

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

