# FIX

<h3>In alcune word cloud ci sono caratteri in arabo/cinese o comunque strani che vanno gestiti.</h3>

# TO DO
Word Cloud con immagine su <b>tutte</b> le Word Cloud<br>

Portare le word cloud fatte fin ora anche nella cartella fakecovid e testarle<br>

Grafico numero di tweet per data<br>

Contare le parole più frequenti, hashtag più frequenti, menzioni più frequenti e fare i relativi istogrammi (?)<br>

La visualizzazione della location dei tweet con il campo "location" del JSON non ha senso perchè è un campo user-defined.<br>

Per la cosa degli amici:<br>
<b>followers_count</b> The number of followers this account currently has. <br>
<b>friends_count</b> The number of users this account is following (AKA their “followings”).<br>
<b>verified</b> When true, indicates that the user has a verified account.<br>
<b>statuses_count</b> The number of Tweets (including retweets) issued by the user.

Ulteriormente<br>
<b>retweet_count</b> Number of times this Tweet has been retweeted. <br>
<b>favorite_count</b> Indicates approximately how many times this Tweet has been liked by Twitter users. <br>

<h3>CAMPI JSON SPIEGATI<br>

Tweet:
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet<br>

User:
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user<br>

Entities:
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities
</h3><br>

#NOTE DELLA PROF - Lezione del 12/03

• Fare un Word Cloud delle parole e degli hashtag più frequenti nei fake tweet, anche NON inerenti al Covid.<br>

• Quali sono le parole che maggiormente compaiono insieme in un tweet; ad esempio: hospital + death, homework + children, smartwork + lunch.<br>

• Rispetto alle fake news è interessante capire quali sono gli hashtag che co-occorrono maggiormente, quindi per farlo bisogna:
- andare a visualizzare le parole che occorrono di più (tramite un wordle)
- selezionare solo queste parole e vedere quali di queste co-occorrono, ossia compaiono insieme.<br>

• Si potrebbero contare quali sono gli username più frequenti.<br>