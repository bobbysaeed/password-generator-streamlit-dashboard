import streamlit as st
from nltk.corpus import words

from src.password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator


st.image('https://cdn.dribbble.com/userupload/42306708/file/original-042d10b6579c7fb485a001087f065041.png?resize=768x576&vertical=center', width=300)
st.title('Password Generator Dashboard')
options = st.radio(
        'Password type:',
            options=['RandomPasswordGenerator', 'MemorablePasswordGenerator', 'PinCodeGenerator']
)
if options == 'PinCodeGenerator':
    length = st.slider('length o the password', 0, 10, 4)
    generator = PinCodeGenerator(length)
    st.write(generator.generate())
