#по общей оценке

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from predict_clf import Predict_ace_pkl
from predict_pytorch import predict_dam, proba_predict_dam


from new_database import Database

from anomal_predict import plot_neurocog
from interpetator import text_conclusion
from sqlalchemy import text


   

text, foto = st.columns(2, vertical_alignment='center')

with st.container():
    with text:
        st.title('Общая оценка когнитивных функций по Адденбрукской когнитивной шкале')
    with foto:
        st.image('list_pages/image/neuro_assment.jpeg', width=290)
        




st.write('''Модели машинного обучения позволяют оценить:
* степень выраженности когнитивных функций;
* соответствие профиля когнитивных способностей органическим нарушениям;
* какие когнитивные функции нарушены.

Также они формируют текстовый отчёт и визуализируют данные.''')


st.subheader('Введите данные',divider=True)


#ввод данных теста
def input_data():
    
    
    age=st.number_input("Введите возраст, он должен быть не менее 18 лет", step=1)
    if age<18:
        
        
        return age
        
    else:
           

        diag=['нет ответа','студенты_тренировка','нет_повреждений',"mci",'dementia',
              'stroke', 'parkinson','barain_injury','другое органическое заболевание ЦНС', 'псевдодеменция', 'психиатрическое заболевание: депрессия', 
              'психиатрическое заболевание: тревога', 'другое психиатрическое расстройство']
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

#Функция вывода результатов
def result():
    st.subheader('нажмите на кнопку для получения результатов и сводную талицу')
    if st.button("Нажимая на кнопку ниже вы даете согласие на сбор и обработку обезличенных данных теста для улучшения рекомендаций", type='primary'):
        
        st.subheader('Описание результатов')
        st.warning('заключение создано при помощи нейросети, возможны неточности', icon='⚠️')
        
        #text_conc=text_conclusion(y_pred_cat, y_pred_dam,  ACE_anomal, ACE)
        #container = st.container(border=True)
        #container.write(text_conc)
        
        
        st.subheader('Сводная таблица', divider='blue')
              #Вывод общих сведений
        
        
              
        if y_pred_dam=='damage':
            dam='повреждение мозга'
        else:
            dam='нет повреждений мозга'
            
        st.write(f'Возраст: {age} лет')

        total={ 'Возраст':age, 
                'm-ACE':m_ACE,
                'ACE-III':ACE,
                'ВНИМАНИЕ':attantion,
                'ПАМЯТЬ':memory, 
                'БЕГЛОСТЬ':fluence, 
                'РЕЧЬ':speech, 
                'Зрительно-пространственные функции':spatial, 
                "степень нарушения предсказание":y_pred_cat,
                "наличие повреждение мозга предсказание":dam,
                "степень нарушения специалист":assmet_cat,
                "наличие повреждение мозга специалист":assement_dam
     
                                                                        }
        df_total=pd.DataFrame(total, index=['Значение']).T
        df_total['Значение']=df_total['Значение'].astype(str) #чтоб не возникало ошибки при выводе таблицы, глюк streamlit
        st.table(df_total)
    
          #ГРАФИКИ

#1
        st.header('Когнитивный профиль', divider='red')
        fig1=px.bar(df[df.columns[0:2]].T,  
             orientation='h', 
            labels={'index':'балл', 'value':'значение'},
            text=[m_ACE, ACE],
            title='Адденбрукская когнитивная шкала-III. '+'Возраст: '+str(age)
           )

        fig1.add_vline(x=88, line_width=5, line_dash="dash", line_color="red")
        fig1.add_vline(x=82, line_width=5, line_dash="dash", line_color="red")
        fig1.add_vline(x=27, line_width=5, line_dash="dash", line_color="yellow")

        #df_procent=((df[df.columns[2:7]]/[18,26,14,26,16])*100).T.round(2) #датафрейм для процентного представления потери баллов


#2      
       
        fg2=plot_neurocog(ACE_anomal, y_pred_dam, age, ACE)
        
        #=px.bar(df_procent, text=df_procent['Значение'].values,
            #orientation='h', 
            #labels={'index':'функция', 'value':'процент сохранности функции от максимального значения'},
            #title='Адденбрукская когнитивная шкала-III.'+' Возраст: '+str(age),
            #)

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fg2, use_container_width=True)
        
        #Массив для записи в базу данных
        ACE_db=[m_ACE, ACE, attantion, memory,fluence, speech, spatial]
        stepen=y_pred_cat
        damage=y_pred_dam
        massiv=[age]+ACE_db+[stepen,damage, diagnos]+[assmet_cat, assement_dam]
       
    #3    
        data_db=Database()
        event= diagnos
        if event=='студенты_тренировка':
            st.write('данные успешно обработаны')
        else:
            try:
                data_db.insert_data(massiv)
               
            except:
                st.write('no data')
                #data_db.insert_data(massiv)
               
                
      
            
            
            
    
#функция предсказания
def predict():
       
    st.subheader('Баллы больше 88 считаются нормальными, ниже 82 - следует подозревать деменцию')
    if ACE<88 and ACE>=82:
        st.warning('Ниже нормы. ACE-III=  '+str(ACE))
        st.warning('Ниже нормы. m_ACE=  '+str(m_ACE))
    elif ACE<82:
        st.error('Следует подозревать деменцию. ACE-III=   '+str(ACE))
        st.error('Следует подозревать деменцию. m_ACE=   '+str(m_ACE))
   
    else:
        st.write('ACE-III= ',ACE)
        st.write('m-ACE= ',m_ACE)
    #предсказание степени выраженности нарушений
    
    
    st.subheader('Предсказание степени выраженности нарушений', divider='orange')
    if y_pred_cat=='незначительные' or y_pred_cat=='умеренные' :
        st.write('степень нарушения когнитивных функций: '+ str(y_pred_cat))
        st.write('Вероятность достоверности прогноза: ', y_pred_cat_proba*100)
    else:
        st.warning('степень нарушения когнитивных функций: '+str(y_pred_cat))
        st.write('Вероятность достоверности прогноза: ', y_pred_cat_proba*100)
         
        #st.header('График достоверности прогноза', divider='red')

   
    #fig3=px.bar(y=data_graf_cat.keys(), 
    #        x= data_graf_cat.values(),
    #        orientation='h',
    #        text=data_graf_cat.values(),
    #        labels={'y':'категория',  'x':'вероятность'},
             
    #                   )
    #st.plotly_chart(fig3, use_container_width=True)
    

#повреждения мозга
    st.subheader('Предсказание наличия повреждения мозга', divider='blue')
    
    
    
    if y_pred_dam=='damage':
        st.warning('есть вероятность органического повреждения мозга, проведите дополнительные исследования')
        st.write('Инсульт, ЧМТ, нейродегенеративные нарушения, MCI и т.п')
        st.write('Вероятность достоверности прогноза:   ', y_pred_dam_proba)
    elif y_pred_dam=='no_dam':
        st.write('отсутсутсвует органическое повреждение мозга', )
        st.write('Вероятность достоверности прогноза:   ', y_pred_dam_proba)
        

  
    
    

    

#основная программа
#**************************************************
#***************************************************

try:
    m_ACE, ACE, attantion, memory, fluence, speech, spatial, age,  diagnos, ACE_anomal=input_data()


    dic={'m-ACE':m_ACE,
    'ACE-III':ACE,
    'ВНИМАНИЕ':attantion,
     'ПАМЯТЬ':memory, 
     'БЕГЛОСТЬ':fluence, 
     'РЕЧЬ':speech, 
     'Зрительно-пространственные функции':spatial, 
     'Возраст':age 
     }
    df=pd.DataFrame(dic, index=['Значение'])



#загрузка моделей предсказания

    ACE_III=np.array([ACE, attantion, memory, fluence, speech, spatial, age])
    

     #значение лейблов
    label_stepen=['незначительные', 'умеренные', 'выраженные', 'значительные']
    
    #модель предсказания степени
    model_cat=Predict_ace_pkl('clf_models/model_cat_stepen.pkl')     
    
    #степень повреждения
    y_pred_cat=label_stepen[model_cat.predict(ACE_III)[0]]
    y_pred_cat_proba=model_cat.predict_proba(ACE_III).max().round(2)

    p_value=model_cat.predict_proba(ACE_III).round(2)
    #classes=model_cat.clf_classes()
    #data_graf_cat=dict(zip(classes, p_value[0]))

#органическое ли?
    y_pred_dam=predict_dam(ACE_III)                
    y_pred_dam_proba=proba_predict_dam(ACE_III)    
    
   

   
    st.header('РЕЗУЛЬТАТЫ', divider='rainbow')

#1
#_Управление кнопкой чтоб результаты не сбрасывались___________________
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True


#______________________________________________

#2
    st.button('Нажмите для получения рекомендаций по интерпретации', on_click=click_button)
    if st.session_state.clicked:
        predict() # - выводит рекомендации по интерпритации
    
    #оценка степени выраженности
        st.header('Оцените результаты прогноза')
        st.subheader('Оцените результаты степени выраженности', divider='orange')

# Объединяем два массива
        
        assmet_cat=st.radio('согласны?', ['нет ответа','да', 'нет'], key=1, index=0)
        if assmet_cat=='нет':
            assmet_cat=st.selectbox('что подходит лучше', label_stepen, index=0)


#оценка наличия повреждения
        st.subheader('Оцените результаты наличия повреждения мозга', divider='blue')
        assement_dam=st.radio('согласны?',  ['нет ответа','да',  'нет'], key=2, index=0)
        if assement_dam=='нет':
            assement_dam=st.selectbox('что подходит лучше', ['нет ответа','есть повреждение мозга', 'нет повреждения мозга'],index=0)


        
        result()





except TypeError:
     st.error('Введите возраст. Он должен быть не менее 18 лет')

    
        
    











    



   
    
    

   
  

