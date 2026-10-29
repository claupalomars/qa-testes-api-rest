
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
