import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)
    #abre o arquivo .json

faturamentos = [
    dia['valor'] for dia in dados['dias'] if dia['valor'] > 0
    ]  # Pula os dias sem faturamento

mais_faturamento = max(faturamentos)
menos_faturamento = min(faturamentos)

media_faturamento = sum(faturamentos) / len(faturamentos)
#calcula a media de faturamento

acima_da_media = 0
for faturamento in faturamentos:
    if faturamento > media_faturamento:
        acima_da_media =+ 1
#calcula os dias acima da media

print(f"Dia com menor faturamento: {menos_faturamento}")
print(f"Dia com maior faturamento: {mais_faturamento}")
print(f"Dias com faturamento acima da média: {acima_da_media}")
