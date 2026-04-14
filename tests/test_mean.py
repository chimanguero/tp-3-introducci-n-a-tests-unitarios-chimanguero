"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
def test_mean_un_elemento():
    """Lista con un solo elemento debe retornar ese elemento."""
    assert mean([10]) == 10.0

def test_mean_negativos():
    """Lista con números negativos."""
    assert mean([-2, -4]) == -3.0

def test_mean_decimales():
    """Lista con números decimales (float)."""
    assert mean([1.5, 2.5, 3.5]) == 2.5

def test_mean_lista_vacia():
    """Lista vacía → debe lanzar ValueError."""
    with pytest.raises(ValueError):
        mean([])