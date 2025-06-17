import streamlit as st
from create_embeddings import embed_query 
from pinecone_util import query_pinecone
from card_types import color_values, card_classes, formats_classes

st.set_page_config(page_title="MTG Card Search", layout="wide")

st.title("Magic: The Gathering Card Similarity")
st.markdown("Enter a card description or effect and find similar Magic cards.")

user_query = st.text_input("Describe a card or effect:", placeholder="e.g. Draw two cards")
color_filter = st.multiselect("Color", list(color_values.values()))
card_class = st.multiselect("Type", list(card_classes.values()))
formats_class = st.multiselect("Format", list(formats_classes.values()))

if user_query:
    with st.spinner("Searching..."):
        selected_color_codes = [key for key, value in color_values.items() if value in color_filter]
        selected_card_classes = [key for key, value in card_classes.items() if value in card_class]
        selected_formats = [key for key, value in formats_classes.items() if value in formats_class]

        filter = {
            "color_identity": selected_color_codes,
            "type_line": selected_card_classes,
            "legalities": selected_formats,
            #"mana_cost": mana_filter,
            #"type": card_type_filter
        }

        print(filter["color_identity"])

        embedding = embed_query(user_query)
        results = query_pinecone(embedding, top_k=30, filter=filter)

        print(results)

    st.subheader("Similar Cards")
    
    with st.container():
        cols = st.columns([1, 1, 1])  # display 3 columns with equal width
        for i, item in enumerate(results):
            with cols[i % 3]:  # cycle through the columns
                name = item["metadata"].get("name", "Unknown Card")
                text = item["metadata"].get("text", "")
                image_url = item["metadata"].get("image", "")
                score = item["score"]

                st.markdown(f"### {name} (Score: {score:.3f})")
                if image_url:
                    st.image(image_url, width=200)
                # st.write(text)