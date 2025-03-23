# 💰 Projet-3-Cryptomonnaie-Wild-Data-Hub

Ceci est le fruit du troisième projet que j'ai conçu dans le cadre de ma formation en tant que _DATA ANALYST_ à la **Wild Code School** de Lille.

![Image](https://github.com/user-attachments/assets/1af4003b-06d5-43a0-9353-c6b42e03d719)

![Image](https://github.com/user-attachments/assets/ea1562b8-9d8a-4ea8-a302-180116f58a3a)

## 🎯 Objectif du Projet :

Tableau de bord pour surveiller de manière centralisée les évolutions actuelles du portefeuille de crypto-monnaies, en fournissant un aperçu de leur valeur actuelle, de l'évolution des prix sur 24 heures et des alertes de tendance.
Les données de cours actuelles sont interrogées à partir de l'API REST de CoinMarketCap et stockées dans postgreSQL. L'API vous permet de faire
un maximum de 333 points de requêtes quotidiennes (~1 requête / 5 min). L'appel de plusieurs cryptos peut augmenter le
nombre de points requis par appel d'API, ce qui nécessite d'augmenter le temps entre les requêtes.

## ⌛ Temps Imparti : 
6 semaines


## ⭐ Fonctionnalités

💸 Suivi personnalisé de votre portefeuille crypto  
💸 Surveillance centralisée de sa valeur actuelle  
💸 Réaction rapide aux changements émergents  
💸 Affichage de la valeur globale ou actuelle  
💸 Conversion des valeurs en devise locale  
💸 Graphique de l'évolution des cryptomonnaies  
💸 Envoie d'alertes via discord 

---

### 📌 Prérequis

- [docker](https://docs.docker.com/get-docker/)  
- [docker-compose](https://docs.docker.com/compose/install/)  
- [clé API CoinMarketCap](https://coinmarketcap.com/api/)

---

## ⚙️ Configuration

Tous les paramètres sont gérés via des variables d’environnement transmises à la stack **docker-compose**. Pour plus de détails, consultez le fichier `config/settings.py`.

```bash
mv dotenv-sample .env
vi .env
```

- `SECRET_KEY` : définissez une clé secrète  
- `POSTGRES_PASSWORD` : mot de passe de la base de données  
- `SITE_HOSTNAME` : nom de domaine du site (peut contenir plusieurs valeurs séparées par un espace)  
- `ALLOWED_HOSTS` : hôtes autorisés - doit inclure `SITE_HOSTNAME` et l’IP du serveur Docker  
- `COINMARKET_KEY` : clé API CoinMarketCap utilisée pour les requêtes  
- `TARGET_CURRENCY` : devise locale pour la conversion des prix affichés  

---

## 🚀 Déploiement avec Docker

```
docker build . --tag europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest
```

```
docker build . --tag europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/o/crypto-celery:latest
```

```
docker build . --tag europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-celery-beat:latest
```

```
docker push europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest
```

```
docker push europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/o/crypto-celery:latest
```

```
docker push europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-celery-beat:latest
```

```
docker image rm europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest
```

```
docker build . --tag europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest
```

```
docker push europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest
```

---

## 🔥 Déploiement avec GCP

```
gcloud auth login
```

```
gcloud run services update crypto-web --set-env-vars SECRET_KEY='uPCFulvI_xSdvgNcJYpkQZiOi_jdB5Vo00m3GBOmv_heHj7yZeiP7TTv7WmZtPm-I4s' --region=europe-west4
```

```
gcloud run services update crypto-celery --set-env-vars SECRET_KEY='uPCFulvI_xSdvgNcJYpkQZiOi_jdB5Vo00m3GBOmv_heHj7yZeiP7TTv7WmZtPm-I4s' --region=europe-west4
```

```
gcloud run services update crypto-celery-beat --set-env-vars SECRET_KEY='uPCFulvI_xSdvgNcJYpkQZiOi_jdB5Vo00m3GBOmv_heHj7yZeiP7TTv7WmZtPm-I4s' --region=europe-west4
```

```
gcloud run deploy crypto-web --image=europe-west4-docker.pkg.dev/elegant-plating-450615-d3/crypto-tracker/crypto-web:latest --platform=managed --region=europe-west4 --allow-unauthenticated --env-vars-file=env.yaml --add-cloudsql-instances=elegant-plating-450615-d3:europe-west4:crypto-postgres
```

Application : ouvrez à partir de l'url suivante : [appli-sur-gcp](https://crypto-web-977395841698.europe-west4.run.app/). 

---

## 📎 Présentation

* Présentation : ouvrez à partir de l'url suivante : [Presentation](https://chrisyk59.github.io/crypto-school/). 
