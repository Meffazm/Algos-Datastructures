from itertools import chain
import networkx as nx
from collections import Counter


# n - number of movies
# m - number of links
# k - number of friends movies
# f - number of friends


def movie_recommend(movies, links, seen, friends):
    movies_graph = nx.Graph(links)  # O(m)
    movies_graph.add_nodes_from(movies)  # O(n)
    rating = {}  # O(1)
    friends_movies = Counter(chain.from_iterable(friends.values()))  # O(k)

    for movie in movies_graph:  # O(n)
        if movie in seen:  # O(1)
            continue  # O(1)
        similar = nx.node_connected_component(movies_graph, movie)  # O(m)
        similar.discard(movie)  # O(1)
        discussability = friends_movies[movie]  # O(1)
        uniqueness = sum(friends_movies[mov] for mov in similar) / len(friends)  # O(n)
        if uniqueness != 0:  # O(1)
            rating[movie] = discussability / uniqueness  # O(1)
        else:  # O(1)
            rating[movie] = discussability  # O(1)

    return max(rating, key=rating.get)  # O(n)
