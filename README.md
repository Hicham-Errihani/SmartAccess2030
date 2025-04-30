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
