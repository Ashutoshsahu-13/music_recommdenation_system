import pickle
import streamlit as st
from datetime import datetime
import spotipy
from spotipy.oauth2   import SpotifyClientCredentials
client_id='ed7e8cbe42804977bc8c2ce344772bf7'
client_secret='6e423e12e12042af98137b4c2c0af1b1'
client_credentials_manger=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manger)
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
def recommend(song):
    input_song_index = music_df[music_df['Track Name'] == song].index[0]
    similarity_score = list(enumerate(similarity[input_song_index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommended_music_names=[]
    recommended_poster=[]
    for i in similarity_score[1:6]:
        track=music_df["Track Name"].iloc[i[0]]
        artists=music_df["Artists"].iloc[i[0]]
        recommended_poster.append(get_song_album_cover_url(track,artists))
        recommended_music_names.append(music_df['Track Name'].iloc[i[0]])
    return recommended_music_names,recommended_poster


music_df=pickle.load(open('music1.pkl','rb'))
similarity=pickle.load(open('similarity1.pkl','rb'))
st.title('Music Recommendation System')
select_music=st.selectbox('Select any song in below list',(music_df['Track Name'].values))
if st.button('Recommend'):
    recommended_music_names,recommended_music_psoter=recommend(select_music)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.write(recommended_music_names[0])
        st.image(recommended_music_psoter[0])
    with col2:
        st.write(recommended_music_names[1])
        st.image(recommended_music_psoter[1])
    with col3:
        st.write(recommended_music_names[2])
        st.image(recommended_music_psoter[2])

    with col4:
        st.write(recommended_music_names[3])
        st.image(recommended_music_psoter[3])

    with col5:
        st.write(recommended_music_names[4])
        st.image(recommended_music_psoter[4])