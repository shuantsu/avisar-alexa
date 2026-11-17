---
name: avisar-alexa
description: Envia um anúncio de voz para um dispositivo Alexa via Voice Monkey (API v3). Use quando o usuário pedir para avisar/notificar a Alexa, anunciar uma mensagem, ou dizer algo em um Echo/dispositivo configurado. Aciona com pedidos como "avise a Alexa", "mande um aviso na Alexa", "anuncie na Alexa que...".
---

# Avisar Alexa (Voice Monkey)

Envia uma mensagem falada para um dispositivo Alexa usando o endpoint `https://api-v3.voicemonkey.io/announce`.

## Script

```bash
python <skill_dir>/scripts/avisar_alexa.py "Sua mensagem aqui"
```

No Windows, se necessário:

```bash
py <skill_dir>/scripts/avisar_alexa.py "Sua mensagem aqui"
```

## Opções

- `speech` (posicional): texto a anunciar. Padrão: `"A tarefa foi concluída com sucesso."`
- `--device`: dispositivo Voice Monkey (padrão: `room-echo-4zcbn`)
- `--language`: idioma da fala (padrão: `pt-BR`)
- `--token`: token da API Voice Monkey (padrão embutido no script)

## Exemplos

```bash
# Aviso simples
python <skill_dir>/scripts/avisar_alexa.py "O deploy terminou com sucesso."

# Dispositivo/idioma específicos
python <skill_dir>/scripts/avisar_alexa.py "Hora do café" --device room-echo-4zcbn --language pt-BR
```

## Saída e erros

- Sucesso: imprime a resposta da API (JSON/texto) e retorna código 0.
- Falha: imprime `{"success": false, "error": "..."}` e retorna código 1.

## Notas

- Requer Python 3 e acesso à internet para alcançar `api-v3.voicemonkey.io`.
- O token/dispositivo padrão são os configurados no script; substitua via `--token`/`--device` se precisar usar outra conta ou outro dispositivo.
- Não exponha tokens em logs ou commits desnecessariamente ao reutilizar este script em outros contextos.
