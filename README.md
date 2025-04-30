<p align="center">
  <img src="docs/images/banner.png" alt="SmartAccess2030 Banner" width="700"/>
</p>

![GitHub License](https://img.shields.io/github/license/Hicham-Errihani/SmartAccess2030?color=green)
![Dernier commit](https://img.shields.io/github/last-commit/Hicham-Errihani/SmartAccess2030?color=blue)
![Langage principal](https://img.shields.io/github/languages/top/Hicham-Errihani/SmartAccess2030?color=yellow)
![Taille du repo](https://img.shields.io/github/repo-size/Hicham-Errihani/SmartAccess2030?color=orange)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
# SmartAccess2030

Application intelligente de gestion d’accès industriel : badges, voix, alertes, avec Kafka, Spark, Elasticsearch, IA.

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
