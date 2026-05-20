import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("data/houses_to_rent.csv")

print(df.shape) # retorna uma tupla (linhas, colunas) para verificar tamanho do dataset
print(df.dtypes) # mostra o tipo de cada coluna
print(df.head()) # mostra as 5 primeiras linhas

# Renomear colunas
df.columns = [
    "cidade", "area", "quartos", "banheiros",
    "vagas", "andar", "aceita_animal", "mobiliado",
    "condominio", "aluguel", "iptu", "seguro_incendio", "total"
]

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Verificar cidades disponíveis
print("\nCidades no dataset:")
print(df["cidade"].value_counts())

# Estatísticas descritivas das colunas principais
print("\nEstatísticas descritivas:")
print(df[["area", "quartos", "aluguel", "total"]].describe().round(2))

# Aluguel médio por cidade
print("\nAluguel médio por cidade:")
aluguel_por_cidade = df.groupby("cidade")["aluguel"].mean().round(2).sort_values(ascending=False)
print(aluguel_por_cidade)

# Quantidade de imóveis por cidade
print("\nQuantidade de imóveis por cidade:")
print(df["cidade"].value_counts())

# Top 10 imóveis mais caros
print("\n" + "=" * 50)
print("TOP 10 IMÓVEIS MAIS CAROS")
print("=" * 50)
top10 = df[["cidade", "area", "quartos", "aluguel"]].sort_values("aluguel", ascending=False).head(10)
top10.index = range(1, 11)
print(top10)

# Percentual de imóveis mobiliados por cidade
print("\n" + "=" * 50)
print("PERCENTUAL DE IMÓVEIS MOBILIADOS POR CIDADE")
print("=" * 50)
mobiliado = df.groupby("cidade")["mobiliado"].value_counts(normalize=True).mul(100).round(1).unstack()
print(mobiliado)

# Gráfico de barras: aluguel médio por cidade
plt.figure(figsize=(10, 5))
aluguel_por_cidade.plot(kind="bar", color="steelblue", edgecolor="white")

plt.title("Aluguel Médio por Cidade", fontsize=14, fontweight="bold")
plt.xlabel("Cidade")
plt.ylabel("Aluguel Médio (R$)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafico_01_aluguel_por_cidade.png")
plt.show()

print("Gráfico salvo!")

# Aluguel médio por número de quartos
print("\nAluguel médio por número de quartos:")
aluguel_por_quartos = df.groupby("quartos")["aluguel"].mean().round(2)
print(aluguel_por_quartos)

# Gráfico
plt.figure(figsize=(10, 5))
aluguel_por_quartos.plot(kind="bar", color="teal", edgecolor="white")

plt.title("Aluguel Médio por Número de Quartos", fontsize=14, fontweight="bold")
plt.xlabel("Número de Quartos")
plt.ylabel("Aluguel Médio (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_02_aluguel_por_quartos.png")
plt.show()

print("Gráfico salvo!")

# Filtrar outliers extremos para o gráfico não ficar distorcido
df_filtrado = df[(df["area"] <= 500) & (df["aluguel"] <= 15000)]

print(f"\nImóveis após filtrar outliers: {df_filtrado.shape[0]}")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_filtrado,
    x="area",
    y="aluguel",
    hue="cidade",
    alpha=0.4,
    palette="Set1"
)

plt.title("Correlação entre Área e Aluguel", fontsize=14, fontweight="bold")
plt.xlabel("Área (m²)")
plt.ylabel("Aluguel (R$)")
plt.tight_layout()
plt.savefig("grafico_03_area_vs_aluguel.png")
plt.show()

print("Gráfico salvo!")

# Gráfico 4: Proporção de imóveis que aceitam animais por cidade
print("\nProporção de imóveis que aceitam animais:")
animais = df.groupby(["cidade", "aceita_animal"]).size().unstack(fill_value=0)
print(animais)

animais.plot(kind="bar", figsize=(10, 5), colormap="Set2", edgecolor="white")
plt.title("Imóveis que Aceitam Animais por Cidade", fontsize=14, fontweight="bold")
plt.xlabel("Cidade")
plt.ylabel("Quantidade")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafico_04_animais_por_cidade.png")
plt.show()

# Insights finais
print("\n" + "=" * 50)
print("INSIGHTS PRINCIPAIS")
print("=" * 50)
print(f"Total de imóveis analisados : {df.shape[0]}")
print(f"Cidade mais cara            : {aluguel_por_cidade.idxmax()} (R$ {aluguel_por_cidade.max():,.2f})")
print(f"Cidade mais barata          : {aluguel_por_cidade.idxmin()} (R$ {aluguel_por_cidade.min():,.2f})")
print(f"Aluguel médio geral         : R$ {df['aluguel'].mean():,.2f}")
print(f"Aluguel mediano geral       : R$ {df['aluguel'].median():,.2f}")
print(f"Número de quartos mais comum: {df['quartos'].mode()[0]}")
print("\nAnálise concluída!")