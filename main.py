# Sample data: User preferences for movies (Movie: [User1, User2, User3])
user_movie_preferences = {
    'Movie1': [5, 4, 0],
    'Movie2': [0, 5, 3],
    'Movie3': [4, 0, 5],
    'Movie4': [3, 2, 4],
    'Movie5': [0, 4, 0]
}

# Sample user preferences
user_preferences = {
    'User1': {'Movie1': 5, 'Movie2': 4, 'Movie3': 3, 'Movie4': 2},
    'User2': {'Movie1': 4, 'Movie2': 5, 'Movie3': 2, 'Movie4': 1},
    'User3': {'Movie1': 3, 'Movie2': 2, 'Movie3': 5, 'Movie4': 4}
}

# Function to recommend movies to a user based on collaborative filtering
def recommend_movies(user, preferences, similarity_threshold=0.5):
    user_preferences = preferences[user]
    recommendations = {}

    for movie, rating in user_preferences.items():
        for other_user, other_preferences in preferences.items():
            if other_user != user and movie in other_preferences and other_preferences[movie] > 0:
                similarity = sum(user_preferences[m] * other_preferences[m] for m in user_preferences) / \
                             (sum(user_preferences[m] ** 2 for m in user_preferences) ** 0.5 *
                              sum(other_preferences[m] ** 2 for m in other_preferences) ** 0.5)

                if similarity > similarity_threshold:
                    if movie not in recommendations:
                        recommendations[movie] = 0
                    recommendations[movie] += similarity * other_preferences[movie]

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in sorted_recommendations]

# Get movie recommendations for a user
user_to_recommend = 'User1'
recommended_movies = recommend_movies(user_to_recommend, user_preferences)

print(f"Recommended movies for {user_to_recommend}: {recommended_movies}")
