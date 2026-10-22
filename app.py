import streamlit as st
import pickle

# Model aur Vectorizer load karein
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📩 SMS/Email Spam Detection System")
st.write("Apna message niche enter karein aur check karein ki woh **Spam** hai ya **Not Spam (Ham)**.")

user_input = st.text_area("Message yahan type ya paste karein:")

if st.button("Check Karein"):
    if user_input.strip() == "":
        st.warning("Kripya koi message enter karein!")
    else:
        data = [user_input]
        vectorized_data = vectorizer.transform(data)
        prediction = model.predict(vectorized_data)
        
        if prediction[0] == 1:
            st.error("🚨 Yeh ek SPAM message hai!")
        else:
            st.success("✅ Yeh ek Safe (Not Spam) message hai!")
