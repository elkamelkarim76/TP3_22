Dataset : [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer)

Pipeline : Data → EDA → Prétraitement → Feature engineering → ML → Évaluation → Déploiement Docker
- Features : probabilités implicites des cotes, forme sur 5 matchs, attributs tactiques des équipes
- Split temporel (test = saison 2015/2016), validation croisée `TimeSeriesSplit`
- Modèles : Régression logistique, Random Forest, HistGradientBoosting (GridSearch)

Lancer l'API :
```bash
docker build -t soccer-api .
docker run -p 8000:8000 soccer-api
# Swagger : http://localhost:8000/docs
```

## 2. Big Data — Santander Value Prediction — `02_santander_spark.ipynb`
Compétition : [Santander Value Prediction Challenge](https://www.kaggle.com/competitions/santander-value-prediction-challenge)

- Stockage HDFS (docker-compose Hadoop) + traitement PySpark
- EDA distribuée (Spark SQL), MapReduce (RDD), log1p, stats par ligne, sélection par Random Forest
- MLlib : LinearRegression, RandomForest, GBT + CrossValidator — métrique RMSLE

## Données
```bash
bash scripts/download_data.sh
```

## Structure
```
├── 01_soccer_ml.ipynb
├── 02_santander_spark.ipynb
├── 03_github.ipynb
├── app/main.py            # API FastAPI
├── models/                # modèle sklearn
├── Dockerfile
├── requirements.txt
├── docker-compose.yml     # cluster Hadoop
└── scripts/download_data.sh
```
