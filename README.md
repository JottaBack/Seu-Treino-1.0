# Seu Treino

Aplicação de exemplo em Flask com cadastro, login e uma página protegida.

## Executar

Instale as dependências e inicie o servidor:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000 no navegador. Crie uma conta pela própria página.

As contas são mantidas apenas na memória e são apagadas quando o servidor é
reiniciado. Este projeto é um exemplo de aprendizado, não use com senhas reais
nem como sistema de autenticação de produção.

## Salvamento automático no GitHub

O script `sync_to_github.ps1` cria um commit e envia ao GitHub as alterações
feitas neste repositório. Ele deve ser executado pela tarefa agendada do Windows
a cada 10 minutos. Não coloque senhas, tokens ou outros dados privados nesta
pasta: os commits são publicados no repositório público.
