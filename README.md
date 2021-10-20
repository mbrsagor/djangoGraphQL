# djangoGraphQL
> GraphQl backend web application

### Installing Geospatial libraries
#### Dependency
- Python 3.8.5
- Django 3.1.5
- Postgres 12.3

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed `Homework` backend `API` app on Windows, you should have little problem getting up and running.


#### Run the project in your local development environment.
```
git clone https://github.com/mbrsagor/djangoGraphQL.git
cd djangoGraphQL
virtualenv venv --python=python3.8
source venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

##### Example of GraphQL demo:-
- Query:
```python
query{
  users{
    edges{
      node{
        username
        email
      }
    }
  }
}
```
- Mutation:
```

```

###### Install packages:
- https://pypi.org/project/graphene-django
- https://pypi.org/project/django-graphql-jwt
- https://pypi.org/project/django-graphql-auth

