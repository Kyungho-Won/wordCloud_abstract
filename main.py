#%%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

#%% Example: List of abstracts (replace with your actual data)
df = pd.read_csv('./data/scopus_all.csv')
print(df) 

"""
abstracts = [
    "This is the first abstract about...",
    "The second abstract discusses...",
    "Another abstract with detailed information..."
    # Add more abstracts as needed
]
"""

# Available fields: 'Abstract' or 'Title'
abstracts = df['Title']
# Combine the abstracts into a single string
all_abstracts = " ".join(abstracts)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_abstracts)

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()