import streamlit as st
from nltk.corpus import words

from src.password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator

st.image('src/images/Password_logo.jpg', width=300)
# Title of the application
st.title(":zap: Password Generator Dashboard")

options = st.radio(
        'Password type:',
            options=['RandomPasswordGenerator', 'MemorablePasswordGenerator', 'PinCodeGenerator']
)
if options == 'PinCodeGenerator':
    length = st.slider('length of the password', 0, 10, 4)
    generator = PinCodeGenerator(length)
elif options == 'RandomPasswordGenerator':
    length = st.slider('length o the password', 0, 10, 4)
    include_numbers = st.toggle('include_numbers')
    include_symbols = st.toggle('include_symbols')
    if include_symbols:
        include_symbols = st.text_input('include_symbols')
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
else:
    no_of_words = st.slider('Number of Words', 0, 7, 5)
    separator = st.text_input('separator', '-')
    capitalization = st.toggle('Capitalization')
    vocabulary = words.words()  # Get the list of words from NLTK corpus
    generator = MemorablePasswordGenerator(
        no_of_words,
        separator,
        capitalization,
        vocabulary
    )

password = generator.generate()
st.write(f'The Password is: ```{password}``` ')