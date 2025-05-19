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
    length = st.slider('length of the password', 0, 10, 4)
    generator = PinCodeGenerator(length)
    st.write(generator.generate())
elif options == 'RandomPasswordGenerator':
    length = st.slider('length o the password', 0, 10, 4)
    include_numbers = st.toggle('include_numbers')
    include_symbols = st.toggle('include_symbols')
    if include_symbols:
        include_symbols = st.text_input('include_symbols')
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
    st.write(generator.generate())
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
    st.write(generator.generate())