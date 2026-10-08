# Monitor-de-Clima-
Desenvolvimento de Monitor de Clima por cidade escolhida

# 🌤️ Monitor de Clima

Projeto desenvolvido em **Python** para consultar e acompanhar informações meteorológicas de uma cidade através de uma API.

O projeto está sendo desenvolvido de forma gradual, começando com uma aplicação simples executada pelo terminal e evoluindo posteriormente para um sistema automatizado com interface gráfica e notificações no Windows.

## 🚀 Objetivo

Criar um pequeno assistente meteorológico capaz de consultar informações do clima e apresentar os dados de forma simples e organizada.

Além de ser uma ferramenta prática, o projeto tem como objetivo colocar em prática conceitos de:

- Python
- APIs
- Requisições HTTP
- JSON
- Tratamento de dados
- Automação
- Interface gráfica
- Notificações no Windows

## 🌎 Funcionalidades atuais

Atualmente o programa consegue:

- 🔎 Consultar uma cidade
- 📍 Identificar latitude e longitude
- 🌡️ Consultar temperatura atual
- 🌡️ Mostrar sensação térmica
- 💧 Mostrar umidade do ar
- 💨 Mostrar velocidade do vento
- ⌨️ Permitir informar a cidade pelo terminal

## 🛠️ Tecnologias utilizadas

- **Python 3.14.4**
- **Requests**
- **Open-Meteo API**
- **VS Code**
- **Git / GitHub**

## 📂 Estrutura do projeto

```text
monitor-clima/
│
├── .venv/
├── clima.py
├── requirements.txt
└── README.md
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd monitor-clima
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Git Bash:

```bash
source .venv/Scripts/activate
```

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o programa

```bash
python clima.py
```

Depois informe a cidade quando solicitado.

Exemplo:

```text
Digite o nome da cidade: Mogi das Cruzes
```

## 📊 Exemplo

```text
==========================
    MONITOR DE CLIMA
==========================
Cidade: Mogi das Cruzes
Temperatura: 23.5 °C
Sensação térmica: 24.1 °C
Umidade: 78 %
Vento: 10.2 km/h
==========================
```

## 🔮 Próximas etapas

O projeto ainda está em desenvolvimento. As próximas funcionalidades planejadas são:

- 🌧️ Informar possibilidade de chuva
- ☀️ Identificar condição do tempo
- 🕐 Mostrar horário da consulta
- 🔄 Atualização automática
- 📅 Previsão para as próximas horas
- 📆 Previsão para os próximos dias
- 🔔 Notificações do Windows
- ⚠️ Alertas de chuva e tempestade
- 🌡️ Alertas de temperaturas extremas
- 💾 Histórico das consultas
- 🗄️ Banco de dados SQLite
- 🖥️ Interface gráfica
- ⚙️ Execução em segundo plano
- 🚀 Inicialização automática com o Windows
- 📦 Criação de executável `.exe`

## 📚 Objetivo de aprendizado

Este projeto está sendo desenvolvido como um projeto prático de estudos em Python.

A ideia é evoluir o sistema aos poucos, aplicando conceitos aprendidos durante o desenvolvimento e documentando cada etapa.

## 📡 API

Os dados meteorológicos são obtidos através da **Open-Meteo API**.

## 👨‍💻 Autor

**Jhonathan Ribeiro**

Projeto desenvolvido para estudos de **Python, APIs, automação e desenvolvimento de aplicações**.

---

⭐ Se você gostou do projeto, acompanhe a evolução!
