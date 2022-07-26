import streamlit as st
from PIL import Image
st.title('About System')
st.markdown("A customer personality study involves examining the ideal client profiles of a company. This can help companies better understand who their target market is and how to best serve them. By better understanding its customers, a company is able to adapt its products more easily to meet the individual needs of each individual customer.")
image = Image.open ( 'Business_presentation.jpg' )
st.image ( image )
st.write(" * Firstly this system tries to get the inputs from customer and its behaviour towards purchasing the product.")
st.write(" * Then using the model it predicts the cluster or group in which particular customer falls.")
st.write(" * Also, add-on to this it tries to visualize the insights")
