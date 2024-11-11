
#ввод даты
import numpy as np
import streamlit as st
def input_data():
    
    
    
    age=st.number_input("Введите возраст, он должен быть не менее 18 лет", step=1)
    if age<18:
        
        
        return age
        
    else:
           

        diag=['нет ответа','норма','студенты_тренировка',"умеренные когнитивные нарушения",'Болезнь Альцгеймера',
              'Болезнь Паркинсона', 'Деменция с тельцами Леви', 'Лобно-височная деменция', 'Сосудистая деменция',
              'деменция не уточненая', 
              'псевдодеменция'
              ]
        diagnos = st.radio(
        "выберите повреждения мозга",
        diag, index=0
        )

#ВНИМАНИЕ

        st.header('Внимание', divider='rainbow')
        with st.container(border=True):
        
            at_time=st.selectbox("Внимание: ориентирование во времени",[0,1,2,3,4,5])
   
    
   
            at_place=st.selectbox("Внимание: ориентирование в месте", [0,1,2,3,4,5])
    

            at_three_words=st.selectbox("Внимание: повторить 3 слова и запомнить", [0,1,2,3])
    


            at_calculate=st.selectbox("Внимание: серийный счет от 100 отнимать по 7", [0,1,2,3,4,5])
    


            attantion=at_time+at_place+at_three_words+at_calculate

            st.subheader('Общий балл по вниманию', divider='blue')
            st.write(attantion)


#ПАМЯТЬ
        st.header('Память', divider='rainbow')
    
        with st.container(border=True):
            mem_words=st.selectbox("Память: Припомнить 3 слова", [0,1,2,3])
    
            mem_adr=st.selectbox("Память: Запомнить адресс", [0,1,2,3,4,5,6,7])
    
            mem_president=st.selectbox("Память на президента, премьер-министра и т.д", [0,1,2,3,4])
    
            mem__remember_adr=st.selectbox("Память: свободное припоминание адреса", [0,1,2,3,4,5,6,7])
    
            mem_uznav=st.selectbox("Память: выбор из множества", [0,1,2,3,4,5])
    
            memory=mem_words+mem_adr+mem_president+mem__remember_adr+mem_uznav
            st.subheader('Общий балл по памяти', divider='blue')
            st.write(memory)



#БЕГЛОСТЬ
        st.header('Скорость вербальных ассоциаций', divider='rainbow')
        with st.container(border=True):

            word_fluence=st.selectbox("Называние за 1 минуту слов на букву", [0,1,2,3,4,5,6,7])
    

            word_animal=st.selectbox("Называние за  1 минуту животных", [0,1,2,3,4,5,6,7])
    

            fluence=word_fluence+word_animal
            st.subheader('Общий балл по скорости словесных ассоциаций', divider='blue')
            st.write(fluence)


#РЕЧЬ
        st.header('Речь', divider='rainbow')
        with st.container(border=True):

            speech_komand=st.selectbox("Речь: команды", [0,1,2,3])
    
            speech_sentense=st.selectbox("Речь: написание предложений", [0,1,2])
    
            speech_repit_word=st.selectbox("Речь: повторение слов", [0,1,2])
   
            speech_repit_poslov_1=st.selectbox("Речь: повторение 1 пословицы",[0,1])
    
            speech_repit_poslov_2=st.selectbox("Речь: повторение  2 пословицы", [0,1])
    
            speech_name=  st.selectbox("Речь: название", [0,1,2,3,4,5,6,7,8,9,10,11,12])
    

            speech_undestand=st.selectbox("Речь: понимание",[0,1,2,3,4])
        
            speech_read=st.selectbox("Речь: чтение", [0,1])
    

            speech=speech_komand+speech_sentense+speech_repit_word+speech_repit_poslov_1+speech_repit_poslov_2+speech_read+speech_name+speech_undestand
            st.subheader('Общий балл речь', divider='blue')
            st.write(speech)

#Зрительно-пространственные функции
        st.header('Зрительно-пространственные функции', divider='rainbow')
        with st.container(border=True):
            spatial_endless=st.selectbox("Копирование бесконечностей",[0,1])
    
            spatial_cub=st.selectbox("Копирование куба", [0,1,2])
    
            spatial_clock=st.selectbox("Тест часов",[0,1,2,3,4,5])
   
            spatial_punct=st.selectbox("Подсчет точек", [0,1,2,3,4])
    
            spatial_albabet=st.selectbox("Подсчет букв", [0,1,2,3,4])
    
            spatial=spatial_endless+spatial_cub+spatial_clock+spatial_punct+spatial_albabet

            st.subheader('Общий балл по зрительно-пространственным функциям', divider='blue')
            st.write(spatial)


#СВЕДЕНИЕ В ОБЩЕЕ
        ACE=attantion+memory+fluence+speech+spatial
        m_ACE=m_ACE=at_time-1+word_animal+mem_adr+spatial_clock+mem__remember_adr
        ACE_anomal=np.array([attantion, memory, fluence, speech, spatial])
        
    
        return m_ACE, ACE, attantion, memory, fluence, speech, spatial, age, diagnos, ACE_anomal