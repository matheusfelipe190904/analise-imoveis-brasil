# 🏠 Análise de Imóveis para Aluguel no Brasil

Análise exploratória de dados de imóveis para aluguel em 5 cidades brasileiras,
utilizando Python, Pandas, Matplotlib e Seaborn.

## 📊 Dataset
- **Fonte:** [Kaggle - Brazilian Houses to Rent](https://www.kaggle.com/datasets/antonyroy/finaltry)
- **10.692 imóveis** em São Paulo, Rio de Janeiro, Belo Horizonte, Porto Alegre e Campinas

## 🔍 Análises Realizadas
- Estatísticas descritivas gerais
- Aluguel médio por cidade
- Aluguel médio por número de quartos
- Correlação entre área e aluguel
- Proporção de imóveis que aceitam animais por cidade

## 💡 Principais Insights
- **São Paulo** tem o maior aluguel médio: R$ 4.652,79
- **Porto Alegre** tem o menor aluguel médio: R$ 2.337,70
- A mediana (R$ 2.661) é bem menor que a média (R$ 3.896), indicando outliers de imóveis de luxo
- Imóveis com 3 quartos são os mais comuns no dataset
- A maioria dos imóveis aceita animais em todas as cidades

## 🛠️ Tecnologias
- Python 3.10
- Pandas 2.2.2
- Matplotlib 3.10
- Seaborn 0.13.2

## ▶️ Como Executar
```bash
pip install pandas matplotlib seaborn
python analise_imoveis.py
```

## 📈 Gráficos Gerados
![Aluguel por Cidade](grafico_01_aluguel_por_cidade.png)
![Aluguel por Quartos](grafico_02_aluguel_por_quartos.png)
![Área vs Aluguel](grafico_03_area_vs_aluguel.png)
![Animais por Cidade](grafico_04_animais_por_cidade.png)