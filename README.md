# teste-interface-sistemas

# guia de instalação do projeto

## Windows
1. Faça download do projeto
2. No diretório do projeto digite os comandos:
<ol>
    <li>python -m venv venv</li>
    <li>.\venv\scripts\activate</li>
    <li>pip install -r requirements.txt</li>
    <li>python manage.py runserver </li>
</ol>


## Linux/MacOs
1. Faça download do projeto
2. No diretório do projeto digite os comandos:

```python3 -m venv venv```
```source venv/bin/activate```
```pip install -r requirements.txt```
```python3 manage.py runserver```


3. Para MacOs: instale a biblioteca Weasyprint, responsavel pela geração de PDF

```brew install cairo pango gdk-pixbuf libffi</li>```
```<li>pip install WeasyPrint</li>```
 

4. Para Linux: instale a biblioteca Weasyprint, responsavel pela geração de PDF
```sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info```

```pip3 install weasyprint``` 


# Guia de uso do sistema

## Login

1. usuário: admin
2. email: admin@email.com
3. senha: 1234

### Ao logar, você será redirecionado para a dashboardo do sistema

## Cadastro de receituário

1. Na tabela 'Principal' clique em Receituário
2. Clique no botão adicionar receituario
3. Informe os respectivos campos
4. Clique em salvar

## Gerando PDF para impressão de receituário
1. Em receituário, selecione aquele cujo pdf será gerado
2. Nas ações, selecione a opção Gerar receituário
3. Clique em ir
4. Você será redirecionado para a página de visualização do documento
5. Clique em 'Imprimir'


