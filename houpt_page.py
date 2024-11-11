import streamlit as st  


title_page=st.Page('list_pages/title.py', title='Описание Адденбрукская когнитивной шкалы',
                                        icon=':material/description:',
                                        default=True)

general_assment = st.Page("list_pages/ace_score.py", title="Общая оценка по ACE-III", 
                                                icon=':material/psychology:')

dementia_assment = st.Page("list_pages/predict_diagnos.py", 
                           title="Оценка при нейродегенеративных нарушениях по ACE-III", 
                           icon=":material/psychology_alt:")

model_page=st.Page('list_pages/model_page.py', title=" Метрики и описание моделей",
                   icon=':material/list_alt:')
                                            


autors=st.Page("list_pages/autors.py", title="Разработчики", 
                                  icon=':material/group:')

pg = st.navigation({
                    'Описание Адденбрукской когнитивной шкалы': [title_page],
                    'Нейропсихологическая оценка ACE-III при помощи ML':[general_assment, dementia_assment], 
                    'Информация о моделях': [model_page],
                    'Разработчики': [autors]
                    
                    
})



st.set_page_config(page_title="ACE-III", page_icon=":material/neurology:")

pg.run()