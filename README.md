## Como utilizar
* Requisitos
  ``` 
  Para rodar o Django, você precisa ter o Python3 instalado
  ```
* Clone o projeto para seu computador
  ```bash
  $ git clone https://github.com/larissarsilva/avantia
  ```
* Inicie um ambiente virtual e instale as dependências
  ```bash
  Linux
  $ python3 -m venv env
  $ source env/bin/activate
  $ python3 -m pip install --upgrade pip
  $ pip install -r requirements.txt

  Windows
  python -m venv env
  env/Scripts/activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
* Rode as migrações
  ```bash
  $ python manage.py migrate
  ```
* Inicie o servidor
  ```bash
  $ python manage.py runserver
  ```

* Repositório frontend
  https://github.com/larissarsilva/frontAvantia
  
* Hospedagem
  https://sistemaavantia.000webhostapp.com/#/index
   
