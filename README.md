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

### Criar o banco de dados
```console
./manage.py migrate
```

### Popular os dados no banco
```console
./manage.py loaddata
```
### Rodar o shell
```console
 ./manage.py shell
 ```
