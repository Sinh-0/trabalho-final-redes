---

## 1. Visão Geral do Projeto

Este projeto consiste em um sistema de "Quadro Branco" baseado em terminal, inspirado na simplicidade do *Dontpad*. Ele permite que múltiplos usuários, conectados via internet ou rede local, colaborem em um ambiente de texto compartilhado de forma síncrona.

O sistema foi desenvolvido em Python, utilizando a biblioteca nativa `socket` para comunicação de baixo nível e `threading` para gerenciar a concorrência de múltiplos clientes.

## 2. Arquitetura Técnica e Decisões de Engenharia

### 2.1 Protocolo de Transporte: TCP (Transmission Control Protocol)

Optei pelo protocolo **TCP** para garantir:

- **Confiabilidade:** Cada caractere enviado é confirmado pelo receptor.
- **Ordenação:** As mensagens e edições são entregues na sequência exata em que foram enviadas, evitando inconsistências no texto compartilhado.

### 2.2 Concorrência: Modelo Multithreading

Para suportar a escalabilidade e permitir que novos usuários entrem no quadro sem interromper uns aos outros, o servidor implementa **Threads**:

- Cada conexão aceita pelo método `accept()` gera uma thread de execução independente.
- Isso garante que operações de entrada/saída (I/O) de um usuário não bloqueiem o processamento dos demais.

### 2.3 Infraestrutura de Rede: NAT Traversal com Ngrok

Para superar as limitações de IPs privados e firewalls em ambientes domésticos ou universitários, o projeto utiliza o **Ngrok**. Esta ferramenta cria um túnel TCP que expõe a porta local `12345` do servidor a um endpoint público global, validando o funcionamento da aplicação em ambiente **WAN**.

## 3. Funcionalidades Implementadas

- **Identificação de Usuário:** Sistema de handshake inicial onde o usuário define seu nome ao entrar.
- **Presença em Tempo Real:** Notificações automáticas do sistema quando um colaborador entra ou sai da sessão.
- **Broadcast de Mensagens:** Replicação eficiente de dados para todos os nós conectados.
- **Tratamento de Exceções:** Limpeza automática de threads e sockets em caso de desconexão abrupta.

## 4. Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.

### Passo 1: Iniciar o Servidor

```
python servidor.py
```

### Passo 2: Iniciar o Cliente

```
python cliente.py
```

### Passo 3: Encerrar

```
Ctrl + C
```