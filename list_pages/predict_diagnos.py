#это программа по предсказанию диагноза

import streamlit as st
import numpy as np
import pandas as pd

from predict_clf import Predict_ace_pkl
from predict_pytorch import predict_dam

from inputs_data import input_data
from new_database import Database

from anomal_predict import plot_neurocog
from interpetator import text_conclusion_diagn





#функция вывода результата
#Функция вывода результатов
def result():
    st.subheader('нажмите на кнопку для получения результатов и сводную талицу',divider=True)
    if st.button("Нажимая на кнопку ниже вы даете согласие на сбор и обработку обезличенных данных теста для улучшения рекомендаций", type='primary'):
        
        st.subheader('Описание результатов')
        st.warning('заключение создано при помощи нейросети, возможны неточности', icon='⚠️')
        
        df_interp=pd.read_csv('interpitate_diagn.csv').drop(columns='Unnamed: 0')              
        interpritation=df_interp.iloc[y_predict_diagnos, y_predict_stepen]
        
        text_conc=text_conclusion_diagn( interpritation, ACE_anomal, ACE)
        container = st.container(border=True)
        container.write(text_conc)
        
        
        st.subheader('Сводная таблица', divider='blue')
              #Вывод общих сведений
        
                   
        st.write(f'Возраст: {age} лет')

        total={ 'Возраст':age, 
                'm-ACE':m_ACE,
                'ACE-III':ACE,
                'ВНИМАНИЕ':attantion,
                'ПАМЯТЬ':memory, 
                'БЕГЛОСТЬ':fluence, 
                'РЕЧЬ':speech, 
                'Зрительно-пространственные функции':spatial,
                'диагноз': diagnos, 
                "предсказание диагноза":dict_diagnos[y_predict_diagnos],
                "предсказание степени нарушения ":dict_stepen[y_predict_stepen],
                'оценка предсказания': assement_dig
                }
                
              
     
                                                                        
        df_total=pd.DataFrame(total, index=['Значение']).T
        df_total['Значение']=df_total['Значение'].astype(str) #чтоб не возникало ошибки при выводе таблицы, глюк streamlit
        st.table(df_total)
    
          #ГРАФИКИ


#2      
       
        fg2=plot_neurocog(ACE_anomal, y_pred_dam, age, ACE)
        
       
        st.plotly_chart(fg2, use_container_width=True)
        
          #Массив для записи в базу данных
        massiv=total
        
    #запись в базу данных 
        data_db=Database()   
        event= diagnos
        if event=='студенты_тренировка':
            st.write('данные успешно обработаны')
        else:
            try:
                data_db.insert_data_dementia(massiv.values()) 
            except:
                
                data_db.insert_data_dementia(massiv.values())
                st.write('хорошего вам дня') 



def predict():    
    st.subheader('общий балл', divider=True)
    st.write('общий балл: ', ACE)
    
    st.subheader('Баллы больше 88 считаются нормальными, ниже 82 - следует подозревать деменцию')
    if ACE<88:
        st.warning('Ниже нормы. ACE-III=  '+str(ACE))
        st.warning('Ниже нормы. m_ACE=  '+str(m_ACE))
    else:
        st.write('ACE-III= ',ACE)
        st.write('m-ACE= ',m_ACE)
        
    #степень выраженности нарушений
    
    st.subheader('Степень выраженности когнитивных нарушений', divider=True)
    if dict_stepen[y_predict_stepen]==label_stepen[1]:
        st.warning('степень выраженности: '+ str(dict_stepen[y_predict_stepen]))
        st.write('вероятность: ', y_pred_proba_stepen.round(2))
    elif dict_stepen[y_predict_stepen]==label_stepen[2] or dict_stepen[y_predict_stepen]==label_stepen[3]:
        st.error('степень выраженности: '+ str(dict_stepen[y_predict_stepen]))
        st.write('вероятность: ', y_pred_proba_stepen.round(2))

    else:
        st.write('степень выраженности: ', dict_stepen[y_predict_stepen])
        st.write('вероятность: ', y_pred_proba_stepen.round(2))
        
    #предсказание диагноза
    st.subheader('Дифференциальная диагностика', divider=True)
    if dict_diagnos[y_predict_diagnos]==label_diagnos[1]:
        st.warning('''У пациента выявлены когнитивные нарушения, которые пока не достигли степени деменции. 
                   Рекомендуется провести повторное обследование через полгода, так как пациент входит 
                   в группу риска развития деменции.''')
        st.write('Вероятность: ', y_pred_proba_diagnos.round(2))
    elif dict_diagnos[y_predict_diagnos]==label_diagnos[2]:
        st.error('''Когнитивный профиль пациента по данной методике нейропсихологического тестирования имеет
                 значительное сходство с когнитивным профилем пациентов, страдающих деменцией. 
                 Для более точного диагноза рекомендуется провести дополнительные обследования. 
                 ''')
        st.write('Вероятность: ', y_pred_proba_diagnos.round(2))
    else:
        st.write('Диагноз: '+ str(dict_diagnos[y_predict_diagnos]))
        st.write('Вероятность: ', y_pred_proba_diagnos.round(2))
        
        
  



#**************************НАЧАЛО РАБОТЫ ПРОГРАММЫ**********************************************

#****************ОБЛОЖКА ПРОГРАММЫ ВВЕДЕНИЕ***********************************

text, foto=st.columns(2, vertical_alignment='center')

with st.container():
    with text:
        st.title('Оценка при нейродегенеративных нарушениях по Адденбрукской когнитивной шкале ')
    with foto:
        st.image('list_pages/image/dementia.jpeg', width=290)

st.write('''
Модели машинного обучения по входящим данным оценивают, к какому классу больше всего соответствует нейрокогнитивный профиль:  
* обычные возрастные изменения;  
* когнитивные нарушения, которые не достигают стадии деменции;  
* деменция;
* какие когнитивные функции нарушены.

Также они формируют текстовый отчёт и визуализируют данные.
''',
)

st.warning('''Если вы вводите данные пациентов с органическим повреждением мозга по типу: инсульт, 
           опухоль, черепно-мозговая травма и т. п., то выводы моделей могут быть нерелевантны.''', 
           icon=':material/release_alert:')

#***********************ВВОД ДАННЫХ*************************************************************************

st.subheader('Введите данные',divider=True)
try:
    m_ACE, ACE, attantion, memory, fluence, speech, spatial, age,  diagnos, ACE_anomal=input_data()
    ACE_III=np.array([ACE, attantion, memory, fluence, speech, spatial, age])

#________________________ОБРАБОТКА ДАННЫХ__________________________________________    
    #значение лейблов
    label_stepen=['незначительные', 'умеренные', 'выраженные', 'значительные']
    label_diagnos=['норма', 'mci', 'деменция']
    
    #загрузка моделей
    model_diagnos=Predict_ace_pkl('clf_models/mode_diagnosl.pkl')
    model_stepen=Predict_ace_pkl('clf_models/model_cat_stepen.pkl')
    
    y_pred_dam=predict_dam(ACE_III)
   
           
    #предсказание диагноза
    y_predict_diagnos=model_diagnos.predict(ACE_III)[0]
    y_pred_proba_diagnos=model_diagnos.predict_proba(ACE_III).max()
    classes_diagn=model_diagnos.clf_classes()
       
    #предсказание степени
    y_predict_stepen=model_stepen.predict(ACE_III)[0]
    y_pred_proba_stepen=model_stepen.predict_proba(ACE_III).max()
    classes_stepen=model_stepen.clf_classes()
    
    #словарь лейблов
    dict_stepen=dict(zip(classes_stepen, label_stepen))
    dict_diagnos=dict(zip(classes_diagn, label_diagnos))

#__________________ВЫВОД ДАННЫХ__________________________________________    
    
    #1
#_Управление кнопкой чтоб результаты не сбрасывались___________________
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True
    
    #2
    st.button('Нажмите для получения рекомендаций по интерпретации', on_click=click_button)
    if st.session_state.clicked:
        
        predict() 
        
              #оценка предсказания
        st.subheader('Оцените результаты предсказания', divider='green')
        assement_dig=st.radio('согласны?',  ['нет ответа','да',  'нет'], key=1, index=0)
        if assement_dig=='нет':
            assement_dig=st.selectbox('что подходит лучше', ['нет ответа',
                                                         'нет нарушений', 
                                                          'Умеренные когнитивные нарушения (MCI)',
                                                          'Деменция',
                                                          'Другое'],index=0)
        # - выводит рекомендации по интерпритации
  
# Вывод графика и текста       
        result()
    
    
    

except TypeError:
    st.error('Введите возраст. Он должен быть не менее 18 лет')
