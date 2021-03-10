# Twitter Covid19 Visualisation

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104.

The dataset that we've used is composed by one column: <b>tweet_id</b>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/thepanacealab/SMMT. <br>
We're interested in <i>get_metadata.py</i>, which we have downloaded using the following command:<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_acquisition/get_metadata.py -O get_metadata.py</code>
<br>

Then we just have to execute in the terminal:<br>

<code>python3 get_metadata.py -i input.tsv -o hydrated_tweets -k api_keys.json</code><br>

where api_keys.json contains the Twitter API Keys and Tokens in a JSON format.
<br>

The command above returns the following files:
- A <b>hydrated_tweets.json</b> file which contains the full json object for each of the hydrated tweets
- A <b>hydrated_tweets.csv</b> file which contains partial fields extracted from the tweets.
- A <b>hydrated_tweets.zip</b> file which contains a zipped version of the tweets_full.json file.
- A <b>hydrated_tweets_short.json</b> which contains a shortened version of the hydrated tweets.
<br>

We've changed the file names to:
- A <b>general_hydrated.json</b> file which contains the full json object for each of the hydrated tweets
- A <b>general_hydrated.csv</b> file which contains partial fields extracted from the tweets.
- A <b>general_hydrated.zip</b> file which contains a zipped version of the tweets_full.json file.
- A <b>general_hydrated_short.json</b> which contains a shortened version of the hydrated tweets.
<br>

<b>Parsing</b><br>

We've done the JSON parsing using the tools from https://github.com/thepanacealab/SMMT/tree/master/data_preprocessing.<br>
We've used <i>parse_json_lite.py</i> and <i>fields.py</i>, we have downloaded them using the following commands:<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/parse_json_lite.py -O parse_json_lite.py</code>
<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/fields.py -O fields.py</code>
<br>

The parsing is done executing this command:<br>
<code>python parse_json_lite.py filename.json</code><br>

This utility takes two arguments. The first argument is the json file. The second argument is optional. If the second argument is given, it will preprocess the json file. The preprocessing includes removal of URLs, twitter specific Urls, Emojis, Emoticons.
Note: For the preprocessing to work, the second argument must be p

<code>python parse_json_lite.py filename.json p</code><br>

What fields do you want to extrat from your Tweet json?

By default the parse will extract all fields. It's possible limit to the only ones required want by editing the <b>fields.py</b> file and only leaving the selected ones.
<br>
All the fields available can be found at https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet



<h2>Visualisation about Covid19 Misinformation on Twitter</h2>

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 <br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104.<br>

The dataset that we've used is composed by two columns: <b>tweet_id</b> and <b>tweet_class</b><br>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/thepanacealab/SMMT in the same way as explained above. <br>

We've changed the file names returned by the hydratation process in:
- A <b>fakecovid_hydrated.json</b> file which contains the full json object for each of the hydrated tweets
- A <b>fakecovid_hydrated.csv</b> file which contains partial fields extracted from the tweets.
- A <b>fakecovid_hydrated.zip</b> file which contains a zipped version of the tweets_full.json file.
- A <b>fakecovid_hydrated_short.json</b> which contains a shortened version of the hydrated tweets.