# TODO

## Abbellire il github


# Twitter Covid19 Visualisation
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

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

The <i>general_result.json</i> file isn't available online due to the limits of GitHub on big files.

<b>Parsing</b><br>

The parsing is done through some Python code on each file. 




<h2>Visualisation about Covid19 Misinformation on Twitter</h2>

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

<b>Parsing</b><br>

The parsing is done through some Python code on each file.

# Views Folder

This folder has the purpose to let everyone see our work, since Altair, Plotly and Jupyter have some weird problems that doesn't allow the users to watch the charts on Github.
We have cleaned the two main directories **/generalcovid** and **/fakecovid** and uploaded every chart in .png format. You can find all the .png files in the **views/img** folder.
