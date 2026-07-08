

import streamlit as st
import json
import os

file_path = "youtube.txt"

def load_data():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_data_helper(videos):
    with open(file_path, "w") as file:
        json.dump(videos, file, indent=2)

def list_all_videos(videos):
    st.markdown('<div style="margin-top:20px">', unsafe_allow_html=True)
    if not videos:
        st.info("No videos found.")
        return
    for i, video in enumerate(videos, start=1):
        video_name = video.get('Video Name', 'Unnamed Video')
        duration = video.get('duration', 'Unknown Duration')
        st.markdown(f"""
        <div style="background-color:#121212;padding:20px;border-radius:12px;margin-bottom:10px;border:1px solid #2c2c2c;">
            <h4 style="color:#e50914;font-weight:bold;">{i}. {video_name}</h4>
            <p style="color:#f5f5f5;">⏱ Duration: {duration}</p>
        </div>
        """, unsafe_allow_html=True)

def add_video(videos):
    st.markdown("<h3 style='color:#e50914;'>➕ Add New Video</h3>", unsafe_allow_html=True)
    with st.form("add_video"):
        name = st.text_input("Video Name")
        duration = st.text_input("Duration (e.g. 10 min)")
        submitted = st.form_submit_button("Add")
        if submitted:
            videos.append({"Video Name": name, "duration": duration})
            save_data_helper(videos)
            st.success("✅ Video added successfully!")

def update_video(videos):
    st.markdown("<h3 style='color:#f5c518;'>✏️ Update Video</h3>", unsafe_allow_html=True)
    if not videos:
        st.warning("No videos available to update.")
        return
    index = st.selectbox("Choose video to update", range(len(videos)), format_func=lambda i: videos[i].get("Video Name", f"Unnamed {i+1}"))
    new_name = st.text_input("New Video Name", value=videos[index].get("Video Name", ""))
    new_duration = st.text_input("New Duration", value=videos[index].get("duration", ""))
    if st.button("Update"):
        videos[index] = {"Video Name": new_name, "duration": new_duration}
        save_data_helper(videos)
        st.success("✅ Video updated!")

def delete_video(videos):
    st.markdown("<h3 style='color:#f5c518;'>🗑️ Delete Video</h3>", unsafe_allow_html=True)
    if not videos:
        st.warning("No videos to delete.")
        return
    index = st.selectbox("Choose video to delete", range(len(videos)), format_func=lambda i: videos[i].get("Video Name", f"Unnamed {i+1}"))
    if st.button("Delete"):
        deleted = videos.pop(index)
        save_data_helper(videos)
        st.success(f"🗑️ Deleted video: {deleted.get('Video Name', 'Unnamed Video')}")

def main():
    st.set_page_config(page_title="Netflix/Amazon Style Video Manager", layout="centered")
    st.markdown("""
        <style>
        body { background-color: #000000; color: #ffffff; }
        .sidebar .sidebar-content { background-color: #111; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color:#e50914; font-family: sans-serif;'>🎬 MyStream Video Manager</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border:1px solid #333;'>", unsafe_allow_html=True)

    videos = load_data()
    menu = ["🎥 Show Videos", "➕ Add", "✏️ Update", "🗑️ Delete"]
    choice = st.sidebar.radio("Navigation", menu)

    if choice == "🎥 Show Videos":
        list_all_videos(videos)
    elif choice == "➕ Add":
        add_video(videos)
    elif choice == "✏️ Update":
        update_video(videos)
    elif choice == "🗑️ Delete":
        delete_video(videos)

if __name__ == "__main__":
    main()
