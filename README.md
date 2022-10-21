# Django + GraphQL

This repository contains a backend application boilerplate powered by Django
and Graphene for creating a modern, API first architecture.

As much as possible avoid modifying files forked from this repo to avoid 
conflicts when pulling.  Most functionality traditionally requiring changes
to project-wide files such as `settings.py` can be overridden.

## Features

### Environment variables

Support has been added for loading environment variables from files such as
`.env.local`, using a mechanism similar to 
[Next.js](https://nextjs.org/docs/basic-features/environment-variables)

```dotenv
# .env.local
SECRET_KEY=somefancysecret
```

In general only one .env.local file is needed. However, you can also specify\
environment variables that will be loaded in development
(`python manage.py runserver` and via `docker compose`) or production.

The root directory of the project will be scanned for the following files:

    * `.env` (all environments)
    * `.env.development` (development)
    * `.env.production` (production).
    * `.env.local` (your machine) **always overrides**

> .env, .env.development, and .env.production files should be included in your
> repository as they define defaults. .env*.local should be added to .gitignore, as those files are intended to be ignored. .env.local is where secrets can be stored.

## Getting started

To use this as a base for your project, start by creating a new fork.

### Creating apps

Functionality should be encapsulated inside apps.

```bash
python manage.py startapp <myapp>
```

> For more information on django commands, consult their excellent documentation
> [here](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)


## Features

1. Translations

## City data

City data is provided by the cities_light package. Run 
`python manage.py cities_light` to download city data.

./manage.py cities_light_fixtures dump
./manage.py cities_light_fixtures load
