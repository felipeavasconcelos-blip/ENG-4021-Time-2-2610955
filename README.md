# MedMap

O MedMap é uma aplicação web de saúde preventiva. Muitas pessoas não sabem quais exames, consultas e vacinas precisam fazer, e o histórico de saúde da família costuma ficar só na memória. No MedMap, a pessoa cadastra o seu perfil, o histórico de saúde da família e os seus hábitos, e a aplicação mostra quais cuidados ela precisa e quando fazê-los.

**Disciplina:** ENG4021 - Projeto Integrado
**Instituição:** PUC-Rio
**Professor:** Alexandre Meslin
**Grupo:** Time 2 (turma 33B)

## Status do projeto

Em desenvolvimento. As telas já foram feitas em HTML e CSS e já estão no projeto Django, com uma rota para cada tela. A próxima etapa é ligar as telas ao banco de dados.

## Sumário

- [Membros do grupo](#membros-do-grupo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Protótipos](#protótipos)
- [Telas](#telas)
- [Fluxo de uso](#fluxo-de-uso)
- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Como rodar o projeto](#como-rodar-o-projeto)
- [Exemplo de uso](#exemplo-de-uso)
- [Documentação adicional](#documentação-adicional)
- [Melhorias futuras](#melhorias-futuras)
- [Licença](#licença)

## Membros do grupo

| Nome | Função | GitHub |
| --- | --- | --- |
| Felipe Fraga | Desenvolvedor | [ffraga1](https://github.com/ffraga1) |
| Felipe Vasconcelos | Desenvolvedor | [felipeavasconcelos-blip](https://github.com/felipeavasconcelos-blip) |
| Gael Moraes | Desenvolvedor | [gaelmoraess](https://github.com/gaelmoraess) |
| Letícia Virgini | Desenvolvedora | [leticiavirgini-png](https://github.com/leticiavirgini-png) |
| Rafaela Ossaille | Desenvolvedora | [rafaelaossaille](https://github.com/rafaelaossaille) |
| Thiago Braz | Desenvolvedor | [thiagobraz524](https://github.com/thiagobraz524) |

## Funcionalidades

- Criar conta, entrar na conta e recuperar a senha
- Editar e excluir a conta
- Listar os usuários cadastrados
- Registrar o histórico de saúde da família
- Check-up Inteligente: sugerir consultas, exames e vacinas de acordo com a idade, o sexo, os hábitos e o histórico familiar
- Calendário de cuidados com lembretes
- Página de artigos com dúvidas comuns sobre saúde preventiva

## Tecnologias

### Linguagens

- **HTML** e **CSS**: telas do site
- **Python**: back-end

### Frameworks e bibliotecas

- **Django**: back-end, rotas das telas e banco de dados

### Ferramentas

- **VS Code**: editor de código
- **Git** e **GitHub**: controle de versão
- **SQLite**: banco de dados padrão do Django
- **Figma** e **Lovable**: design e protótipos
- **Kanban do Moodle**: organização das tarefas de cada sprint

## Protótipos

- [Design no Figma](https://www.figma.com/design/hC0vYHw3bqj2FYwUQB0ftd/Figma-time-2-ENG-4021?node-id=0-1&t=hGo2DWpb9pkVvA3d-1)
- [Protótipo no Figma](https://www.figma.com/make/p2kqCzxgwWj3IYYZ3roUE1/MedMap--atualizado-?t=l5wNJmRCFwn9r36C-1)
- [Protótipo no Lovable](https://lovable.dev/projects/603a8d27-59a2-4160-a01c-2c9390db849e)

## Telas

As telas ficam em `ArquivosDeCodigo/MeuSite/templates`, e o CSS de cada uma fica em `ArquivosDeCodigo/MeuSite/static/css`. A tela de listar usuários ainda está em `ArquivosDeCodigo/TelaDeLogin` e vai passar para o Django na próxima etapa.

| Tela | Arquivo | Endereço | O que faz |
| --- | --- | --- | --- |
| Página inicial | `home.html` | `/` | Tela de boas-vindas do usuário |
| Login | `Tela.html` | `/Tela/` | Entrar na conta com e-mail e senha |
| Criar conta | `CriarConta.html` | `/CriarConta/` | Cadastro de um novo usuário |
| Esqueci senha | `EsqueciSenha.html` | `/EsqueciSenha/` | Recuperar o acesso à conta |
| Como usar | `ComoUsar.html` | `/ComoUsar/` | Explica como usar o MedMap |
| Artigos | `Artigos.html` | `/Artigos/` | Textos sobre saúde preventiva com fontes oficiais |
| Edição de usuário | `EdicaoUsuario.html` | `/EdicaoUsuario/` | Alterar os dados da conta |
| Remoção de usuário | `RemocaoUsuario.html` | `/RemocaoUsuario/` | Excluir a conta |
| Listar usuários | `ListarUsuarios.html` | ainda sem rota | Mostra os usuários cadastrados, com opções de editar e remover |

### Login
Tela de entrada, onde o usuário digita o e-mail e a senha.

![Tela de login](Imagens/login.png)

### Criar conta
Formulário de cadastro de um novo usuário.

![Tela de criar conta](Imagens/criar-conta.png)

### Esqueci senha
Tela para recuperar o acesso à conta pelo e-mail.

![Tela de esqueci senha](Imagens/esqueci-senha.png)

### Página inicial
Tela de boas-vindas, com os principais recursos do MedMap.

![Página inicial](Imagens/pagina-inicial.png)

### Como usar
Passo a passo de como usar o MedMap.

![Tela como usar](Imagens/como-usar.png)

### Artigos
Textos curtos sobre exames, vacinas e histórico familiar, com fontes oficiais.

![Página de artigos](Imagens/artigos.png)

### Edição de usuário
Tela para alterar os dados da conta.

![Tela de edição de usuário](Imagens/edicao-usuario.png)

### Remoção de usuário
Tela para excluir a conta, com aviso e confirmação.

![Tela de remoção de usuário](Imagens/remocao-usuario.png)

### Listar usuários
Lista dos usuários cadastrados, com botões para editar e remover cada um.

![Tela de listar usuários](Imagens/listar-usuarios.png)

## Fluxo de uso

1. Entre na tela de **Login**. Se ainda não tiver conta, clique em **Criar conta**.
2. Se esquecer a senha, use a tela **Esqueci senha**.
3. Depois de entrar, você chega na **Página inicial**.
4. Em **Como usar**, você vê o passo a passo do MedMap.
5. Em **Artigos**, você lê respostas simples sobre exames, vacinas e histórico familiar.
6. Para mudar os seus dados ou excluir a conta, use as telas de **Edição** e **Remoção de usuário**.

```mermaid
flowchart LR
    A[Login] --> B[Criar conta]
    A --> C[Esqueci senha]
    A --> D[Página inicial]
    B --> A
    D --> E[Como usar]
    D --> F[Artigos]
    D --> G[Listar usuários]
    G --> H[Edição de usuário]
    G --> I[Remoção de usuário]
```

## Arquitetura do projeto

As telas em HTML e CSS ficam como templates do Django. Cada tela tem uma view e uma rota. O próximo passo é guardar os dados no banco de dados.

```mermaid
flowchart LR
    A[Telas em HTML e CSS] --> B[Django: views e rotas]
    B --> C[(Banco de dados)]
```

### Estrutura de pastas

- `ArquivosDeCodigo/manage.py`: arquivo para rodar o projeto Django
- `ArquivosDeCodigo/MeuSite`: configurações, views e rotas (`settings.py`, `views.py`, `urls.py`)
- `ArquivosDeCodigo/MeuSite/templates`: telas do site (HTML)
- `ArquivosDeCodigo/MeuSite/static/css`: estilo das telas (CSS)
- `ArquivosDeCodigo/TelaDeLogin`: tela de listar usuários, que ainda vai passar para o Django
- `Documentos`: links das atividades de cada sprint
- `Imagens`: prints das telas usados neste README

## Como rodar o projeto

Pré-requisitos: ter o Python, o Git e um navegador instalados.

1. Clone o repositório: `git clone https://github.com/leticiavirgini-png/ENG-4021-Time-2.git`
2. Entre na pasta do projeto: `cd ENG-4021-Time-2/ArquivosDeCodigo`
3. Instale o Django: `pip install -r requirements.txt`
4. Rode o servidor: `python manage.py runserver`
5. Abra `http://127.0.0.1:8000/` no navegador.

Não é preciso nenhuma configuração específica.

## Exemplo de uso

Maria cria uma conta no MedMap e entra no site. Na página **Como usar**, ela vê o que precisa preencher. Depois, lê o artigo sobre mamografia na página **Artigos** e descobre que, pela idade dela, já deve fazer o exame. Se quiser trocar o e-mail, ela usa a tela de **Edição de usuário**.

## Documentação adicional

- [Documento do projeto (Google Docs)](https://docs.google.com/document/d/1XEaQMvfLpiWesibYZ-AwQ24oDW-SMko7l49yNKJLPTo/edit)
- [Modelagem de dados](https://docs.google.com/document/d/1XEaQMvfLpiWesibYZ-AwQ24oDW-SMko7l49yNKJLPTo/edit?tab=t.l9mjjwr8762q)
- Pasta `Documentos/`, com os links das atividades de cada sprint

## Melhorias futuras

- Passar a tela de listar usuários para o Django
- Ligar as telas ao banco de dados
- Criar o perfil de saúde e o histórico familiar
- Criar o Check-up Inteligente e o calendário de cuidados
- Enviar lembretes por e-mail
- Permitir vários perfis na mesma conta (por exemplo, pais e filhos)

## Licença

Projeto acadêmico, sem licença definida.
