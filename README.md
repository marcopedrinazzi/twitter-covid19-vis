# Twitter Covid19 Visualisation

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104.

The dataset that we've used is composed by one column: <b>tweet_id</b>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/DocNow/twarc <br>
We've executed the following command to get the needed results:<br>

<code> twarc --tweet_mode extended hydrate general_dataset.csv > general_result.json
</code>
<br>

The <i>general_result.json</i> file isn't available online due to the limits of GitHub on big files.

<b>Parsing</b><br>

We've done the JSON parsing using the tools from https://github.com/thepanacealab/SMMT/tree/master/data_preprocessing.<br>
We've used <i>parse_json_lite.py</i> and <i>fields.py</i>, we have downloaded them using the following commands:<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/parse_json_lite.py -O parse_json_lite.py</code>
<br>

<code>wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/fields.py -O fields.py</code>
<br>

The parsing is done executing this command:<br>
<code>python3 parse_json_lite.py filename.json</code><br>

This utility takes two arguments. The first argument is the json file. The second argument is optional. If the second argument is given, it will preprocess the json file. The preprocessing includes removal of URLs, twitter specific Urls, Emojis, Emoticons.
Note: For the preprocessing to work, the second argument must be p

<code>python3 parse_json_lite.py filename.json p</code><br>

What fields do you want to extrat from your Tweet json?

By default the parse will extract all fields. It's possible limit to the only ones required want by editing the <b>fields.py</b> file and only leaving the selected ones.
<br>
All the fields available can be found at https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet

The parsing process produces a .tsv file with the results.


<h2>Visualisation about Covid19 Misinformation on Twitter</h2>

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19 <br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104.<br>

The dataset that we've used is composed by two columns: <b>tweet_id</b> and <b>tweet_class</b><br>

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/DocNow/twarc. In this case we've produced a one version column of the dataset with only the <b>tweet_id</b> to complete the hydratation.
We've executed the following command to get the needed results:<br>

<code> twarc --tweet_mode extended hydrate fakecovid_dataset_one_column.csv > fakecovid_result.json
</code>
<br>