'''
Code by Pyry Pohjanoksa
'''

import streamlit as st
import os

st.set_page_config(layout="wide")

image_folder = "./images"

images = os.listdir(image_folder)
trees = [image.split(".")[0] for image in images]

st.title("Carbon sequestration planner")
st.write("")

text_col_1, text_col_2 = st.columns(spec=[2.2,3])

with text_col_1:
    st.write("This is a visualization tool to determine the most efficient locations to plant trees for carbon sequestration (i.e. capturing carbon from the atmosphere). The tool uses land cover data, soil data and temperature data to determine potential locations for new carbon sinks.")
    st.write("The brightness of image pixels indicate the carbon capture potential in that area for the selected tree species. We use an index to estimate the sequestration potential. Dark pixels indicate high potential. The map uses the EPSG:3386 projection. For more technical details go to the slides.")
    st.write("This platform is demoed for the Finland region. It can be expanded to other regions around the globe.")
    st.link_button("See the slides", "https://docs.google.com/presentation/d/1hxc4hNrIjpkBPzDgIy5G75mM75H-B_y82ZKY6XuH5vc/edit?usp=sharing")

st.write("---")
st.subheader("Carbon capture potential by tree species mapped")

col1, col2 = st.columns(spec=[2,1], vertical_alignment="center")

with col2:
    selected_tree = st.radio(label="Available maps", options=trees)

with col1:
    st.image(f"{image_folder}/{selected_tree}.png", 
            use_container_width="always",
        #  width=1500
            )