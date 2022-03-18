# Projet 7 - Implémentez un modèle de scoring
## Parcours Data Scientist - OpenClassrooms

L'entreprise Prêt à dépenser souhaite mettre en œuvre un outil de 'scoring crédit' pour calculer la probabilité qu'un client rembourse son crédit. En fonction, la demande de crédit est classifiée comme accordée ou refusée. Cette entreprise souhaite développer un algorithme de classification en s'appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).

De plus, les chargés de relation client ont fait remonter le fait que les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d'octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l'entreprise veut incarner.

Prêt à dépenser décide donc de développer un dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement.

#### Traitement des données
Features engineering effectué à partir à partir du kernel Kaggle [Lightgbm with simple features](https://www.kaggle.com/jsaguiar/lightgbm-with-simple-features)


#### Dashboard Scoring Credit:
Il s'agit d'une Web App effectuée en collaboration entre Heroku et Streamlit. Elle est consultable [ici](https://scoring-credit-dashboard.herokuapp.com/).
L'API qui permet de récupérer le score est de type flask.


#### L'application répond au cahier des charges suivant :

- Permettre de visualiser le score et l’interprétation de ce score pour chaque client pour une personne non experte en data science.
- Permettre de visualiser des informations descriptives relatives à un client.
- Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.


#### Les données :
Données Kaggle : [Home Credit Default](https://www.kaggle.com/c/home-credit-default-risk/data)

#### Compétences évaluées :
- Présenter son travail de modélisation à l'oral
- Réaliser un dashboard pour présenter son travail de modélisation
- Rédiger une note méthodologique afin de communiquer sa démarche de modélisation
- Utiliser un logiciel de version de code pour assurer l’intégration du modèle
- Déployer un modèle via une API dans le Web
