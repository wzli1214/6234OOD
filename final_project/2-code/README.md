### User case
1. Login/Logout/Signup
2. search movies based on the title / actors
3. See the trailers / reviews
3. Post an watching event
4. Voting



### Database:

Use two SQLite database:

1. movies database, contains 3000+ movies
https://www.kaggle.com/oxanozaep/imdb-eda/data

2. a SQLite database use for managing the post and voting.


### Search Engine and Cache
Search Index: Built an inverted index structure with wildcard to enable vague search.
Rank: Movie search results are sorted by rating, while actor search results are sorted by the number of movies acted.
Cache: Implemented a LRU Cache to record search result to make search suggestion faster.



### Recommender
An item-based recommender is implemented.

According to movies in user's movie list, movies with same genres will be recommended for each user. If user's movie list is empty or the number of movies to recommend is not sufficient, movies with highest ratings will be recommended instead.

The final recommendation is randomly chosen from a set of candidate movies, so the result will be slightly different each time.