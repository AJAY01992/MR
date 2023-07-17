import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url=("https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id))
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYmFlNDQ5OWE5NTQyY2ViYjNhNGFhZWFiMGI4MjJlMSIsInN1YiI6IjY0OTljNDhkNmY0M2VjMDBhYzNjMjhmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o9NEBBo4Z_pC2xMY6mqOzTapQtCZcJR1pQK6CGqbO4w"
    }
    response = requests.get(url, headers=headers)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+ data['poster_path']



def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[ movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    
    recommend_movies=[]
    recommend_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_Movie_name= st.selectbox(
    'How would you like to be contacted?',
     movies['title'].values)

if st.button('Recommend'):
    recommend_movies,recommend_movies_posters=recommend(selected_Movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movies[0])
        st.image(recommend_movies_posters[0])
    with col2:
        st.text(recommend_movies[1])
        st.image(recommend_movies_posters[1])
    with col3:
        st.text(recommend_movies[2])
        st.image(recommend_movies_posters[2])
    with col4:
        st.text(recommend_movies[3])
        st.image(recommend_movies_posters[3])
    with col5:
        st.text(recommend_movies[4])
        st.image(recommend_movies_posters[4])



