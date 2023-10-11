import streamlit as st
import pickle
def recommend(movie):
    index = movies[movies['title'].values == movie].index[0]
    distances = sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])
    recommended_movies=[]
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies = pickle.load(open('movies.pkl','rb'))
sim=pickle.load(open('sim.pkl','rb'))
movie_list = movies['title'].values
st.title('Movie recommendation system')
selected_movie = st.selectbox(
    'How to contact you?', movie_list )
if st.button('Recommendation'):
    rc=recommend(selected_movie)
    for i in rc:
      st.write(i)
