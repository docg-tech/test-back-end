## Teste de Backend

Fala, dev! Tudo bem?

Queremos alguém que saiba trabalhar em equipe e que possa colaborar e ajudar seus colegas ao longo das tarefas, e além disso esteja disposto a aprender.

Este teste tem como objetivo avaliar e desafiar você. Não é obrigatório realizá-lo completamente (nem dominar todos os frameworks), queremos apenas reconhecer seu esforço e potencial para aprender, se adaptar e tomar decisões.

## O desafio

Sua missão é criar uma API que seja capaz de administrar os clientes e seus pets que solicitam serviços, para que possamos consumir estes dados de maneira prática, rápida e automatizada.

A regra de negócio desta API é:
Clientes dentro da API podem possuir um ou mais pets, e podem querer executar um serviço para esse pet em uma data específica.

Precisamos no fim apenas saber quais serviços serão executados em um dia específico, para qual cliente e qual pet.

Esta API deverá seguir as práticas RESTful e conter listagens, busca, paginação e filtros. Fique à vontade para decidir quais filtros são mais interessantes.

## O que precisa conter

### Cliente (CRUD)
```
Nome
E-mail
Telefone
Pets
```

### Pet (CRUD)
```
Nome
Espécie
Raça
```

### Serviço (CRUD)
```
Titulo
Preço
```

CRUD = Create, Read, Update e Delete.

Talvez sejam necessárias algumas relações intermediárias para guardar informações extras...

## Consigo fazer?

Consegue sim! Só precisa saber (ou aprender agora) um pouco sobre as seguintes tecnologias:

- Conceitos de API RESTful
- Modelagem de dados
- Ruby on Rails
- Algum banco de dados, por exemplo, Postgres, MySQL, SQL Server, MongoDB, etc...
- Git

## Requisitos

Modelagem de dados;
- O retorno deverá ser em formato JSON;
- Requisições GET, POST, PUT ou DELETE, conforme a melhor prática;
- A persistência dos dados pode ser realizada da maneira que preferir;
- Criar README do projeto descrevendo as tecnologias utilizadas, chamadas dos serviços e configurações necessário para executar a aplicação.

## Ganha mais pontos

- Desenvolver utilizando TDD;
- Criar API de relatório;
- Criar uma solução de autenticação.
- Encapsular a solução com docker

## Como eu entrego?

Primeiramente, você pode fazer um fork desse repositório aqui, para sua conta do Github, depois disso crie uma branch nova com o seu nome (ex: nome_sobrenome), para podermos identificá-lo.

Após terminar o desafio, você pode solicitar um pull request para a branch 'main' do nosso repositório. Vamos receber e fazer a avaliação de todos.

## Só isso?

Só!

É isso e boa sorte!
