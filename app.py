# import streamlit as st
# import pandas as pd
# import pickle
# import requests


# def fetch_poster(movie_id):
#    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
#    data = response.json()
#    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
   
# # Function to recommend movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id

#         recommended_movies.append(movies.iloc[i[0]].title)
#         #fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# # Load the movie dictionary
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('Movie Recommender System')

# st.write('Welcome to the Movie Recommender System! We recommend you the following movies:')
# selected_movie_name = st.selectbox(
#     "Which movie do you like best?",
#     movies['title'].values)

# if st.button("Recommend"):
#     names,posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.text(names[0])
#     st.image(posters[0])

# with col2:
#     st.text(names[1])
#     st.image(posters[1])

# with col3:
#     st.text(names[2])
#     st.image(posters[2])

# with col4:
#     st.text(names[3])
#     st.image(posters[3])

# with col5:
#     st.text(names[4])
#     st.image(posters[4])



# import streamlit as st
# import pandas as pd
# import pickle
# import requests

# # Function to fetch movie poster from TMDB API
# def fetch_poster(movie_id):
#     response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

# # Function to recommend movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id

#         recommended_movies.append(movies.iloc[i[0]].title)
#         # Fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))

#     return recommended_movies, recommended_movies_posters

# # Load the movie dictionary
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('🎬 Movie Recommender System')

# st.write('Welcome to the Movie Recommender System! We recommend you the following movies:')
# selected_movie_name = st.selectbox(
#     "Which movie do you like best?",
#     movies['title'].values)

# if st.button("Recommend"):
#     names, posters = recommend(selected_movie_name)

#     # Indent the column layout inside the if condition
#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         st.text(names[0])
#         st.image(posters[0])

#     with col2:
#         st.text(names[1])
#         st.image(posters[1])

#     with col3:
#         st.text(names[2])
#         st.image(posters[2])

#     with col4:
#         st.text(names[3])
#         st.image(posters[3])

#     with col5:
#         st.text(names[4])
#         st.image(posters[4])



import streamlit as st
import pandas as pd
import pickle
import requests
import time  # Importing time module for the spinner delay

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load the movie dictionary
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommendation System')

st.write('Welcome to the Movie Recommendation System! We recommend you the following movies:')
selected_movie_name = st.selectbox(
    "Which movie do you like best?",
    movies['title'].values)

if st.button("Recommend"):
    with st.spinner("🔍 Finding the best movies for you..."):
        time.sleep(5)  # Simulating a loading time
    
    names, posters = recommend(selected_movie_name)

    # Indent the column layout inside the if condition
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    st.success("✅ Movies recommended successfully!")

