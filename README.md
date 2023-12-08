# Desenvolvimento de Sistemas Web - Atividades

Aqui estão as atividades desenvolvidas durante a disciplina de Desenvolvimento de Sistemas Web.

- **[Atividade 04](004)**
  - Crie um ambiente virtual;
  - Utilizando o ambiente virtual, crie um projeto Django com o nome de sua preferência;
  - Adicione o .gitignore disponibilizado ao projeto;
  - Inicie o git no projeto e utilize também o gitflow;
  - Utilize o gitflow para iniciar o desenvolvimento de uma nova tarefa;
  - Em seguida, crie uma aplicação com o nome de sua preferência;
  - A aplicação criada deverá rodar um “hello world” ao acessar a rota raiz do sistema web;
  - Mescle a nova tarefa à develop;
  - Disponibilize a nova versão do software para produção;
  - Faça o push do projeto no seu GitHub.

- **[Atividade 05](005)**
  - Utilize os arquivos do projeto anexo e faça:
    - Crie um projeto Django;
    - Crie um app Django;
    - Inclua as páginas index e login do projeto anexo no projeto Django;
    - Trabalhe com um template base que manterá todos os elementos comuns entre as duas páginas;
    - O JavaScript, CSS e imagens comuns às páginas deverão ficar em uma pasta de arquivos estáticos do próprio projeto;
    - As imagens correspondentes ao conteúdo da página deverão ficar em uma pasta de arquivos estáticos da aplicação Django;
    - A logomarca do site deverá direcionar para a página inicial do site;
    - O ícone de perfil, no canto direito superior deverá levar o usuário para a página de login.
  - Por fim, suba seu projeto para o GitHub e disponibilize o link do repositório como resposta.

- **[Atividade 06](006)**
  - Crie um projeto Django para a produção de um Sistema Web para um Sebo de discos.
  - A princípio, crie um model para disco com os seguintes atributos:
    - Nome;
    - Descrição;
    - Selo fonográfico;
    - Ano;
    - País;
    - Gênero;
    - Quantidade.
  - Inclua o disco no sistema administrativo e faça pelo menos 5 inserções de dados.

- **[Atividade 07](007)**

**1. Utilizando a atividade 6, faça as seguintes modificações:**
- O selo fonográfico deve deixar de ser apenas um atributo de texto do disco e passar a ser uma classe. Um disco deve ter apenas um selo fonográfico e um selo fonográfico poderá estar em vários discos;
- Crie um modelo Artista. O modelo artista poderá possuir vários discos e um disco poderá ser gravado por vários artistas.
- 
**2. A partir do admin do django, crie, no mínimo, 7 entradas para cada modelo.**

**3. Utilizando o shell do django, faça as seguintes consultas:**
- Liste todos os discos;
- Liste todos os artistas de um disco específico;
- Quais os artistas que gravaram seus discos no selo Sony Music.

**Envio da atividade**
- A atividade deverá ser enviada a partir do github. Para isso, crie uma granch chamada relacionamentos e envie o link nesta atividade.
- Para o item 3, consultas, gere o sql da consulta e envie em um documento de texto também nesta atividade


- **[Atividade 09](009)**
  
**utilizando o código produzido na atividade 8, crie as views e templates necessários para as seguintes ações:**
- Exibir a lista de discos cadastrados;
- Exibir os detalhes de um disco.

- Crie uma interface utilizando html e css organizada e interessante.

- Crie uma branch chamada atividade9 para armazenar o código dessa atividade.
