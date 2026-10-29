
import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_consultar_reservas():
    resposta = requests.get(f"{BASE_URL}/booking", timeout=30)

    assert resposta.status_code == 200

    reservas = resposta.json()

    assert isinstance(reservas, list)
    assert len(reservas) > 0


def test_reservas_possuem_identificador():
    resposta = requests.get(f"{BASE_URL}/booking", timeout=30)

    assert resposta.status_code == 200

    reservas = resposta.json()

    assert isinstance(reservas, list)

    for reserva in reservas:
        assert "bookingid" in reserva
        assert isinstance(reserva["bookingid"], int)

def test_consultar_reserva_inexistente():
    url = f"{BASE_URL}/booking/999999999"

    resposta = requests.get(url, timeout=30)

    assert resposta.status_code == 404

def test_criar_reserva():
    url = f"{BASE_URL}/booking"

    dados = {
        "firstname": "Maria",
        "lastname": "Silva",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Breakfast"
    }

    resposta = requests.post(url, json=dados, timeout=30)

    assert resposta.status_code == 200

    reserva_criada = resposta.json()

    assert "bookingid" in reserva_criada
    assert reserva_criada["booking"]["firstname"] == "Maria"
    assert reserva_criada["booking"]["lastname"] == "Silva"

def test_atualizar_reserva():
    url = f"{BASE_URL}/booking"

    resposta_token = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        timeout=30
    )

    assert resposta_token.status_code == 200

    token = resposta_token.json()["token"]
    headers = {"Cookie": f"token={token}"}

    dados = {
        "firstname": "Maria",
        "lastname": "Silva",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Breakfast"
    }

    resposta_criacao = requests.post(
        url,
        json=dados,
        timeout=30
    )

    assert resposta_criacao.status_code == 200

    booking_id = resposta_criacao.json()["bookingid"]

    dados_atualizados = {
        "firstname": "Joao",
        "lastname": "Souza",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-11-10",
            "checkout": "2026-11-15"
        },
        "additionalneeds": "Lunch"
    }

    resposta_atualizacao = requests.put(
        f"{url}/{booking_id}",
        json=dados_atualizados,
        headers=headers,
        timeout=30
    )

    assert resposta_atualizacao.status_code == 200

    reserva_atualizada = resposta_atualizacao.json()

    assert reserva_atualizada["firstname"] == "Joao"
    assert reserva_atualizada["lastname"] == "Souza"
    assert reserva_atualizada["totalprice"] == 300

def test_excluir_reserva():
    url = f"{BASE_URL}/booking"

    resposta_token = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        timeout=30
    )

    assert resposta_token.status_code == 200
    token = resposta_token.json()["token"]
    headers = {"Cookie": f"token={token}"}

    dados = {
        "firstname": "Maria",
        "lastname": "Silva",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Breakfast"
    }

    resposta_criacao = requests.post(
        url,
        json=dados,
        timeout=30
    )

    assert resposta_criacao.status_code == 200
    booking_id = resposta_criacao.json()["bookingid"]

    resposta_exclusao = requests.delete(
        f"{url}/{booking_id}",
        headers=headers,
        timeout=30
    )

    assert resposta_exclusao.status_code == 201

    resposta_consulta = requests.get(
        f"{url}/{booking_id}",
        timeout=30
    )

    assert resposta_consulta.status_code == 404
