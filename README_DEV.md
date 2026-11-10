# CDKBusness — environnement de développement

## Prérequis
- Python 3.12+
- Git
- Visual Studio Code (recommandé)

## Installation sous Windows PowerShell

```powershell
git clone https://github.com/flexau/projet-ecommerce.git
cd projet-ecommerce
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/ dans le navigateur.

## Structure
- `config/` : configuration Django
- `apps/core/` : accueil et pages communes
- `templates/` : templates HTML
- `static/` : CSS, JavaScript et ressources statiques
- `media/` : médias téléversés (non versionnés)

## Périmètre actuel
Le socle Django et la première page d'accueil sont en place. Les véhicules affichés sur la page d'accueil sont des données de démonstration ; le catalogue connecté à la base de données sera développé dans une prochaine étape. Aucun paiement réel n'est activé.
