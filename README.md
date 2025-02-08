# 💰 Projet-3-Cryptomonnaie-Wild-Data-Hub

C'est le résultat du deuxième projet réalisé lors de ma formation en tant que _DATA ANALYST_ à la **Wild Code School** à Lille.

## 🎯 Objectif du Projet :

Le système de recommandation de films est mis en place pour le compte d'un gérant de cinéma de la Creuse afin de lui aider à choisir des films pour ses clients locaux.
Les KPIs sont définis pour évaluer les films susceptibles de correspondre aux goûts locaux.

1. Période de sortie des films :

Films sortis entre 1975 et 1995.

2. Nationalité des films :

Origine : Française et Américaine.

3. Catégories :

Films appartenant aux genres :
     Comédie,
     Famille,
     Drama
   
4. Notes des films :

Score supérieur ou égal à 6 /10 sur les plateformes de notation (e.g., IMDb, TMDB).

5. Durée des films :

À définir selon les préférences locales (proposer des durées moyennes entre 80 min et 240 min).

## ✅ Etapes : 

#### Semaine 1 :  
Appropriation et première exploration des données     
Outils principaux : jupyter, pandas, gzip   

![Capture15](https://github.com/user-attachments/assets/8a387e9e-f3ca-48f2-945a-de246742786d)

![Capture2](https://github.com/user-attachments/assets/95597d23-bb75-4230-9a31-08faff664343)

![Capture3](https://github.com/user-attachments/assets/0885c1f6-8e1f-4b33-946d-4572f9d3db3f)

![Capture4](https://github.com/user-attachments/assets/c3f91bd0-06c3-4590-93de-23c83437e821)

#### Semaine 2 : 
Jointures, filtres, nettoyage,     
Outils principaux : jupyter, pandas

![Capture5](https://github.com/user-attachments/assets/36e0fd44-b3bb-4b4c-b310-765e2a7c83b2)

![Capture6](https://github.com/user-attachments/assets/2e458362-855b-4472-bf58-49f938247165)

![Capture7](https://github.com/user-attachments/assets/41220518-930b-4845-a233-4eae2dccb772)

#### Semaine 3 : 
Recherche de corrélation, visualisation     
Outils principaux : google colab, pandas, seaborn, matplotlib

![Capture8](https://github.com/user-attachments/assets/36532d5f-4911-40dc-9952-b392ee903287)

![Capture9](https://github.com/user-attachments/assets/ec2d184d-192e-4dc2-925f-c3b156f2e11e)

![Capture10](https://github.com/user-attachments/assets/14c38f5b-e38d-4d75-9f58-c77aa0c49f11)

![Capture11](https://github.com/user-attachments/assets/a695aed4-a6b9-45d4-935c-abec6825b53f)

![Capture12](https://github.com/user-attachments/assets/52c5e3be-8604-46f9-8f0c-5c0a952a6543)

![Capture13](https://github.com/user-attachments/assets/e386ddfa-554d-41dd-bb8f-40f2b33be90e)

![Capture14](https://github.com/user-attachments/assets/9aeba95f-8231-4c65-9b40-2ed3e28d32fa)

#### Semaine 4 :   
Machine learning, recommandations    
Outils principaux : google colab, scikit-learn, nltk

![Capture16](https://github.com/user-attachments/assets/5905b835-1e9d-4c3e-ab6a-a4e954f1c939)

![Capture17](https://github.com/user-attachments/assets/13c0718a-2550-42f0-b444-516982beeca0)

![Capture18](https://github.com/user-attachments/assets/914a4c23-3b88-47b5-ab0c-7c68839f7ab7)

![Capture19](https://github.com/user-attachments/assets/c0f2c0ab-43eb-42d2-9e8e-423e9cb16cdc)

![Capture20](https://github.com/user-attachments/assets/df871ad6-a760-4fec-9f78-e4568669b488)

![Capture21](https://github.com/user-attachments/assets/b5046d80-bfe8-4c76-a67b-578025b2940d)

#### Semaine 5 :  
Affinage, présentation et Demo Day
Outils principaux : google colab, google slide, streamlit 

![Capture22](https://github.com/user-attachments/assets/e651ee0d-eab8-4bac-ac41-7b872bcb9389)

## 🎬 Source des Données :  
-[Données IMDb](https://datasets.imdbws.com/)   
-[Données TMDB](https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view)   
-[Explication datasets](https://www.imdb.com/interfaces/)  


## 📎 Livrables

* Exploration et infiltrage des données : ouvrez les notebooks correspondants dans Jupyter : [Notebook](https://github.com/Sopanha2020/Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films/blob/main/Notebooks/TMDB%20IMDB%20Data%20Wrangling.ipynb).  
* Nettoyage et visualisation des données : ouvrez les notebooks correspondants dans Google Colab : [Notebook](https://github.com/Sopanha2020/Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films/blob/main/Notebooks/Film_Recommendation_System.ipynb).
* Application : ouvrez à partir de l'url suivante : [appli-streamlit](https://projet-2-group-moving-frame-systeme-de-recommandation-de-films.streamlit.app/). 

## 📡 Installation

0. Prérequis d'installation
    
    Python >= 2.12
    
1. Clonez le dépôt:
    ```sh
    git clone https://github.com/Sopanha2020/Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films.git
    ```
2. Allez dans le répertoire du projet:
    ```sh
    cd Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films
    ```
3. Installez les dépendances:
    ```sh
    pip install -r requirements.txt
    ```
4. Ajouter la clé API tmdb pour utilisation en local:  
    ```
    Copier votre clé API tmdb dans le fichier api.txt
    ```
5. Lancer l'application en local:
    ```sh
    streamlit run app.py
    ```
# Crypto Tracker 🐍📈 – Central Portfolio Tracking

[![Python](https://img.shields.io/badge/Made%20with-Python%203.x-blue.svg?style=flat-square&logo=Python&logoColor=white)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Powered%20by-Django%203.x-green.svg?style=flat-square&logo=Django&logoColor=white)](https://www.djangoproject.com/) 

### Easy asset tracking – at a glance 🚀

![Application Screenshot](media_files/sample.png)

Dashboard to centrally monitor current crypto portfolio developments, by providing an overview of their current value.
Values can either be displayed by their current *Overall value* (requires adding Purchases) or by their *Current value*
(indicated by the <sup>`V`</sup> next to the number).

The current course data is polled from CoinMarketCap's REST API and stored in the database. The API allows you to make 
a maximum of 333 points worth of daily requests (~1 request / 5min). Querying multiple cryptos may increase the 
amounts of points required per API call, thus requires increasing the time between requests.

## ⭐ Features

💸 Personalized crypto portfolio tracking  
💸 Centrally keep an eye on its current value  
💸 Quickly react to emerging changes  
💸 Show overall or current value  
💸 Convert values into local currency  
💸 Chart crypto course  
💸 Soon: alerting via Pushover  

## Deployment 👾

Deployment is best done via Docker – can also be achieved by installing each component manually,
but this is quite tedious, so I'm not going to detail that here.

This application is meant to be run behind e.g. Traefik or a WAF (Web Application Firewall) that handles 
the SSL certificates, such as LetsEncrypt.

Once rolled out the application is reachable via `http://<ip-address>:5000`

### Requirements

* [Docker](https://docs.docker.com/get-docker/)  
* [docker-compose](https://docs.docker.com/compose/install/)  
* [CoinMarketCap API Key](https://coinmarketcap.com/api/)

### Setup

All relevant parameters are controlled via environment variables that are passed
to the docker-compose stack. For further reference review the `config/settings.py` file.

```bash
mv dotenv-sample .env
vi .env
```

* `SECRET_KEY` just set it
* `POSTGRES_PASSWORD` database password
* `SITE_HOSTNAME` name your site is going to be reached at. Multiple values can be space-separated
* `ALLOWED_HOSTS` allowed host headers - should have `SITE_HOSTNAME` values + IPv4 of your Docker host  
* `COINMARKET_KEY` your CoinMarketCap API key used for requests
* `TARGET_CURRENCY` if you wish to convert the USD course + price data to your local currency

### Docker Rollout

```bash
mv docker/docker-compose .
mv docker/rebuild-shortcut rebuild
chmod +x ./rebuild
./rebuild
```

Everything should now be running smoothly. Use a service (`cron` will also do) to start
the process automatically at boot. Alternatively you can also add `-d` to the `docker-compose`
command in `rebuild` and run it manually at each startup.

## Usage 🚀

Once running, access the admin panel via `http://<ip-address>:5000/admin` 
To access it, you will need to create a user using `chmod +x docker/manage-shortcut; ./docker/manage-shortcut createsuperuser`  

Login with the credentials just created, to then add the `Cryptos` you wish to track. 
Once added, `Purchases` enable you to indicate your assets/amount for each crypto.


[![Buy me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/alfonsrv)  

---

## TODOs 🛠️

- Resize image  
- Price Alerting

