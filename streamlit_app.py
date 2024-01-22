import streamlit as st
import os

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_videos", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except:
        return False

def main():
    st.title('Video Upload App')

    # Maak een directory als deze nog niet bestaat
    if not os.path.exists('uploaded_videos'):
        os.makedirs('uploaded_videos')

    uploaded_file = st.file_uploader("Kies een videobestand", type=['mp4', 'avi', 'mov', 'mkv'])

    if uploaded_file is not None:
        result = save_uploaded_file(uploaded_file)
        if result:
            st.success('Video succesvol geüpload.')
        else:
            st.error('Fout bij het uploaden van de video.')

if __name__ == "__main__":
    main()
