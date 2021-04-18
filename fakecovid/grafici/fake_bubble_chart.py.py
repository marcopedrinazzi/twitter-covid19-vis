import pandas as pd
import json
from dateutil.parser import parse
import plotly.express as px

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index = 0
names= []
usernames = []
followers = []
following = []
ages = []
likes = []
verified = []

for element in data:
    #name
    name = data[index]['user']['name']
    names.append(name)

    #screen_name (username)
    user = data[index]['user']['screen_name']
    usernames.append("@"+user)

    #followers_count
    follower = data[index]['user']['followers_count']
    followers.append(follower)

    #friends_count
    friend = data[index]['user']['friends_count']
    following.append(friend)

    #created_at
    age = data[index]['user']['created_at']
    d = parse(age)
    d = d.strftime('%Y/%m/%d')
    ages.append(d)
    
    #favourites_count
    like = data[index]['user']['favourites_count']
    likes.append(like)

    #verified
    v = data[index]['user']['verified']
    #verified.append(v)
    
    if v:
       verified.append("Verified")
    else:
       verified.append("Not Verified")
    
                        
    index=index+1

df = pd.DataFrame(
    {'Name': names,
     'Username': usernames,
     'Account age': ages,
     'Verified': verified,
     'Followers count': followers,
     'Friends count': following,
     'Likes count': likes
    })
df['Account age']= pd.to_datetime(df['Account age'])


fig = px.scatter(df, hover_data=['Name','Username','Likes count','Friends count'],
                 x="Account age", y="Followers count",
                 size='Likes count',
                 color="Verified",
                 title="Popularity of account - Fake Covid-19 dataset",
                 labels={"Verified": "Type of account"}
                )

fig.update_traces(marker=dict(opacity=0.8,line=dict(width=1,
                              color='DarkSlateGrey')),
                              selector=dict(mode='markers'))

fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)

fig.update_yaxes(fixedrange=True)


fig.show()
