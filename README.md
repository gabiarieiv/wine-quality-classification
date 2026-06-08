# 🍷 Wine Quality Classification with Machine Learning
> Projeto desenvolvido utilizando técnicas de Machine Learning Applied to Business com foco em classificação preditiva e geração de insights estratégicos.

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte do Tech Challenge da pós-graduação em Data Analytics da FIAP.

O objetivo é construir modelos de Machine Learning capazes de prever a qualidade de vinhos com base em características físico-químicas presentes no dataset Wine Quality.

O projeto contempla todas as etapas de um fluxo profissional de Machine Learning:

- análise exploratória de dados (EDA)
- tratamento e preparação dos dados
- transformação da variável alvo
- treinamento de modelos
- avaliação de performance
- otimização de hiperparâmetros
- interpretação dos resultados
- geração de insights de negócio

---

# 🎯 Objetivo de Negócio

A classificação automática da qualidade de vinhos pode auxiliar produtores e indústrias vinícolas na identificação de fatores que impactam a percepção de qualidade dos produtos.

A utilização de Machine Learning permite transformar dados físico-químicos em inteligência estratégica, apoiando:

- melhoria da qualidade final dos vinhos
- otimização de processos produtivos
- redução de inconsistências
- tomada de decisão baseada em dados

---

# 📊 Dataset

Foi utilizado o dataset público:

## Wine Quality Dataset

Disponível em:

:contentReference[oaicite:0]{index=0}

O dataset contém atributos físico-químicos relacionados a vinhos tintos portugueses, incluindo:

- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- sulphates
- alcohol
- pH
- quality

---

# 🧠 Problema de Machine Learning

O problema foi tratado como uma classificação binária:

- Alta qualidade → nota ≥ 7
- Baixa/Média qualidade → nota < 7

Variável alvo:

```python
quality_binary

