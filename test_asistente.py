import unittest
import pytest

import asistente

def test_enter_global_config(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "s")
    returned_comands = asistente.enter_global_config_mode()
    expected_comands = "\nenable \nconfigure terminal \n"

    assert returned_comands == expected_comands