# teste-interface-sistemas

# guia de instalação do projeto

## Windows
1. Faça download do projeto
2. No diretório do projeto digite os comandos:
```sh 
python -m venv venv</li>
```
```sh 
.\venv\scripts\activate</li>
```
```sh 
pip install -r requirements.txt</li>
```sh 
python manage.py runserver </li>
```
<p>Caso surja a excessão "OSError: cannot load library 'gobject-2.0-0': error 0x7e...", siga o manual de instalação do GTK em https://www.gtk.org/docs/installations/windows/</p>
<p>
Baixe a versão mais recente da biblioteca glib no site oficial: https://developer.gnome.org/glib/. Certifique-se de baixar a versão compatível com a sua arquitetura (32 bits ou 64 bits).<br/>

Extraia o arquivo ZIP baixado para uma pasta de sua escolha.<br/>

Abra o prompt de comando do Windows como administrador e navegue até a pasta onde você extraiu os arquivos.<br/>

Execute os seguintes comandos no prompt de comando:
<br/>
```sh
cd glib-<versão>\glib
```
```sh
nmake -f makefile.msc
```
</p>

## Linux/MacOs
1. Faça download do projeto
2. No diretório do projeto digite os comandos:

```sh 
python3 -m venv venv
```
```sh 
source venv/bin/activate
```
```sh 
pip install -r requirements.txt
```
```sh 
python3 manage.py runserver
```


### Para MacOs: instale a biblioteca Weasyprint, responsavel pela geração de PDF

```sh
brew install cairo pango gdk-pixbuf libffi
```
```sh
brew install weasyprint
```
 

### Para Linux: instale a biblioteca Weasyprint, responsavel pela geração de PDF
```sh 
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

```sh 
pip3 install weasyprint
``` 


# Guia de uso do sistema

## Login

1. usuário: admin
2. email: admin@email.com
3. senha: 1234

### Ao logar, você será redirecionado para a dashboard do sistema

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


