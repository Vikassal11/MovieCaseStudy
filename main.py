import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

movies = pd.read_csv('/Users/payalsagwal/Desktop/moviedata.csv')
movies.info()
print(movies)

movies["title_year"] = movies["title_year"] * 1
movies["gross"] = movies["gross"] / 1000000

movies["budget"] = movies["budget"] / 1000000
movies["profit"] = movies["gross"] - movies["budget"]
# print (m["budget"],m["profit"])

movies.sort_values(by="profit", ascending=False)
plt.ylabel(movies["profit"])
plt.xlabel(movies["title_year"])

plt.scatter(movies["budget"], movies["profit"])
plt.legend(['budget', 'profit'])
plt.show()

# movies.columns
# movies.iloc[:10, :]
# movies[movies["profit"] < 0]

movies["MetaCritic"] = movies["MetaCritic"] / 10
movies["Avg_rating"] = (movies["IMDb_rating"] + movies["MetaCritic"]) / 2

df = movies[["Title", "IMDb_rating", "MetaCritic", "Avg_rating"]]
df = df.loc[abs(df["IMDb_rating"] - df["MetaCritic"] < 0.5)]
# movies[co.metaCritic] = movies["MetaCritic"] / 10
# movies[co.avgRating] = (movies["IMDb_rating"] + movies["MetaCritic"]) / 2
# print(movies)
# df=movies[["Title", "IMDb_rating", "MetaCritic", "Avg_rating"]]
# dg = df.loc[abs(df["IMDb_rating"]-df["MetaCritic"])<0.5]
# print(dg)
#
# df = df.sort_values(by="Avg_rating",ascending=False)
# UniversalAcclaim=df.loc[df["Avg_rating"]>=8]
# print(UniversalAcclaim)
# group = movies.pivot_table(values=["actor_1_facebook_likes", "actor_2_facebook_likes", "actor_3_facebook_likes"], aggfunc="sum", index=["actor_1_name", "actor_2_name", "actor_3_name"])
#
# group["totalLikes"] = group["actor_1_facebook_likes"]+group["actor_2_facebook_likes"]+group["actor_3_facebook_likes"]
# group.sort_values(by="totalLikes",ascending=False,inplace=True)
# group = group.iloc[0:5,:]
# print(group)
# Demographic Analysis
# Create the dataframe df_by_genre
df_by_genre = movies.loc[:, "CVotes10":"VotesnUS"]
df_by_genre[["genre_1", "genre_2", "genre_3"]] = movies[["genre_1", "genre_2", "genre_3"]]
# print(df_by_genre)

# Create a column cnt and initialize it to 1
df_by_genre["cnt"] = 1
df_by_genre[["genre_1", "genre_2", "genre_3"]]
# print(df_by_genre)

# Group the movies by individual genres
df_by_g1 = df_by_genre.groupby("genre_1").aggregate(np.sum)
df_by_g2 = df_by_genre.groupby("genre_2").aggregate(np.sum)
df_by_g3 = df_by_genre.groupby("genre_3").aggregate(np.sum)
#
# print(df_by_g1)
# print(df_by_g2)
# print(df_by_g3)
#
# Add the grouped data frames and store it in a new data frame
df_add = df_by_g1.add(df_by_g2, fill_value=0)
df_add = df_add.add(df_by_g3, fill_value=0)
# print(df_add)
#
# Extract genres with atleast 10 occurences
genre_top_10 = df_add.loc[df_add["cnt"] > 10]
#
# print(genre_top_10)
#
# Take the mean for every column by dividing with cnt
# genre_top_10.iloc[:,0:-1]=genre_top_10.iloc[:,0:-1].divide(genre_top_10["cnt"],axis=0)
#
# print(genre_top_10)
#
# Converting CVotes to int type
# genre_top_10[genre_top_10.loc[:,"CVotes10":"CVotesnUS"].columns]=genre_top_10[genre_top_10.loc[:,"CVotes10":"CVotesnUS"].columns].astype(int)
#
# print(genre_top_10)
#
# Countplot for genres
# plt.plot(x=genre_top_10["cnt"],y=genre_top_10.index)
# plt.show()
#
# 1st set of heat maps for CVotes-related columns
# plt.figure(figsize=(20,10))
# plt.subplot(1,2,1)
# ax=sns.heatmap(genre_top_10[["CVotesU18M","CVotes1829M","CVotes3044M","CVotes45AM"]],annot=True,cmap="coolwarm")
# plt.subplot(1,2,2)
# plt.show()
#
# ax=sns.heatmap(genre_top_10[["CVotesU18F","CVotes1829F","CVotes3044F","CVotes45AF"]],annot=True,cmap="coolwarm")
# plt.show()
#
# R-rated movies
movies.loc[movies["content_rating"] == "R"].sort_values(by="CVotesU18", ascending=False)[["Title", "CVotesU18"]].head(
    10)
print(movies)
