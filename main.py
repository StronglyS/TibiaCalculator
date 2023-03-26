def gerar_lista_de_xp(nivel_maximo):
    xp_por_nivel = []
    for nivel in range(1, nivel_maximo + 1):
        xp = int(50/3 * (nivel**3 - 6*nivel**2 + 17*nivel - 12))
        xp_por_nivel.append(xp)
    return xp_por_nivel

nivel_maximo = 5000

level_atual = int(input("Digite o seu nível atual: "))
level_desejado = int(input("Digite o nível desejado: "))
dias_por_semana = int(input("Digite a quantidade de dias na semana que jogará: "))
horas_por_dia = float(input("Digite a quantidade de horas por dia que jogará: "))
raw_xp_por_hora = float(input("Digite a sua RAW XP por hora: "))
horas_boost = float(input("Digite a quantidade de horas com boost: "))
horas_verde = float(input("Digite a quantidade de horas com stamina verde: "))

# Gerando a lista de experiência por nível
lista_experiencia = gerar_lista_de_xp(nivel_maximo)

def calcular_tempo_para_level(raw_xp_por_hora, horas_por_dia, horas_boost, horas_verde, dias_por_semana, level_atual, level_desejado, lista_experiencia):
    xp_por_hora = raw_xp_por_hora * (1 + 0.5 * min(horas_boost, 3))
    if horas_verde > 3:
        xp_por_hora *= 1
    else:
        xp_por_hora *= 1.5
    xp_necessaria = lista_experiencia[level_desejado - 1] - lista_experiencia[level_atual - 1]
    horas_necessarias = xp_necessaria / xp_por_hora
    dias_necessarios = horas_necessarias / (horas_por_dia * dias_por_semana / 7)
    return dias_necessarios

# Chamando a função para calcular o tempo necessário para alcançar o level desejado
dias_necessarios = calcular_tempo_para_level(raw_xp_por_hora, horas_por_dia, horas_boost, horas_verde, dias_por_semana, level_atual, level_desejado, lista_experiencia)

# Exibindo o resultado
print(f'Para alcançar o level {level_desejado}, serão necessários {dias_necessarios:.2f} dias')
