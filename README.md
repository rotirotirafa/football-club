# W.I.P - API - Football Club

É uma api que consiste em fornecer uma solução back-end para quem queira gerir sua equipe ou time de futebol.

### Features atuais:
- Auth (JWT)
- [x] Cargos (Administrador, Usuário)
- [x] Usuários
- [x] Jogadores
- Torneios
- Partidas
- Gols
- Cartões Vermelhos
- Cartões Amarelos
- Escalação

## Proposta do DB
desatualizado!
![Proposta de tabelas](/football-club-db.png)

## Run
```
uvicorn main:app --host 0.0.0.0 --port 80 
```

## Alembic

- Criar uma revision -> ``alembic revision -m "criar" ``
- Efetivar comando de criar -> `` alembic upgrade head ``
- Rollback -> ``alembic downgrade -1``

