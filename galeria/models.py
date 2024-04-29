from django.db import models

# Create your models here.

# O Django nos fornece a possibilidade de manipular banco de dados sem a necessidade de usar a linguagem SQL. 
# Acessando a pasta "galeria" e depois "models.py", neste arquivo criaremos estruturas de classes de orientação a objetos. 
# O Django "traduz" uma classe para uma tabela no banco de dados, chamamos essa ferramenta de Django ORM ("Object Relational Mapper").

# Após a classe, incluímos as colunas que desejamos. 
# Por exemplo, a coluna "nome" que importa do models.CharField() (usamos charField por ser uma string). 
# Dentro dos parênteses, colocamos o parâmetro max length, o null e o blank.

# O max length é o número limite de caracteres aceitos em um nome, o null inserimos igual a falso porque não pode ser um campo vazio, e o blank é falso também. 
# Logo após, vamos inserir a "descricao" que será um TextField. 
# A descrição será um texto mais longo comentando o que há na imagem. 
# Depois inserimos o campo "foto" (para exibirmos o caminho da foto), que será um CharField (porque desejamos o nome que colocaremos para cada foto), com as mesmas informações no parênteses.
class Fotografia(models.Model):# Model é uma classe
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
    
# CharField é do tipo String no banco de dados. 
# max_length é o varchar
# null = False é o Not null, ou seja Não nulo
# blank = False é uma string vazia é como se fosse: x = ""

# Construímos a classe que se tornou um model, isso acontece porque a classe representa uma tabela no banco de dados. 
# Para aplicarmos uma boa prática, após a classe criamos uma função que nos devolverá o nome de cada item.

# Comando para criar o arquvio migrations: python manage.py makemigrations
# Este arquivo é criado: Ele gera um documento nomeado "0001_initial.py", em "galeria > migrations".
'''
Migrations for 'galeria':
  galeria\migrations\0001_initial.py
    - Create model Fotografia
'''
# Esse documento é um relatório completo do que desejamos fazer: 
# criar uma nova tabela dentro do banco de dados, com todos os campos que inserimos no model. 
# Inclusive, ele gerou um id que usaremos como chave primária.

# Comando para criar as tabelas no bd a partir da nossa classe: python manage.py migrate
# Assim, ele aplica todas as migrações, inclusive, as que estavam pendentes. 









