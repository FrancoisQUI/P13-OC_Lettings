## Résumé
___
Site web d'Orange County Lettings

## Développement local
___
### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Tailwind CSS

Ce projet utilise tailwind CSS pour la mise en place de styles. En développement pour mettre a jour automatiquement les fichiers CSS il faudra lancer la commande : ```python manage.py tailwind start```

#### Avant chaque push 

Ne pas oublier de lancer les commandes suivante si vous avez ajouté des fichiers statics ou modifier le style de l'application :

```sh
python manage.py tailwind build 
python manage.py collectstatic 
```

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Utiliser la pipeline CI/CD
___

### Principe de fonctionnement

#### Résumé

Le projet est configuré pour un pipeline CI/CD utilisant CirlcleCI / Docker / Heroku

À chaque push sur la branche *"main"* dans **git-hub**, **circleci** déclanchera une série de test, une vérification pep 8, la construction et le deploiement d'une image docker sur **le docker-hub**, puis un déploiement de l'image docker sur **heroku**

#### Déroulement

1. Le developpeur push sur git-hub
2. Circle-CI prends le relai
   1. Construction et test
      1. Il installe le projet sur une machine virtuelle
      2. Il effectue les tests unitaires avec pytest
      3. Il lance le linter Pep8 *flake8* (et bloque le processus en cas de non-respect de regales configurées)
   2. Construction d'une image Docker 
      1. Il se connecte au compte docker
      2. Il crée l'image docker
      3. Il pousse l'image vers le site docker-hub
   3. Déploiement de l'image sur heroku
      1. Il installe heroku sur l'image circleCI
      2. Il crée l'application Heroku si elle n'existe pas
      3. Il ajoute les variables d'environnement dans Heroku
      4. Il récupère l'image docker
      5. Il la déploie sur heroku

#### Variables d'environnement

Les variables d'environnement sont utilisés par ce projet et a tous les niveaux de développement.
Vous trouverez ci-dessous un tableau récapitulatif des variables utilisées et des endroits ou elles doivent être renseignées

|   Variable Name | type | exemple                                                | Origin                   | .env | circleCI | docker run | heroku |
|----------------:|:----:|--------------------------------------------------------|--------------------------|:----:|:--------:|:----------:|:------:|
|           DEBUG | bool | true                                                   | settings.py              |   X  |     X    |     (X)    |    *   |
|      SECRET_KEY |  str | fp$9^593hsriajg...                                     | settings.py              |   X  |     X    |      X     |    *   |
|   ALLOWED_HOSTS | list | [0.0.0.0, "localhost"]                                 | settings.py              |   X  |     X    |     (X)    |    *   |
|            PORT |  int | 8000                                                   | settings.py              |   X  |          |     (X)    |        |
|      SENTRY_DSN |  str | "https://30[...]04@o1[...]19.ingest.sentry.io/6[...]4" | Sentry App Configuration |   X  |     X    |      X     |    *   |
|    DOCKER_LOGIN |  str | username                                               | docker-hub account       |      |     X    |            |        |
| DOCKER_PASSWORD |  str | motdepasse123/                                         | docker-hub account       |      |     X    |            |        |
|  HEROKU_API_KEY |  int | 2103871[...]02847143                                   | heroku account           |      |     X    |            |        |
| HEROKU_APP_NAME |  str | application-exemple                                    | heroku account           |      |     X    |            |        |


- ```X``` signifie qu'il faut la renseigner
- ```(X)``` signifie qu'elle peut etre renseignée si la valeur par défaut ne convient pas
- ```*``` signifie qu'elle est utilisée et renseignée automatiquement à condition qu'elle ait bien éte configurée dans circleCI

#### Configurer la pipeline
 Compte necessaires : 
- [Github](https://github.com/)
- [CircleCI](https://app.circleci.com/)
- [Heroku](https://www.heroku.com)
- 

#### Sentry

#### Lancer l'image docker en local

- installer docker si necessaire

- lancer la commande :
  - avec les informations entre crochet peuvent etre remplacées par les informations présente dans vos fichiers d'environnement
  - le couple {app_name}:{tag} correspond a l'image que vous voulez lancer (voire docker-hub)

```shell
  docker run -p 8000:8000 -e PORT={port} -e SECRET_KEY={secret_key} -e DEBUG="true" -e ALLOWED_HOSTS={allowed_host} -e SENTRY_DSN={sentry_dsn} {app_name}:{tag}
```


