# 💰 Projet-3-Cryptomonnaie-Wild-Data-Hub

Ceci est le fruit du troisième projet que j'ai conçu dans le cadre de ma formation en tant que _DATA ANALYST_ à la **Wild Code School** de Lille.

![Image](https://github.com/user-attachments/assets/1af4003b-06d5-43a0-9353-c6b42e03d719)

## 🎯 Objectif du Projet :

Tableau de bord pour surveiller de manière centralisée les évolutions actuelles du portefeuille de crypto-monnaies, en fournissant un aperçu de leur valeur actuelle, de l'évolution des prix sur 24 heures et des alertes de tendance.
Les données de cours actuelles sont interrogées à partir de l'API REST de CoinMarketCap et stockées dans postgreSQL. L'API vous permet de faire
un maximum de 333 points de requêtes quotidiennes (~1 requête / 5 min). L'interrogation de plusieurs cryptos peut augmenter le
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
💸 Bientôt : alertes via discord 

---

## 👾 Déploiement

Le déploiement est recommandé via Docker. Il est également possible d’installer chaque composant manuellement, mais cette méthode est fastidieuse et ne sera donc pas détaillée ici.

Cette application est conçue pour être exécutée derrière un proxy inverse comme **Traefik** ou un **pare-feu applicatif (WAF)** qui gère les certificats SSL, tels que **LetsEncrypt**.

Une fois déployée, l’application sera accessible via :

```
http://<adresse-ip>:5000
```

### 📌 Prérequis

- [Docker](https://docs.docker.com/get-docker/)  
- [docker-compose](https://docs.docker.com/compose/install/)  
- [Clé API CoinMarketCap](https://coinmarketcap.com/api/)

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

```bash
mv docker/docker-compose .
mv docker/rebuild-shortcut rebuild
chmod +x ./rebuild
./rebuild
```

L’application devrait maintenant être opérationnelle.  
Pour un démarrage automatique au **boot**, utilisez un service système (ou `cron`).  
Sinon, ajoutez `-d` à la commande `docker-compose` dans le script `rebuild` pour le lancer manuellement à chaque démarrage.

---

## 🔥 Utilisation

Une fois l’application lancée, accédez au **panneau d’administration** via :  

```
http://<adresse-ip>:5000/admin
```

Pour y accéder, créez un utilisateur administrateur avec la commande suivante :  

```bash
chmod +x docker/manage-shortcut
./docker/manage-shortcut createsuperuser
```

Connectez-vous avec les identifiants créés, puis ajoutez les cryptomonnaies que vous souhaitez suivre.  
Ensuite, utilisez l’onglet **"Purchases"** pour indiquer vos actifs et montants détenus.

---

## 🛠️ TODOs

- Redimensionner les images  
- Ajout d'alertes de prix

## 📎 Livrables

* Application : ouvrez à partir de l'url suivante : [dashboard-pythonanywhere](https://projet-2-group-moving-frame-systeme-de-recommandation-de-films.streamlit.app/). 
