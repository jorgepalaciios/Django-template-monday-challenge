# Django Template Project
Django template for future projects. Includes all the packages needed to have a basic project with minimal setups. It also work as a template in Gitlab to create new repositories.

## Stack
- Python 3.10
- Django 3.2
- Django Rest Framework 3.14
- Celery 5.2.*
- PostgreSQL 12
- Redis 7.0.4
- Docker 20.10-*
- Docker compose 2.10.*
- node 16.*
- npm 8.19.*

## Build containers and run project
The project is builded over Docker and Docker compose. So there's no need to set a virtualenv, just compose the application and start to code.
### Development
For local development or test instances, this is the easiest choice to run the aplication.
```
docker compose up -d --build
```
### Production
For instances that are showed to a clien (QA) or to deploy it in a production environment.
```
docker compose up -d -f docker-compose.prod.yml --build
```
## Generate and compile translations
This repo has the basic setup to support internacionalization. So your future project can support multiple languages. Just need to integrate in frontend request the Accept-language header to return responses in supported languages. If the header is not in the request, the default language in used (en).

You are free to choose you're default and supported languages.

Before compile or add translations in one language, you need to access to you api container. If you use docker desktop, just access to container cli tab. In case that you need to use the terminal.

```
docker exec -it <container_id/name> sh
```

To add/update translation messages, run

```
python manage.py makemessages -l <language code: es>
```

This will generate a directory with the languade code name in locales folder. You're messages to translate are located in django.po file.

Once you complete to set you're translated messages. Run next command to compile messages.

``` 
python manage.py compilemessages
```

This generates a .mo file

## Semantic commits and Changelog
Changelog is a file to keep registers of changed between version. For more information about what should have a CHANGELOG file visit this link [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). For a spanish version look up [Mantenga un Changelog](https://keepachangelog.com/es-ES/1.0.0/).

Changelog file uses semantic versioning to keep registers of changes. To know more about it check this link [Semantic Versioning](https://semver.org/).

It's also required that commits made by developers follow semantic commit instructions to generate the Changelog file and include all changes made.

Semantic commit instructions are detailed in this Github Gits discussion [Semantic Commit](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

Before generate a Changelog, install node dependencies
```
npm install
```

First version it's already done by default, but if you need to restart Changelog, delete Changelog file, adjust package.json version and run:
```
npm run release -- --first-release
```
This will generate changelog file with version adjusted in package.json file

As was defined in SemVer documentation, software versions are defined as a composition of 3 version numbers x.y.z where:

- x -> it's major version. If this number increases it means that it's a major change. This means that doesn't have compatibility with previous versions.

- y -> it's a minor version. This version increase it's usually due to adding a feature to the software and doesn't mean that there's going to be compatibility issues.

- z -> path version. This increses are done when a fix it's made.

To update changelog increasing patch version. 
```
npm run release:patch
```

To update changelog increasing minor version. 
```
npm run release:minor

```

To update changelog increasing major version. 
```
npm run release:major
```
