import streamlit as st 
import pandas as pd


#********************Програмаа по описанию метрик моделей машинного обучения*****************

st.title('Характеристики моделей машинного обучения')

st.header('Характеристика выборки и общие принципы построения моделей.', divider=True)

label_noses=dict(
инстульт =                                 81,
деменция=                                34,
Болезнь_Паркинсона=                               32,
mci=                                     26,
норма=                                  19,
ЧМТ=                            6,
другое_органическое_заболевание_ЦНС=      5,
опухоль=                                  2,
психиатрическое_заболевание_тревога=     1)


  
st.table(label_noses )
with open('list_pages/image_metric/text_dataset.txt', 'r',encoding='UTF-8') as f:
        text_dataset = f.read()
        st.text(text_dataset)
         
st.subheader('Всего человек')
st.write(sum(label_noses.values()))

st.header('Характеристики модели, предсказывающей степень',divider=True)
with st.expander('характеристики модели'):
   

    metric_step={'CatBoost':	[0.91,	0.99]}
    st.table(pd.DataFrame(metric_step, index=['Accuracy', 'AUC']))
         
    st.image('list_pages/image_metric/confus_step.png') 
    st.image('list_pages/image_metric/признаки_степень.png')
    st.image('list_pages/image_metric/stepen/fig_auc.png')
    with open('list_pages/image_metric/stepen/file.txt', 'r') as f:
        metric_step=f.readlines()
        st.dataframe(metric_step)
#Диагноз        
st.header('Характеристики модели, предсказывающей диагноз',divider=True)
with st.expander('характеристики модели'):
   

    metric_step={'CatBoost':	[0.91,	0.98]}
    st.table(pd.DataFrame(metric_step, index=['Accuracy', 'AUC']))
    
    st.write('''В выборку входили:
* пациенты без когнитивных нарушений и жалоб на них, которые не были обнаружены при тестировании;
* люди с умеренными когнитивными нарушениями, предъявлявшие жалобы на изменение памяти и внимания. 
С помощью нейропсихологических тестов у них было обнаружено снижение когнитивных функций. 
Эта группа людей испытывала незначительные трудности в повседневной жизни, 
но активно использовала компенсаторные стратегии для преодоления трудностей;
* пациенты с установленным диагнозом «деменция»: болезнью Альцгеймера, деменцией 
с тельцами Леви, сосудистой деменцией 
и другими неуточнёнными нейродегенеративными заболеваниями.''')
         
    st.image('list_pages/image_metric/diagnos/fig_matrix.png', caption='Значение меток: 0-нет нарушений, 1-mci, 2-деменция') 
    st.image('list_pages/image_metric/diagnos/fig_auc.png', caption='AUC для каждой из меток')
    with open('list_pages/image_metric/diagnos/file.txt', 'r') as f:
        metric_diagn = f.readlines()
        
        st.dataframe(metric_diagn)

#Повреждение мозга        
st.header('Характеристики модели, предсказывающей органическое повреждение мозга',divider=True)
with st.expander('характеристики модели'):
   

    metric_step={'нейросеть':	[0.87,	0.91]}
    st.table(pd.DataFrame(metric_step, index=['Accuracy', 'AUC']))
    st.write('''Под органическим повреждением мозга понимались различные состояния,
             связанные с нарушением структуры мозговой ткани:
* инсульт;
* черепно-мозговая травма;
* деменция;
* болезнь Паркинсона;
* опухоль мозга;
* MCI (умеренное когнитивное нарушение) и другие причины структурных повреждений мозговой ткани.''')
         
    st.image('list_pages/image_metric/damage/fig_matrix.png', caption='Значение меток: 0-нет нарушений, 1-есть повреждение') 
    st.image('list_pages/image_metric/damage/fig_roc_curve.png')
   
     