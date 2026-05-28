# 🛰️ Sistema de Monitoramento Espacial de Eventos Ambientais

Este repositório contém a solução desenvolvida para a **1ª Global Solutions de 2026** da disciplina de **Data Driven Application & Data Science**. 

O projeto consiste em uma aplicação em Python capaz de simular o processamento e a análise de dados espaciais provenientes de monitoramento por satélites, focando em eventos como desmatamento, queimadas e variações climáticas.

## 🚀 Funcionalidades

O sistema é executado via terminal e realiza as seguintes operações matemáticas e lógicas sem o uso de bibliotecas externas de análise (como o Pandas):

- **Entrada e Validação de Dados:** - Registro de múltiplos eventos ambientais.
  - Validação rigorosa de dados (ex: área afetada deve ser > 0, intensidade do impacto deve estar entre 1 e 10, número de ocorrências deve ser >= 1).
- **Armazenamento de Dados:**
  - Uso de estruturas de listas (`lists`) para separar e organizar tipos de eventos, localizações (país, região, cidade) e métricas.
- **Análise Estatística e Processamento:**
  - Cálculo do total de área afetada e média de intensidade.
  - Identificação da região com o maior número de ocorrências.
  - Cálculo da densidade média (ocorrências/área).
  - Identificação do **Evento Mais Crítico**, calculado com base na ponderação entre intensidade e área afetada.
- **Geração de Relatório:**
  - Exibição de um painel formatado no terminal resumindo todas as métricas analisadas.

## 📋 Pré-requisitos

Para executar este projeto, você precisará ter o **Python 3.x** instalado em sua máquina. Nenhuma biblioteca externa ou módulo adicional é necessário.

## 🛠️ Como usar (Instruções de Uso)

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/juliacrws/projeto-gs-data-science.git]
   (https://github.com/juliacrws/projeto-gs-data-science.git)
