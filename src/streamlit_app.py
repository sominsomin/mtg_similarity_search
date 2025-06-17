import streamlit as st
from create_embeddings import embed_query 
from pinecone_util import query_pinecone

st.set_page_config(page_title="MTG Card Search", layout="wide")

st.title("Magic: The Gathering Card Similarity")
st.markdown("Enter a card description or effect and find similar Magic cards.")

color_values = {
    "G": "Green",
    "R": "Red",
    "W": "White",
    "B": "Black",
    "U": "Blue"
}
mana_options = [1, 2, 3, 4, 5]
card_type_options = ["creature", "instant", "sorcery", "enchantment", "artifact"]

user_query = st.text_input("Describe a card or effect:", placeholder="e.g. Draw two cards")
color_filter = st.multiselect("Color", list(color_values.values()))
#mana_filter = st.selectbox("Mana Cost", mana_options)
#card_type_filter = st.selectbox("Card Type", card_type_options)


if user_query:
    with st.spinner("Searching..."):
        selected_color_codes = [key for key, value in color_values.items() if value in color_filter]

        filter = {
            "color_identity": selected_color_codes,
            #"mana_cost": mana_filter,
            #"type": card_type_filter
        }

        print(filter["color_identity"])

        embedding = embed_query(user_query)
        results = query_pinecone(embedding, filter=filter)

        print(results)
    st.subheader("Similar Cards")
    for item in results:
        name = item["metadata"].get("name", "Unknown Card")
        text = item["metadata"].get("text", "")
        image_url = item["metadata"].get("image", "")
        score = item["score"]

        with st.container():
            st.markdown(f"### {name} (Score: {score:.3f})")
            if image_url:
                st.image(image_url, width=200)
            st.write(text)