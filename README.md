# TODO
<h2>!!!!!!NELLE FAKE NEWS VA LETTO IL CSV E IN QUALCHE MANIERA CATALOGATO COSA è PARTIALLY FALSE O FALSE !!!!</h2><br>

<h2>TENERE AGGIORNATI I NOTEBOOK</h2>

# FIX
<h3>IL GEN FROM FREQ IGNORA LE STOPWORDS E ALTRE COSE. VEDI RIFERIMENTO LIBRERIA</h3><br>
<h3>DA APPRODONFIRE: Filtrare per lingua if(data[index]lang==.......) then ==> filtro else scarto. Lo script per la lingua <i>lang.py</i> utile comunque da presentare e quindi va tenuto</h3>
<h4>bigrams e trigrams da controllare bene. Ci sono alcuni risultati che non mi aspetto. altra punteggiatura non permette di riconoscere le parole, da capire.</h4>

# Twitter Covid19 Visualisation

<b>Authors</b>: Simona Guida, Marco Pedrinazzi

Data from: https://github.com/Gautamshahi/Misinformation_COVID-19<br>
The dataset comes from this research work: Shahi, G. K., Dirkson, A., & Majchrzak, T. A. (2021). An exploratory study of covid-19 misinformation on twitter. Online social networks and media, 100104. https://arxiv.org/abs/2005.05710<br>

The dataset that we've used is composed by one column: <b>tweet_id</b>

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

We've done the hydratation (to get complete details (i.e. fields) of a tweet from its ID) thanks to this tool https://github.com/DocNow/twarc. In this case we've produced a one version column of the dataset with only the <b>tweet_id</b> to complete the hydratation.
We've executed the following command to get the needed results:<br>

<code> twarc --tweet_mode extended hydrate fakecovid_dataset_one_column.csv > fakecovid_result.json
</code><br>

Afte the hydratation, we've found some tweets which weren't about COVID19, so we've deleted them from <i>fakecovid_result.json</i>. We've removed the following tweets:<br>

1027222566581231617		(2018)<br>
1179751464215949313		(2019)<br>
539901552937664513		(2014)<br>
539914412401123328		(2014)<br>
1025660196218183680		(2018)<br>
1088739576687091712		(2019)<br>
1088800362847526913		(2019)<br>
1101094162865242113		(2019)<br>
1156661710247403523		(2019)<br>
1169318930156007425		(2019)<br>
1171793133690150919     (2019)<br>
1185034497521340416		(2019)<br>
1201776606706118656		(2019)<br>
900683060915523584		(2017)<br>
1015698605720686593		(2018)<br>
1126068077999853568		(2019)<br>
1165696327558344704		(2019)<br>
1181970325757517825		(2019)<br>
1184483676924436480		(2019)<br>
1188412233270714368		(2019)<br>
1200150134203568128		(2019)<br>
725937576532578304		(2016)<br>
900685413416751104		(2017)<br>
1132002388376788995		(2019)<br>
1134145939151740929		(2019)<br>
1167029938635100161		(2019)<br>
720102224605638656		(2016)<br>
903686853508857859		(2017)<br>
962814691415347200		(2018)<br>
995638432318738432		(2018)<br>
1014931242842775558		(2018)<br>
1023850585949274112		(2018)<br>
1023860881929711616		(2018)<br>
1053169444690763776		(2018)<br>
1105241563620360193		(2019)<br>
1117789925527773184		(2019)<br>
1153706403565117440		(2019)<br>
1153708733882601472		(2019)<br>
673699231098527744		(2015)<br>
827283890146463750		(2017)<br>
940623615615266822		(2017)<br>
971254280601694209		(2018)<br>
1105214769563402241		(2019)<br>
1105393223462207488		(2019)<br>
1105668048416108544		(2019)<br>
1172772374074118145		(2019)<br>
1172789409478922241		(2019)<br>
1176858065242660865		(2019)<br>
1209402080273809408		(2019)<br>
481020774195552256		(2014)<br>
899910766064750592		(2017)<br>
1097754735656951808		(2019)<br>
1105282184414416898		(2019)<br>
1150852667301912578		(2019)<br>
1068140903917858816		(2018)<br>
1184254666315456512		(2019)<br>
587827070077571072		(2015)<br>
1018297937720414208		(2018)<br>
1043078112010031104		(2018)<br>
957147456596213760		(2018)<br>
999352051829297153		(2018)<br>
1052255689563721729		(2018)<br>
1068212767897858049		(2018)<br>
1068277017999826944		(2018)<br>
1177110421758795777		(2019)<br>
1197668564137906176		(2019)<br>
1154784135447220224		(2019)<br>
515407029498679298		(2014)<br>
551629973195218946		(2015)<br>
580828044027424768		(2015)<br>
593080368430911488		(2015)<br>
934640524832645120		(2017)<br>
963112422822285312		(2018)<br>
1075785713914929152		(2018)<br>
1186606201259343873		(2019)<br>
615979734988681216		(2015)<br>
719965429175820288		(2016)<br>
933795562947796992		(2017)<br>
934535302642679808		(2017)<br>
997447899465297923		(2018)<br>
1167826809355792390		(2019)<br>
1184857295676674048		(2019)<br>
1206404759575506944		(2019)<br>
563148469796216833		(2015)<br>
951117592843956224		(2018)<br>
1200463040224718848		(2019)<br>
513491003462795264		(2014)<br>
1006592956059484160		(2018)<br>
1078854747086450689		(2018)<br>
1207528337180020736		(2019)<br>
1003387827395186688		(2018)<br>
<br>

<b>Parsing</b><br>

The parsing is done through some Python code on each file.
