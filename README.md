# W.I.P - API - Football Club

É uma api que consiste em fornecer uma solução back-end para quem queira gerir sua equipe ou time de futebol.

### Features atuais:
- Auth (JWT)
- Cargos (Administrador, Usuário)
- Usuários
- Jogador
- Torneios
- Partidas
- Gols
- Cartões Vermelhos
- Cartões Amarelos
- Escalação

## Proposta do DB

![Proposta de tabelas](/football-club-db.png)

## Run
```
uvicorn app:app --host 0.0.0.0 --port 80 
```

## Alembic

- Criar uma revision -> ``alembic revision -m "criar" ``
- Efetivar comando de criar -> `` alembic upgrade head ``
- Rollback -> ``alembic downgrade -1``

