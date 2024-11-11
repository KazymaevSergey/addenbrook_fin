import joblib
import plotly.express as px
import numpy as np
import streamlit as st


columns_anomal=['ВНИМАНИЕ', 'ПАМЯТЬ', 'БЕГЛОСТЬ', 'РЕЧЬ', 'ЗРИТЕЛЬНО_ПРОСТРАНСТВЕННЫЕ']

#создание словара с моделями
def dict_anomal_clf():
  k={}
  for name in columns_anomal:
    clf=joblib.load(f'clf_anomal/{name}.pkl')  
    k[name]=clf
  return k
    

#attention=16
#memory=23
#fluence=11
#speech=10
#spatial=15

#age=45

#ACE=attention+memory+fluence+speech+spatial

#ACE_anomal=np.array([attention, memory, fluence, speech, spatial])
#absolut=np.array([18,26,14,26,16])
#procent_anomal=(ACE_anomal*100/absolut).round(2)





#созадание функции предсказания на основе моделей
def predict_anomal(cognitive_name, val):
  pred=dict_anomal_clf().get(cognitive_name).predict(np.array(val).reshape(-1,1))
  return pred

def dict_anomal(absolut, procent_anomal, ACE_anomal):
  dic={}
  for colum, value,absol, proc  in zip(columns_anomal, ACE_anomal,absolut, procent_anomal):
    x=predict_anomal(colum, value.reshape(-1,1))
    if  x=='норма':
      dic[colum]=f'норма: {value}/{absol}/{proc} '

    elif  x=='нарушение':
      dic[colum]=f'нарушение: {value}/{absol}/{proc}'

   

  return dic



def color(ACE_anomal):
  c=[]
  for colum, value in zip(columns_anomal, ACE_anomal):
    
    x=predict_anomal(colum, value.reshape(-1,1))[0]
    if  x=='норма':
      c.append(x)
    elif x=='нарушение':
      c.append(x)
   
  return c


def plot_neurocog(ACE_anomal, interpretir, age, ACE):

# для надписи в титле
  if interpretir=='damage':
    inter='есть когнитивные нарушения'
    title=f'Возраст: {age}. ACE-III={ACE} - {inter}'
  elif interpretir=='no_dam':
    inter='незначительные когнитивные нарушения или отсутсвуют'
    title=f'Возраст: {age}.  ACE-III={ACE} - {inter}'
  
# создание словаря для графика
  absolut=np.array([18,26,14,26,16])
  procent_anomal=(ACE_anomal*100/absolut).round(2)
  bar_anomal=dict(zip(columns_anomal, procent_anomal))
  
# создание графика
  fig=px.bar(y=bar_anomal.keys(), 
             x=bar_anomal.values(), 
             orientation='h',
#             
             text=dict_anomal(absolut, procent_anomal, ACE_anomal).values(), 
#             
             color=color(ACE_anomal),  
             color_discrete_map={'норма': 'blue', 'нарушение': 'green'},
             
             labels={'color':'сохранность когнитивных функций', 
                     'y':'функции',
                     'x':'процент сохранности функции от максимального значения'}
            )
  
  fig.update_layout(
    title=dict(text=title)
                    )
  
  
  return fig










