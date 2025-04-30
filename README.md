<p align="center">
  <img src="docs/images/banner.png" alt="SmartAccess2030 Banner" width="700"/>
</p>

![Licence](https://img.shields.io/github/license/Hicham-Errihani/SmartAccess2030?style=for-the-badge&color=4caf50)
![Dernier commit](https://img.shields.io/github/last-commit/Hicham-Errihani/SmartAccess2030?style=for-the-badge&color=2196f3)
![Langage principal](https://img.shields.io/github/languages/top/Hicham-Errihani/SmartAccess2030?style=for-the-badge&color=ffeb3b)
![Taille du repo](https://img.shields.io/github/repo-size/Hicham-Errihani/SmartAccess2030?style=for-the-badge&color=ff9800)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ed?style=for-the-badge&logo=docker&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-Apache-black?style=for-the-badge&logo=apachekafka&logoColor=white)
![Spark](https://img.shields.io/badge/Spark-Streaming-f57c00?style=for-the-badge&logo=apachespark&logoColor=white)


---

## 🎯 Présentation du projet

### 🎫 **SmartAccess2030 — Système Intelligent de Gestion des Billets et du Public pour le Mondial 2030**

**SmartAccess2030** est une solution avancée de **gestion sécurisée des accès**, des **billets électroniques** et du **flux de spectateurs** pour les événements à très grande échelle, à commencer par la Coupe du Monde 2030.

Ce système innovant repose sur un pipeline technologique combinant **intelligence artificielle**, **Big Data**, et **traitement en temps réel**, afin d’optimiser la sécurité, l’organisation et l’expérience spectateur.

---

### 🚀 Fonctionnalités clés :

- 🎫 **Vérification rapide des billets numériques** (QR code, NFC, etc.)
- 🧠 **Reconnaissance faciale et vocale** pour authentification des détenteurs
- 📡 **Analyse temps réel des flux d’entrées** via **Kafka + Spark Streaming**
- 🔍 **Suivi des mouvements de foule** dans les stades via **capteurs et IA**
- 📊 **Tableaux de bord décisionnels** pour les organisateurs et les services de sécurité
- 📂 **Archivage complet** des sessions, accès, alertes et historiques de fréquentation

---

🎯 **Objectif principal** : assurer une gestion fluide, intelligente et ultra-sécurisée du public lors des matchs du **Mondial 2030**, tout en offrant aux organisateurs un outil de **pilotage temps réel**, de **détection de risques** et de **traçabilité complète**.

Ce projet répond aux standards des **grands événements internationaux**, dans une logique de **smart event**, **sécurité de masse**, et **expérience spectateur augmentée**.

---


## 📁 Structure
- `src/` : Code principal
- `scripts/` : Scripts de lancement
- `docker/` : Conteneurs Kafka + Elasticsearch
- `notebooks/` : Analyses exploratoires
- `data/` : Données brutes et traitées
- `models/` : Modèles IA (Whisper, etc.)

## 🚀 Installation

```bash
git clone https://github.com/<ton_user>/SmartAccess2030.git
cd SmartAccess2030
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
