# De SQL para ORM Django
Criei esse projeto para criar os exemplos para a palestra que fiz na The Developer's Conference (TDC) 2017.

## Procedimentos
### Clone o repositório

```console
git clone git@github.com:beatrizuezu/de-sql-para-orm-django.git de-sql-para-orm-django
cd de-sql-para-orm-django
```
### Crie um virtualenv com Python 3.x e ative
```console
virtualenv .env -p python3
source .env/bin/activate
```
### Instale as dependencias
```console
pip install -r requirements.txt
```

### Crie um banco chamado `Exemplo` no MySQL
```mysql
create database exemplo;
```

### E execute as migrations
```console
./manage.py migrate
```

### Popular os dados no banco
```console
./manage.py loaddata categorias produtos
```
### Rodar o shell
```console
 ./manage.py shell
 ```

### Seguir os passos dessa [publicação](https://medium.com/@beatrizuezu/visualizando-query-sql-a-partir-do-orm-django-5771370a9c55)
