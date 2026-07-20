def analyze_heart_effort(activities):
    # Analisa esforço cardíaco e gera URLs de localização para cada atividade.
    # Calcula o Índice de Variabilidade de Esforço (max_hr - avg_hr).
    # Classifica como 'Esforço Variável' ou 'Esforço Estável'.
    # Retorna lista de dicionários com nome, médias, máximos, variabilidade e URL do Google Maps.
    """
    Analisa esforço cardíaco e gera URLs de localização para cada atividade.
    Calcula o Índice de Variabilidade de Esforço (max_hr - avg_hr).
    Classifica como 'Esforço Variável' ou 'Esforço Estável'.
    Retorna lista de dicionários com nome, médias, máximos, variabilidade e URL do Google Maps.
    """
    results = []
    for act in activities:
        name = getattr(act, 'name', 'Desconhecido')
        avg_hr = getattr(act, 'average_heartrate', None)
        max_hr = getattr(act, 'max_heartrate', None)
        start_latlng = getattr(act, 'start_latlng', None)
        url = None
        variabilidade = '-'
        classificacao = '-'
        if avg_hr is not None and max_hr is not None:
            variabilidade = max_hr - avg_hr
            classificacao = 'Esforço Variável' if variabilidade > 15 else 'Esforço Estável'
        if start_latlng and isinstance(start_latlng, (list, tuple)) and len(start_latlng) == 2:
            lat, lng = start_latlng
            if lat is not None and lng is not None:
                url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
        results.append({
            'name': name if name else '-',
            'average_heartrate': avg_hr if avg_hr is not None else '-',
            'max_heartrate': max_hr if max_hr is not None else '-',
            'variabilidade': variabilidade,
            'classificacao': classificacao,
            'start_latlng': start_latlng if start_latlng else '-',
            'maps_url': url
        })
    return results
