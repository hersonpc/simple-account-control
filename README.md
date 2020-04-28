# simple-account-control

Curso: **CIÊNCIA DE DADOS E BIG DATA ANALYTICS**.  
Disciplina: **PRATICA E LABORATORIO II**.  


## Introdução

Sistema de controle bancário, para permitir que o usuário crie uma classe Cliente (NOME, TELEFONE) e uma classe Conta (com número e saldo), logicamente vinculada ao cliente, que permita simular duas operações (saque e extratos, simples). Deve ser admitida a manipulação de uma conta especial agregando a esta o atributo limite. Ao final simular a listagem de extrato bancário.

## Como executar o sistema

### Pre requisitos:

Os códigos de exempo, são para sistemas operacionais Linux baseados em Debian:

1. Ter instalados o git e o python no ambiente
```bash
sudo apt install git python -y
```

2. Baixar o código fonte deste projeto e executa-lo
```bash
git clone https://github.com/hersonpc/simple-account-control && cd simple-account-control/src
python main.py
```

## Interface

### Menu principal

![](/docs/001-menu.jpg)  

### Cadastro de clientes e contas

![](/docs/002-cadastro.jpg)  

### Relatório de contas cadastradas

![](/docs/003-listagem.jpg)  

### Acesso ao menu interno da conta

![](/docs/004-menu-conta.jpg)  

### Extrato da conta

![](/docs/005-extrato.jpg)  

### Registrar movimentações (Depositos ou Saques)

![](/docs/006-registro-movimentacao.jpg)  

### Alteração de limites (Para contas especiais)

![](/docs/007-alteracao-limite.jpg)  

### Extrato final exibindo todos os históricos

![](/docs/008-extrato-final.jpg)  