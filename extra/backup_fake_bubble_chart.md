#qui
#df_rt = pd.DataFrame(
#    {'Name': names,
#     'Username': usernames,
#     'Account created on': ages,
#     'Type of account': verified,
#     'Followers count': followers,
#     'Friends count': following,
#     'Tweet Retweets count': retweets,
#     'Category': category,
#     'Date':dates
#    })
#df_rt['Date']= pd.to_datetime(df_rt['Date'])

Sotto il grafico
#fig = px.scatter(df_rt, hover_data=['Name','Username','Type of account','Tweet Retweets count','Friends count','Account created on'],
#                 x="Date", y="Tweet Retweets count",
#                 size='Followers count',
#                 color="Category",
#                 color_discrete_sequence=["#1A85FF", "#D41159"],
#                 template="plotly_white",
#                 title="Popularity of Tweets - Fake Covid-19 dataset (Size of the bubbles based on Tweet retweets count)",
#                 labels={"Category": "Type of Tweet"}
#                )

#fig.update_traces(marker=dict(opacity=0.8,line=dict(width=1,
#                              color='DarkSlateGrey')),
#                              selector=dict(mode='markers'))

#fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
#fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, type="log")

#fig.update_yaxes(fixedrange=True)


#fig.show()