# TODO

<h2>TODO tabella general url</h2>

<h2>!!!!!!NELLE FAKE NEWS VA LETTO IL CSV E IN QUALCHE MANIERA CATALOGATO COSA è PARTIALLY FALSE O FALSE !!!!</h2><br>

<h2>LEXICAL DISPERSION PLOT - General: mentions, text, bigrams, trigrams (tutte top 5)</h2>

<h2>LEXICAL DISPERSION PLOT - Fake</h2>

<h2>https://altair-viz.github.io/gallery/index.html#</h2>

<h2>@marco classified da aggiungere ai vari notebook - Mancano Fake Text e Fake Bigrams-Trigrams</h2>

<h2>@marco colori nelle word cloud. Da capire</h2>

# FIX
<h3>IL GEN FROM FREQ IGNORA LE STOPWORDS E ALTRE COSE. VEDI RIFERIMENTO LIBRERIA</h3><br>

# IDEE

<b>- https://jasonkessler.github.io/demo_compact.html Scatter Text per Hashtag, Testo, Emoji confrontando i due dataset. Asse x frequenza su dataset general, asse y frequenza su dataset fake</b>

https://usc-melady.github.io/COVID-19-Tweet-Analysis/misinfo.html, https://storybench.shinyapps.io/covid-tweets/, https://mykabir.github.io/coronavis/, https://arxiv.org/abs/2005.05710

• Dalla sezione "Top domains": https://storybench.shinyapps.io/covid-tweets/ 
Tabella con link nei tweet e relativo verified e non verified account che ha riportato il link nel tweet, e nelle due colonne si può fare un data bar che mostra la frequenza di quante volte è stato inserito quel link. <br>

• Da dove provengono i vari tweet (già discusso che si può vedere per qualcosa di semplice alla fine) <br>

• Brand and non-brand accounts oppure verified → TwiRole library (https://github.com/liuqingli/TwiRole - <code>user_classifier.py</code>)
<br>

• <strike>Frequenza retweet differenziando per categoria false, partially… <strike> (è già contenuto in Fig.6 p.11) <br>

• <strike>Scatter text delle emoji più utilizzate dagli account verified e non <strike> (c'è già la 1° idea)<br>

• Sentiment analysis (data su asse x e sentiment score su asse y) -> relativo magari ai top hashtag #coronavirus, ecc

• Grafo usando in_reply_to_user_id (suddividendolo anche per categoria magari) e anche quoted_status_id

• Line chart popolurarity of words

• Bot analysis https://github.com/IUNetSci/botometer-python https://botometer.osome.iu.edu

• Popularity of account: Favourites count, follower count, account age (created_at nell'account) and verified status

• <b>ASSOLUTAMENTE DA COMPARARE I DUE DATASET</b>

• <b>NB figura 6 pagina 11</b>The diffusion of misinformation tweets can be analysed in terms of likes and retweet [78]. Likes indicate how many times a user clicked the tweet as a favourite while retweet is when a user retweets a tweet or retweet with comment. We have visualised the number of likes and retweet gained by each misinformation tweet with the timeline. There is con- siderable variance in the count of retweet and likes, so we decided to normalise the data. We normalise the count of likes and retweet using Min-Max Normalization in the scale of [0, 1]. We normalised the count of retweet and likes for the overall month together and plotted the normalised count of retweet and liked for both false and partially false and plot- ted it for each month. In <b>Figure 6 (p. 11)</b>, we presented our result from January to July 2020, one plot for each month. The blue colour indicates the retweet of the false category, whereas orange colour indicates the retweet of the partially false category. Similarly, the green colour shows the likes of the false category, whereas red colour shows the likes of the partially false category. <b>Vedi pagina 11</b>

• Sezione 5.3.3 Paper -> https://altair-viz.github.io/gallery/grouped_bar_chart_with_error_bars.html

<br>

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

Afte the hydratation, we've found some tweets which weren't about COVID19, so we've deleted them from <i>fakecovid_result.json</i>. We've removed the following tweets:<br>

tweet_ID | year
---|-----
1027222566581231617 | 2018 
1179751464215949313 | 2019 
539901552937664513 | 2014 
539914412401123328 | 2014
1025660196218183680 | 2018 
1088739576687091712 | 2019 
1088800362847526913 | 2019 
1101094162865242113 | 2019 
1156661710247403523 | 2019
1169318930156007425 | 2019
1171793133690150919 | 2019
1185034497521340416 | 2019
1201776606706118656 | 2019
900683060915523584 | 2017
1015698605720686593 | 2018
1126068077999853568 | 2019
1165696327558344704 | 2019
1181970325757517825 | 2019
1184483676924436480 | 2019
1188412233270714368 | 2019
1200150134203568128 | 2019
725937576532578304 | 2016
900685413416751104 | 2017
1132002388376788995 | 2019
1134145939151740929 | 2019
1167029938635100161 | 2019
720102224605638656 | 2016
903686853508857859 | 2017
962814691415347200 | 2018
995638432318738432 | 2018
1014931242842775558 | 2018
1023850585949274112 | 2018
1023860881929711616 | 2018
1053169444690763776 | 2018
1105241563620360193 | 2019
1117789925527773184 | 2019
1153706403565117440 | 2019
1153708733882601472 | 2019
673699231098527744 | 2015
827283890146463750 | 2017
940623615615266822 | 2017
971254280601694209 | 2018
1105214769563402241 | 2019
1105393223462207488 | 2019
1105668048416108544 | 2019
1172772374074118145 | 2019
1172789409478922241 | 2019
1176858065242660865 | 2019
1209402080273809408 | 2019
481020774195552256 | 2014
899910766064750592 | 2017
1097754735656951808 | 2019
1105282184414416898 | 2019
1150852667301912578 | 2019
1068140903917858816 | 2018
1184254666315456512 | 2019
587827070077571072 | 2015
1018297937720414208 | 2018
1043078112010031104 | 2018
957147456596213760 | 2018
999352051829297153 | 2018
1052255689563721729 | 2018
1068212767897858049 | 2018
1068277017999826944 | 2018
1177110421758795777 | 2019
1197668564137906176 | 2019
1154784135447220224 | 2019
515407029498679298 | 2014
551629973195218946 | 2015
580828044027424768 | 2015
593080368430911488 | 2015
934640524832645120 | 2017
963112422822285312 | 2018
1075785713914929152 | 2018
1186606201259343873 | 2019
615979734988681216 | 2015
719965429175820288 | 2016
933795562947796992 | 2017
934535302642679808 | 2017
997447899465297923 | 2018
1167826809355792390 | 2019
1184857295676674048 | 2019
1206404759575506944 | 2019
563148469796216833 | 2015
951117592843956224 | 2018
1200463040224718848 | 2019
513491003462795264 | 2014
1006592956059484160 | 2018
1078854747086450689 | 2018
1207528337180020736 | 2019
1003387827395186688 | 2018
<br>

<b>Parsing</b><br>

The parsing is done through some Python code on each file.
