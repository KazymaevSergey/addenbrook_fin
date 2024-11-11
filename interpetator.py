from yandex_cloud_ml_sdk import YCloudML
import streamlit as st
from anomal_predict import predict_anomal
import numpy as np

flod_id=st.secrets.yandexGPT.fold_id
key_api=st.secrets.yandexGPT.openai_key

sdk = YCloudML(folder_id=flod_id, auth=key_api)

model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)

columns_anomal=['ВНИМАНИЕ', 'ПАМЯТЬ', 'БЕГЛОСТЬ', 'РЕЧЬ', 'ЗРИТЕЛЬНО_ПРОСТРАНСТВЕННЫЕ']
absolut=np.array([18,26,14,26,16])

def function_interpetator(ACE_anomal):
  c={}
  for colum, value in zip(columns_anomal, ACE_anomal):
    x=predict_anomal(colum, value)
    if x=='норма':
      c[colum]=x[0]
    elif x=='нарушение':
      c[colum]=x[0]
       
  return c


def func_text(ACE_anomal):
    func_inter_norm=[]
    func_inter_diserd=[]
    cognitive=function_interpetator(ACE_anomal)
    for cog, inter, ace_val, ace_max in zip(cognitive.keys(), cognitive.values(), ACE_anomal, absolut):
        
        if inter=='норма':
          interet=cog+' '+inter+': '+str(ace_val)+' балл из '+str(ace_max)
          func_inter_norm.append(interet)
          
        if inter=='нарушение':
          interet=cog+' '+inter+': '+str(ace_val)+' балл из '+str(ace_max)
          func_inter_diserd.append(interet)
    return func_inter_norm, func_inter_diserd


def damage(val_damage):
    if val_damage=='no_dam':
        pred_dam=' причина не органического характера'
    elif val_damage=='damage':
        pred_dam=' причина органического характера'
    return pred_dam


       


#Функции по написанию текста

def text_conclusion(step_pred, y_dam, ACE_anomal, ACE):
    
    pred_dam=damage(y_dam)
    func_inter_norm, func_inter_diserd=func_text(ACE_anomal)
    
    input_text='''напиши нейропсихологическое заключение короткое  когнитивных нарушени {}, {}, 
                нарушены когнитивные функции {}, при этом сохранны {}
                Общий балл по Адденбруской когнитивной шкале {} из 100'''.format(step_pred, 
                                                                                 pred_dam, 
                                                                                 func_inter_diserd, 
                                                                                 func_inter_norm, ACE)
    result=model.run(input_text)
    
    return result[0].text
  
  
def text_conclusion_diagn(interpritation, ACE_anomal, ACE):
    
    
    func_inter_norm, func_inter_diserd=func_text(ACE_anomal)
    
    input_text='''напиши нейропсихологическое заключение короткое  когнитивных нарушени {}, 
                нарушены когнитивные функции {}, при этом сохранны {}
                Общий балл по Адденбруской когнитивной шкале {} из 100'''.format(interpritation, 
                                                                                  
                                                                                 func_inter_diserd, 
                                                                                 func_inter_norm, 
                                                                                 ACE)
    result=model.run(input_text)
    
    return result[0].text
  
