# Integrantes:
# - Giovanni Pascon Corrêa - RM571546
# - Julia de Moraes Barbosa - RM572997
# - Stefany Feitosa da Silva - RM568651

# Listas para armazenar os dados de cada evento
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# -------------------------------------------------------
# Entrada de Dados

# Solicita a quantidade de eventos
quantidade = 0
while quantidade < 1:
    quantidade = int(input("Insira a quantidade de eventos: "))
    if quantidade < 1:
        print("A quantidade deve ser pelo menos 1. Tente novamente.")

# Coleta os dados de cada evento
for i in range(1, quantidade + 1):
    print(f"\n--- Evento {i} ---")

    tipo = input("Tipo (ex: desmatamento, queimadas): ")
    pais = input("País: ")
    regiao = input("Região: ")
    cidade = input("Cidade: ")

    # Validação: área deve ser maior que zero
    area = 0.0
    while area <= 0:
        area = float(input("Área afetada (km²): "))
        if area <= 0:
            print("A área deve ser maior que zero. Tente novamente.")

    # Validação: intensidade entre 1 e 10
    intensidade = 0
    while intensidade < 1 or intensidade > 10:
        intensidade = int(input("Intensidade (1 a 10): "))
        if intensidade < 1 or intensidade > 10:
            print("A intensidade deve estar entre 1 e 10. Tente novamente.")

    # Validação: ocorrências >= 1
    num_ocorrencias = 0
    while num_ocorrencias < 1:
        num_ocorrencias = int(input("Número de ocorrências: "))
        if num_ocorrencias < 1:
            print("O número de ocorrências deve ser pelo menos 1. Tente novamente.")

    # Armazena nas listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# -------------------------------------------------------
# Análise de Dados

# Total de eventos registrados
total_eventos = len(tipos_eventos)

# Soma total das áreas afetadas
soma_areas = 0.0
for a in areas_afetadas:
    soma_areas += a

# Média das intensidades
soma_intensidades = 0
for intens in intensidades:
    soma_intensidades += intens
media_intensidades = soma_intensidades / total_eventos

# Evento com maior área afetada
maior_area = max(areas_afetadas)
idx_maior_area = areas_afetadas.index(maior_area)

# Região com maior número de ocorrências
regioes_unicas = []
total_por_regiao = []

for i in range(total_eventos):
    reg = regioes[i]
    if reg in regioes_unicas:
        idx = regioes_unicas.index(reg)
        total_por_regiao[idx] += ocorrencias[i]
    else:
        regioes_unicas.append(reg)
        total_por_regiao.append(ocorrencias[i])

max_ocorrencias_regiao = max(total_por_regiao)
idx_regiao_max = total_por_regiao.index(max_ocorrencias_regiao)
regiao_mais_ocorrencias = regioes_unicas[idx_regiao_max]

# Densidade média
soma_densidades = 0.0
for i in range(total_eventos):
    soma_densidades += ocorrencias[i] / areas_afetadas[i]
densidade_media = soma_densidades / total_eventos

# Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidades:
        eventos_acima_media += 1

# Evento mais crítico
criticidade = []
for i in range(total_eventos):
    criticidade.append(intensidades[i] * areas_afetadas[i])

max_criticidade = max(criticidade)
idx_mais_critico = criticidade.index(max_criticidade)

# -------------------------------------------------------
# Relatório de Resultados

print("\n" + "=" * 40)
print("        RELATÓRIO DE ANÁLISE")
print("=" * 40)

print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n" + "-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {soma_areas:.0f} km²")
print(f"Média de intensidade: {media_intensidades:.1f}")

print("\n" + "-" * 40)
print("Análises")
print("-" * 40)
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n" + "-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
print(f"Tipo: {tipos_eventos[idx_mais_critico]}")
print(f"Local: {cidades[idx_mais_critico]}, {regioes[idx_mais_critico]}, {paises[idx_mais_critico]}")
print(f"Intensidade: {intensidades[idx_mais_critico]}")
print(f"Área afetada: {areas_afetadas[idx_mais_critico]:.0f} km²")

print("\n" + "=" * 40)
print(f"Total de desastres registrados: {total_eventos}")