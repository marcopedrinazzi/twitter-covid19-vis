# TODO

<h2>LEXICAL DISPERSION PLOT - Fake: HA SENSO? ALTERNATIVE? </h2>

<h2>!!! NELLE FAKE NEWS VA LETTO IL CSV E IN QUALCHE MANIERA CATALOGATO COSA è PARTIALLY FALSE o FALSE !!!</h2><br>

<h2>@marco classified da aggiungere ai vari notebook - Mancano Fake Text e Fake Bigrams-Trigrams</h2>

# FIX

<h3>IL GEN FROM FREQ IGNORA LE STOPWORDS E ALTRE COSE. VEDI RIFERIMENTO LIBRERIA</h3><br>

<h3>https://altair-viz.github.io/gallery/index.html</h3>

**NB per la presentazione https://personal.sron.nl/~pault/ (sezione color blind) e https://davidmathlogic.com/colorblind/#%23332288-%23117733-%2344AA99-%2388CCEE-%23DDCC77-%23CC6677-%23AA4499-%23882255**

# IDEE
**Lista Colori**:
- '#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677','#AA3377', '#BBBBBB' **bright** (sito Paul Tol)
- '#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77','#CC6677', '#AA4499', '#882255' **sito davidmathloic Tol, è simile a Muted**
- High-contrast (da scartare per l'uso del bianco)
- '#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311','#EE3377', '#BBBBBB' **Vibrant** 
- '#332288', '#88CCEE', '#44AA99', '#117733', '#999933','#DDCC77', '#CC6677','#882255','#AA4499' **Muted**
- Medium-contrast (da scartare per l'uso del bianco)

<h3>- Adattare i colori di **TUTTI** i grafici con https://davidmathlogic.com/colorblind/

**Fatti:**
- Fake classified Hashtag
- Fake hashtag Word Cloud</h3>

• <b>ASSOLUTAMENTE DA COMPARARE I DUE DATASET</b>

- Tabella 2 pagina 9 paper. ***C'è il CSV in gitub*** **Si può fare altro oltre alle tabelle nei buuble chart?**

<b>- https://jasonkessler.github.io/demo_compact.html Scatter Text per Hashtag, Testo, Emoji confrontando i due dataset. Asse x frequenza su dataset general, asse y frequenza su dataset fake</b>

https://usc-melady.github.io/COVID-19-Tweet-Analysis/misinfo.html, https://storybench.shinyapps.io/covid-tweets/, https://mykabir.github.io/coronavis/, https://arxiv.org/abs/2005.05710

• Da dove provengono i vari tweet (già discusso che si può vedere per qualcosa di semplice alla fine) <br>

• Brand and non-brand accounts oppure verified → TwiRole library (https://github.com/liuqingli/TwiRole - <code>user_classifier.py</code>)
<br>

• Sentiment analysis (data su asse x e sentiment score su asse y) -> relativo magari ai top hashtag #coronavirus, ecc

• Grafo usando in_reply_to_user_id (suddividendolo anche per categoria magari) e anche quoted_status_id

• Line chart popolurarity of words

• Bot analysis https://github.com/IUNetSci/botometer-python https://botometer.osome.iu.edu

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
