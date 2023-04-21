
@usefixtures('prepare-database')
async def test_get_roles():
    # arrange
    expected = [
      { "role_id": 1, "name": "admin" },
      { "role_id": 2, "name": "user" },
    ]

    # act
    async with AsyncClient(app=app, base_url=base_url) as client:
        output = await client.get(f'v1/roles')

    # assert
    data = output.json()

    assert output.status_code == HTTPSTATUS.OK
    assert data == { expected }