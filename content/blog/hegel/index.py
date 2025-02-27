# extract Hegel Phenomenology of Spirit
# https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy
# collapse tokenized sentences into single list
# import to ipynb as module
##############################################################

#import csv
#import numpy as np
import pandas as pd
# import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



##############################################################
# # read csv
# csv_list = []
# with open('philosophy_data.csv', 'r') as fd:
#     reader = csv.reader(fd)
#     for row in reader:
#         csv_list.extend(row)

# # dataframe
# df = pd.value_counts(
#     np.array(csv_list)).rename_axis('Word').reset_index(name='Occurances')
##############################################################

# # books available
# TITLES = set(df['title'])

# print(TITLES)

################################################################################
  # text = nltk.word_tokenize("their")
  # pos_tagged = nltk.pos_tag(text)
  # print(pos_tagged)
  # #[('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'),
  # #('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]
  # nouns = filter(lambda x:x[1] in ['NN', 'VB'],pos_tagged)
  # print([noun for noun in nouns])
  # #[('refuse', 'NN'), ('permit', 'NN')]

class CsvFigs:
  """Take Csv convert to HTML of plotly Figs"""
  def __init__(self, df: pd.DataFrame):
    """convert df to count_df & title list & author list"""
    self.TITLES = set(df['title'])
    self.df = df

    def get_authors():
      """LIST OF AUTHORS CORRESPONDS TO SET OF TITLES"""
      authors = []
      # DOES NOT MUTATE SELF.DF
      df = self.df.set_index('title')
      for title in self.TITLES:
        # get value from corresponding row in author column
        author = df['author'].loc[title]
        # TAKE ZERO
        authors.append(author[0])
      return authors
        
    self.AUTHORS = get_authors()

    with open('hegel/index.html', 'w') as f:
        f.write('<h1>Top 20 Word Occurance in...</h1>\n<hr>\n')

  def is_nn_vb(self, word : str):
    """return False if not empty ie is noun or verb"""
    text = nltk.word_tokenize(word)
    pos_tagged = nltk.pos_tag(text)
    nn_vb = filter(lambda x:x[1] in ['NN', 'VB'],pos_tagged)
    nn_vb_lst = [elem for elem in nn_vb]
    # return False if not empty ie is noun or verb
    return not not nn_vb_lst


  def get_tuple_count_list(self, lst : list):
      """constant time lookup structure w/ dict"""
      return Counter(lst).most_common()

  def df_countdf(self, df, title='The Phenomenology Of Spirit'):
    """convert df to df with word and occurance columns"""
    # filter csv

    options =[title]

    # print(True in df['title'].isin(options).to_list())
    # NO TITLES FOUND??
    print(title)
    df = df.loc[df['title'] == title]
    #display(df)
    # df = df[df['title'].isin(options)] 

    # title = 'The Phenomenology Of Spirit'
    # df = df.loc[df['column_name'] == title]
    df = df['sentence_str']

    # sentences to tokens
    lst =  df.values.tolist()
    lst = [sub.split(' ') for sub in lst]
    lst = [j for sub in lst for j in sub]

    # token list to [(token, count)] matrix

    lst = self.get_tuple_count_list(lst)
    lst = lst[0:20]
    print(lst)

    # dataframe
    df = pd.DataFrame(lst, columns=['Word', 'Occurances'])
    
    return df
  
    ###########################################################################
    #df = df_countdf(df)
    ###########################################################################

  def get_nn_vb_index(self, count_df: pd.DataFrame):
    """
    take count dataframe, return index of non-nonword; else return None
    """
    for index, word in enumerate(count_df['Word'].to_list()):
      # word = word[0] # tuple <-- 1st str
      print(word)
      if self.is_nn_vb(word):
        print(word)
        return index
  
  def fig_html(self, author: str, title: str):
    """ 
    Take author and title
    write plotly html to text file
    """
    colors = ['lightslategray',] * 20
    # get count df for title
    
    df = self.df_countdf(self.df, title)
    # get index of nn or vb
    nn_vb_index = self.get_nn_vb_index(df)
    if nn_vb_index is not None:
      colors[nn_vb_index] = 'crimson'

    title = f'Top 20 Word Occurance in {author}\'s {title}'

    fig = go.Figure(data=[go.Bar(
        x=df.Word,
        y=df.Occurances,
        text=df.Occurances,
        marker_color=colors,
    )])
    # prettify
    fig.update_layout(title_text=title,
                      xaxis_title="Word",
                      yaxis_title="Occurances",
                      height=720,
                      width=1280,
                      font=dict(
                      family="Calibri",
                      size=18))
    # fig.show()
    with open('hegel/index.html', 'a') as f:
        f.write(f'<h2><a href="{author}{title}.html" title="{author} {title}">{author}\'s {title}</a></h2>')
        f.write('\n')
    with open(f'hegel/{author}{title}.html', 'w') as f:
        f.write('<h1><a href="../" title="home">home</a></h1>')
        f.write('<hr>\n')
        f.write(fig.to_html(full_html=True, include_plotlyjs='cdn'))
        f.write('\n')
        f.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">')
        
  
  def all_figs(self):
    """
    Repeat fig html for all dataset titles
    """
    for index, title in enumerate(self.TITLES):
      self.fig_html(title=title, 
                    author=self.AUTHORS[index])

################################################################################
################################################################################
def main():
  """TEST CLASS"""
  # read csv
  df = pd.read_csv('philosophy_data.csv', 
                  engine='python', 
                  on_bad_lines='skip')
  figs = CsvFigs(df)
  figs.all_figs()

if __name__ == '__main__':
  main()

### df = df.drop(labels=3, axis=0) # remove white space error
### print(df.iloc[0:20])
### df = df.iloc[0:20]

##########################################################
##########################################################
# TOO MANY VALUES FOR PIE CHART
# fig = px.pie(df, values="Occurances", names="Word",
#               title='Word Occurance in G.W.F. Hegel\'s Phenomenology of Spirit')
# fig.show()

# COLORS - not working
# default_color = "blue"
# colors = {"consciousness": "red"}
# color_discrete_map = {
#     c: colors.get(c, default_color) 
#     for c in df.Word.unique()}
# color_discrete_map[' consciousness'] = 'red'
# for key in color_discrete_map:
#   print(key, color_discrete_map[key])

# print(df.iloc[0].Word)
# FIGURE
# 
# fig = px.bar(df, x="Word", y="Occurances", text_auto=True,
#              title=title,
#              color_discrete_map=color_discrete_map)
# fig.show()
########################################################
########################################################



# print(get_nn_vb_index(df))

