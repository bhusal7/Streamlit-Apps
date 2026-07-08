# app.py

import os
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="File Handling App",
    page_icon="📂",
    layout="wide"
)

st.title("📂 File Handling System")
st.write("Create, Read, Update, Rename and Delete files using Streamlit.")

# -----------------------------
# Function to display all files
# -----------------------------
def get_files():
    """Returns all files inside the current directory and subdirectories."""
    path = Path(".")
    return sorted([str(file) for file in path.rglob("*") if file.is_file()])


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Operations")

operation = st.sidebar.radio(
    "Choose an Operation",
    (
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    )
)

st.sidebar.markdown("---")
st.sidebar.subheader("Available Files")

files = get_files()

if files:
    for file in files:
        st.sidebar.write(f"📄 {file}")
else:
    st.sidebar.info("No files found.")


# ===========================================================
# Create File
# ===========================================================
if operation == "Create File":

    st.header("📄 Create New File")

    filename = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        if filename == "":
            st.warning("Please enter a file name.")

        else:
            path = Path(filename)

            if path.exists():
                st.error("File already exists.")

            else:
                try:
                    with open(path, "w", encoding="utf-8") as file:
                        file.write(content)

                    st.success("File created successfully.")

                except Exception as e:
                    st.error(f"Error : {e}")


# ===========================================================
# Read File
# ===========================================================
elif operation == "Read File":

    st.header("📖 Read File")

    if files:

        selected_file = st.selectbox(
            "Select a file",
            files
        )

        if st.button("Read"):

            try:
                with open(selected_file, "r", encoding="utf-8") as file:
                    data = file.read()

                st.success("File read successfully.")
                st.text_area(
                    "File Content",
                    data,
                    height=300
                )

            except Exception as e:
                st.error(f"Error : {e}")

    else:
        st.info("No files available.")


# ===========================================================
# Update File
# ===========================================================
elif operation == "Update File":

    st.header("✏️ Update File")

    if files:

        selected_file = st.selectbox(
            "Select a file",
            files
        )

        update_option = st.radio(
            "Choose Update Type",
            (
                "Rename File",
                "Overwrite Content",
                "Append Content"
            )
        )

        # ---------------- Rename ----------------
        if update_option == "Rename File":

            new_name = st.text_input("New file name")

            if st.button("Rename"):

                if new_name == "":
                    st.warning("Enter a new file name.")

                else:
                    try:
                        Path(selected_file).rename(new_name)
                        st.success("File renamed successfully.")

                    except Exception as e:
                        st.error(f"Error : {e}")

        # ---------------- Overwrite ----------------
        elif update_option == "Overwrite Content":

            new_content = st.text_area("New Content")

            if st.button("Overwrite"):

                try:
                    with open(selected_file, "w", encoding="utf-8") as file:
                        file.write(new_content)

                    st.success("Content overwritten successfully.")

                except Exception as e:
                    st.error(f"Error : {e}")

        # ---------------- Append ----------------
        else:

            append_text = st.text_area("Content to Append")

            if st.button("Append"):

                try:
                    with open(selected_file, "a", encoding="utf-8") as file:
                        file.write("\n" + append_text)

                    st.success("Content appended successfully.")

                except Exception as e:
                    st.error(f"Error : {e}")

    else:
        st.info("No files available.")


# ===========================================================
# Delete File
# ===========================================================
elif operation == "Delete File":

    st.header("🗑️ Delete File")

    if files:

        selected_file = st.selectbox(
            "Select a file to delete",
            files
        )

        st.warning("This action cannot be undone.")

        if st.button("Delete File"):

            try:
                os.remove(selected_file)
                st.success("File deleted successfully.")

            except Exception as e:
                st.error(f"Error : {e}")

    else:
        st.info("No files available.")