from flask import Flask, jsonify, request
import pandas as pd
import pickle
import numpy as np
import pandas as pd 
from lightgbm import LGBMClassifier
from zipfile import ZipFile


def load_data():
    
    # Données générales
    z = ZipFile('../data/general_info_app.zip')
    initial_data = pd.read_csv(z.open('general_info_app.csv'), index_col='SK_ID_CURR', encoding ='utf-8')
    
    # Données de travail pour sélection modèle
    z = ZipFile('../data/training_data_clean.zip')
    clean_data = pd.read_csv(z.open('training_data_clean.csv'), index_col='SK_ID_CURR', encoding ='utf-8')
    target = clean_data['TARGET']
    clean_data = clean_data.drop(columns='TARGET', axis=1)
    
    # Description
    description = pd.read_csv("../data/features_description.csv", 
                               usecols=['Row', 'Description'], encoding= 'unicode_escape')
    return initial_data, clean_data, target, description    

def load_model():

    '''loading the trained model'''
    pickle_in = open('../model/LGBM_model_final.pkl', 'rb') 
    clf = pickle.load(pickle_in)
    
    return clf

def load_customer_score(data, customer_id, model):  
    
    customer_score = model.predict_proba(data[data.index == int(customer_id)])[:,1]        
    return  customer_score[0]
    
    

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'NOSECRETKEY'

initial_data, clean_data, target, description = load_data()
model = load_model()
customer_ids = clean_data.index.values



@app.route('/get_score_credit/<id_client>', methods=['GET'])
def get_score_credit(id_client):
    """Récupération du score client à partir de son identifiant.
    Score client = probabilité d'être insolvable.
    """
    score = load_customer_score(clean_data, id_client, model)
    
    # renvoyer la prediction 
    dict_final = {
        'score' : round(score, 2)
        }
    return jsonify(dict_final)
    
    
#lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)