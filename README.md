# TP5 - MikroTik REST API

## Prerequis
- MikroTik CHR v7 avec `/ip service enable www`
- Python 3 + `py -m pip install requests python-dotenv`

## Configuration
Creer un fichier `.env` (non versionne, liste dans .gitignore) :

    DEVICE_HOST=192.168.233.162
    DEVICE_USER=api-user
    DEVICE_PASSWORD=motdepasse

## Utilisation
- `py api_crud.py` : GET, POST, PATCH, DELETE sur /ip/address
- `py configure_router.py` : cree les routes statiques manquantes (idempotent)
