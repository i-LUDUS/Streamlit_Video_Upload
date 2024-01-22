import streamlit as st
import os
import shutil

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_videos", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except:
        return False

def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def main():
    st.title('Video Upload en Beheer App')

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

    # Lijst van geüploade bestanden
    st.subheader("Beschikbare Video's")
    for filename in list_files("uploaded_videos"):
        with st.container():
            st.write(filename)
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f'Afspelen {filename}'):
                    st.video(os.path.join("uploaded_videos", filename))
            with col2:
                if st.button(f'Verwijderen {filename}'):
                    os.remove(os.path.join("uploaded_videos", filename))
                    st.experimental_rerun()

if __name__ == "__main__":
    main()
