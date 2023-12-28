from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# openai = OpenAI()
# result = openai.predict("내가 가장 좋아하는 동물은?")
# print(result)

chat_open_ai = ChatOpenAI()

import streamlit as st

st.title('애완동물을 잘 돌보는 방법')
pet = st.text_input('어떤 애완동물에 대해 알고 싶은가요?')
if st.button('알아보기'):
    with st.spinner('찾는 중...'):
        result = chat_open_ai.predict(pet+"를 잘 돌보는 방법을 알려줘")
        st.write(result)
