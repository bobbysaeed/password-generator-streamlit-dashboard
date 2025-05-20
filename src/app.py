import streamlit as st
from nltk.corpus import words

from src.password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator

st.image('src/images/Password_logo.jpg', width=300)
# Title of the application
st.title(":zap: Password Generator Dashboard")

options = st.radio(
                   ":lock: Password type:",
                   options=['RandomPasswordGenerator', 'MemorablePasswordGenerator', 'PinCodeGenerator']
                )

if options == 'PinCodeGenerator':
    length = st.slider("Length", min_value=2, max_value=10, value=4)

    generator = PinCodeGenerator(length)
elif options == 'RandomPasswordGenerator':
    length = st.slider("Length:", min_value=5, max_value=50, value=8)
    include_numbers = st.toggle('Include Numbers')
    include_symbols = st.toggle('Include Symbols')

    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
else:
    no_of_words = st.slider("Number of Words", min_value=2, max_value=10, value=5)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle('Capitalization')

    generator = MemorablePasswordGenerator(
        no_of_words,
        separator,
        capitalization,
        words.words()
    )

password = generator.generate()
st.write(":unlock: The Password is:")
st.header(fr"``` {password} ```")