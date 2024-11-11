import streamlit as st

#программа об авторах

st.title('Разработчики')

foto1, text1 = st.columns(2, vertical_alignment='top')

foto2, text2 = st.columns(2, vertical_alignment='top')
                        
#первый автор
with st.container():
    with foto1:
        st.image("list_pages/image/sergey_fabula.jpg")
    with text1:
        st.write('*Казымаев Сергей Александрович*, клинический психолог, нейропсихолог, г. Москва')
    
   
#Второй автор
with st.container():
    with foto2:
        st.image("list_pages/image/slava_fabula.jpg")
    with text2:
        st.write('*Быков Вячеслав*, клинический психолог, нейропсихолог, г. Ярославль')