These web pages are generated using the *index.py* file.

The repository is [Here](https://github.com/ischmidls/ischmidls.github.io/tree/main/pages)

The data source is [Here](https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy)

My Python CsvFigs class uses this flow:


CSV --> Pandas DataFrame --> Plotly GraphObject --> text file

For the DataFrame, I use the collections module from the Python standard library to quickly get the counts for each word from the list of sentence strings.
Then, the imported NLTK module determines whether one of the top 20 occuring words is a noun or a verb to color the bar red in Plotly.


This started as a project to find the mode of the words in Hegel's Phenomenology of Spirit.

I realized I could generalize it. It got out of hand, but I retamed it.
