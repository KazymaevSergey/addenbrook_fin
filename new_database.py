import streamlit as st
from sqlalchemy import text
from sqlalchemy import create_engine


        
        
class Database():
    def __init__(self):
          
        self.conn=create_engine(st.secrets.databaseTDIB.url, pool_pre_ping=True)               #st.connection('tidb', type='sql')
        
        self.columns_dementia = '''
age
m_ACE
ACE
attention
memory
fluency
speech
spatials
diagnosis
predicted_diagnosis
predicted_stepen
assessment_prediction'''.split()

        self.columns = ['age',  'm_ACE', 'ACE',  'attantion',  'memory',
            'fluence',  'speech', 'spatials', 'stepen', 'damage', 'diagnos', 
            'assment_stepen', 'assment_damage']
        
        
    def insert_data_dementia(self, data):
        engine=self.conn
        
        dict_data=dict(zip(self.columns_dementia,data))
               
        with engine.connect() as connect:
                connect.execute(text( '''INSERT INTO ace_dementia
(age, m_ACE, ACE, attention, memory, fluency, speech, spatials, 
diagnosis, predicted_diagnosis, predicted_stepen, assessment_prediction)
            
VALUES(
:age, :m_ACE, :ACE, :attention, :memory, :fluency, :speech, :spatials, 
:diagnosis, :predicted_diagnosis, :predicted_stepen, :assessment_prediction) ''' ), dict_data)
                connect.commit()
    
    
    def insert_data(self, data):
        engine=self.conn
        
        dict_data=dict(zip(self.columns, data))
       
        
        with engine.connect() as connect:
                connect.execute(text( '''INSERT INTO ace_general (      
            age, m_ACE, ACE, attantion, memory, fluence, speech, spatials, 
            stepen, damage, diagnos, assment_stepen, assment_damage)
                                  
            VALUES (
            :age, :m_ACE, :ACE, :attantion, :memory, :fluence, :speech, :spatials,
            :stepen, :damage, :diagnos, :assment_stepen, :assment_damage)'''
                ),  dict_data)
                connect.commit()

    







   

        

