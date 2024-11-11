import streamlit as st
from sqlalchemy import text


        
        
class Database():
    def __init__(self):
        self.conn=st.connection('tidb', type='sql')
        
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
        connection=self.conn
        
        dict_data=dict(zip(self.columns_dementia,data))
               
        with connection.session as session:
            session.execute(text( '''INSERT INTO ace_dementia
(age, m_ACE, ACE, attention, memory, fluency, speech, spatials, 
diagnosis, predicted_diagnosis, predicted_stepen, assessment_prediction)
            
VALUES(
:age, :m_ACE, :ACE, :attention, :memory, :fluency, :speech, :spatials, 
:diagnosis, :predicted_diagnosis, :predicted_stepen, :assessment_prediction) ''' ), dict_data)
            session.commit()
    
    
    def insert_data(self, data):
        connection=self.conn
        
        dict_data=dict(zip(self.columns, data))
       
        
        with connection.session as session:
            session.execute(text( '''INSERT INTO ace_general (      
            age, m_ACE, ACE, attantion, memory, fluence, speech, spatials, 
            stepen, damage, diagnos, assment_stepen, assment_damage)
                                  
            VALUES (
            :age, :m_ACE, :ACE, :attantion, :memory, :fluence, :speech, :spatials,
            :stepen, :damage, :diagnos, :assment_stepen, :assment_damage)'''
                ),  dict_data)
    
            session.commit()

    







   

        

