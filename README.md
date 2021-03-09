# Twitter Covid19 Visualisation

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

Data from: https://github.com/thepanacealab/covid19_twitter <br>
The dataset comes from this research work: Banda, J. M., Tekumalla, R., Wang, G., Yu, J., Liu, T., Ding, Y., & Chowell, G. (2020). A large-scale COVID-19 Twitter chatter dataset for open scientific research--an international collaboration. arXiv preprint arXiv:2004.03688.

Dataset download: https://zenodo.org/record/4588081#.YEcuDi9aa8o

<table>
  <tr>
    <th>Dataset Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>full_dataset.tsv.gz</td>
    <td></td>
  </tr>
  <tr>
    <td>full_dataset-clean.tsv.gz</td>
    <td></td>
  </tr>
  <tr>
    <td>statistics-full_dataset-clean .tsv</td>
    <td></td>
  </tr>
  <tr>
    <td>statistics-full_dataset.tsv</td>
    <td></td>
  </tr>
  <tr>
    <td>frequent_terms.csvs</td>
    <td></td>
  </tr>
  <tr>
    <td>frequent_bigrams.csv</td>
    <td></td>
  </tr>
  <tr>
    <td>frequent_trigrams.csv</td>
    <td></td>
  </tr>
   <tr>
    <td>emoji.zip</td>
    <td></td>
  </tr>
   <tr>
    <td>hashtag.zip</td>
    <td></td>
  </tr>
   <tr>
    <td>mentions.zip</td>
    <td></td>
  </tr>
</table>

<h2>Visualisation about Covid19 Misinformation on Twitter</h2>

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 <br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104.<br>

The dataset that we've used is composed by two columns: <b>tweet_id</b> and <b>tweet_class</b><br>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/thepanacealab/SMMT. <br>
We're interested in get_metadata.py, which we have downloaded using the following command:<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_acquisition/get_metadata.py -O get_metadata.py</code>
<br>

Then we just have to execute in the terminal:<br>

<code>python3 get_metadata.py -i input.tsv -o hydrated_tweets -k api_keys.json</code><br>

where api_keys.json contains the Twitter API Keys and Tokens in a JSON format.
<br>
The command above returns the following files:
- A <b>hydrated_tweets.json</b> file which contains the full json object for each of the hydrated tweets
- A <b>hydrated_tweets.CSV</b> file which contains partial fields extracted from the tweets.
- A <b>hydrated_tweets.zip</b> file which contains a zipped version of the tweets_full.json file.
- A <b>hydrated_tweets_short.json</b> which contains a shortened version of the hydrated tweets.
