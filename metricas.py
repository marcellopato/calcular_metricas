def calcular_metricas(vp, vn, fp, fn):
    """
    Calcula as métricas de avaliação de um modelo de classificação.

    Parâmetros:
        vp (int): Verdadeiros Positivos
        vn (int): Verdadeiros Negativos
        fp (int): Falsos Positivos
        fn (int): Falsos Negativos

    Retorna:
        dict: Métricas calculadas (acurácia, sensibilidade, especificidade, precisão, F-score)
    """
    try:
        # Cálculos
        acuracia = (vp + vn) / (vp + vn + fp + fn)
        sensibilidade = vp / (vp + fn)
        especificidade = vn / (vn + fp)
        precisao = vp / (vp + fp)
        f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

        return {
            "Acurácia": acuracia,
            "Sensibilidade (Recall)": sensibilidade,
            "Especificidade": especificidade,
            "Precisão": precisao,
            "F-score": f_score
        }
    except ZeroDivisionError:
        return {"Erro": "Divisão por zero nas métricas. Verifique os valores fornecidos."}


# Exemplo de matriz de confusão arbitrária
vp = 50
vn = 40
fp = 10
fn = 5

# Calculando métricas
metricas = calcular_metricas(vp, vn, fp, fn)

# Exibindo resultados
for nome, valor in metricas.items():
    print(f"{nome}: {valor:.2f}")
