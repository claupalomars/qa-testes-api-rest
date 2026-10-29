
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
