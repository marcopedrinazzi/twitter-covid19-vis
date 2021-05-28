# TODO

## Finire il lavoro dei link in views e aggiornare il readme in views e home

# Twitter Covid19 Visualisation
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

**The repository is structured as follows:**
- ***/extra*** contains lecture notes, scripts and extra stuff we've used to develop the project
- ***/fakecovid* contains the visualisations about the misinformation on twitter about Covid-19**
- ***/generalcovid* contains the visualisations about tweets about Covid-19**
- ***/scatter_text_charts* contains the visualisations about a frequency comparison between the data in the two datasets described below**
- ***/views* described below**
- ***/slides* contains the slides we have used for the presentation of our work**

# Views Folder

This folder has the purpose to let everyone see our work, since Altair, Plotly and Jupyter have some weird problems that doesn't allow the users to watch the charts on Github.
We have cleaned the two main directories **/generalcovid** and **/fakecovid** and uploaded every chart in .png format. You can find all the .png files in the **views/img** folder.

## generalcovid/
### [OK_VIEW_General_Bigrams_Trigrams_Word_Clouds.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Bigrams_Trigrams_Word_Clouds.ipynb)
### [OK_VIEW_General_Dates_Charts.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Dates_Charts.ipynb)
### [OK_VIEW_General_Emojis.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Emojis.ipynb)
### [OK_VIEW_General_Frequency distribution of Retweets and Likes.ipnyb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Frequency%20distribution%20of%20Retweets%20and%20Likes.ipynb)
### [OK_VIEW_General_Hashtag_Word_Clouds.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Hashtag_Word_Clouds.ipynb)
### [OK_VIEW_General_Heatmap.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Heatmap.ipynb)
### [OK_VIEW_General_Map.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Map.ipynb)
### [OK_VIEW_General_PreProcessing.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_PreProcessing.ipynb)
### [OK_VIEW_General_Tables.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Tables.ipynb)
### [OK_VIEW_General_Text_Word_Clouds.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Text_Word_Clouds.ipynb)
### [OK_VIEW_General_Twitter_Sentiment_Analysis.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Twitter_Sentiment_Analysis.ipynb)
### [OK_VIEW_General_Users_and_Mentions_Word_Clouds.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/OK_VIEW_General_Users_and_Mentions_Word_Clouds.ipynb)
### [VIEW_General_Strip_Plot.ipynb](https://nbviewer.jupyter.org/github/marcopedrinazzi/twitter-covid19-vis/blob/main/views/generalcovid/VIEW_General_Strip_Plot.ipynb)

## fakecovid/

## scatter_text_charts/

# Visualisations about Covid-19 Tweets (/generalcovid)

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19<br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104. https://arxiv.org/abs/2005.05710<br>

Sentiment analysis done through: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

The dataset that we've used is composed by one column: <b>tweet_id</b><br>

If you want to access a tweet from its ID you can use any user name and the url will redirect to the correct twitter handle.<br>
For instance, if I go to: <br>
https://twitter.com/anyuser/status/1341161857931874304<br>
The link redirects to:<br>
https://twitter.com/Twitter/status/1341161863103488003<br>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/DocNow/twarc <br>
We've executed the following command to get the needed results:<br>

<code> twarc --tweet_mode extended hydrate general_dataset.csv > general_result.json
</code>
<br>

The <i>general_result.json</i> file isn't available online due to the limits of GitHub on big files and for compliance reasons to Twitter.


## Visualisations about Covid19 Misinformation on Twitter (/fakecovid)

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 <br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104. https://arxiv.org/abs/2005.05710<br>

The dataset that we've used is composed by two columns: <b>tweet_id</b> and <b>tweet_class</b><br>

If you want to access a tweet from its ID you can use any user name and the url will redirect to the correct twitter handle.<br>
For instance, if I go to: <br>
https://twitter.com/anyuser/status/1341161857931874304<br>
The link redirects to:<br>
https://twitter.com/Twitter/status/1341161863103488003<br>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/DocNow/twarc. In this case we've produced a one version column of the dataset with only the <b>tweet_id</b> to complete the hydratation.
We've executed the following command to get the needed results:<br>

<code> twarc --tweet_mode extended hydrate fakecovid_dataset_one_column.csv > fakecovid_result.json
</code><br>

Afte the hydratation, we've found some tweets which weren't about COVID19, so we've deleted them from <i>fakecovid_result.json</i>.
<br>

