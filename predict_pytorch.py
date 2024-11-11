import numpy as np
import onnxruntime


ort_session = onnxruntime.InferenceSession('clf_models/dam_prediction.onnx')


def predict_dam(ACE):
    
   
    ort_inputs = {ort_session.get_inputs()[0].name: ACE.astype(np.float32).reshape(1, -1)}
    ort_outs = ort_session.run(None, ort_inputs )

     
    maps={'no_dam':0, 'damage':1}
    y_predict=[]
    classes=[x for x in maps.keys()]
    y_pred = ort_outs
    y_pred=np.round(y_pred,0)[0][0][0].astype(np.int32) 

    y_predict=classes[y_pred]
        
        
    
    return y_predict



def proba_predict_dam(ACE):
      
    ort_inputs = {ort_session.get_inputs()[0].name: ACE.astype(np.float32).reshape(1, -1)}
    ort_outs = ort_session.run(None, ort_inputs )
   
    y_pred_proba = ort_outs[0][0][0]
    y_pred=np.round(y_pred_proba ,0)

    
    if y_pred==0:
            proba=(1-y_pred_proba)*100
            proba=np.round(proba, 3)
    elif y_pred==1:
             proba=y_pred_proba*100
             proba=np.round(proba, 3)
        
    return proba
    

   
    
    


