import unittest
import pytest

import global_config, config_basic, vlan_acceso, vlans

def test_enter_global_config(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "s")
    returned_comands = global_config.enter_global_config_mode()
    expected_comands = "\nenable \nconfigure terminal \n"

    assert returned_comands == expected_comands

def test_config_basic(monkeypatch):

    answers = iter(["Marco", "cisco", "s", "No entrar", "s", "cisco", "s", "cisco"])
    comandos = ""
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    returned_comands = config_basic.config_b(comandos)
    expected_comands = "\nhostname Marco\nenable secret cisco\nservice password-encryption\nbanner motd #No entrar#\nline con 0\npassword cisco\nlogin\nline vty 0 15\npassword cisco\nlogin\ndo copy run start \n"

    assert returned_comands == expected_comands

def test_vlan_acceso(monkeypatch):

    answers = iter(["192.168.0.10", "", "255.255.255.0"])
    comandos = ""
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    returned_comands = vlan_acceso.int_acceso(comandos)
    expected_comands = "\ninterface vlan 1\nip address 192.168.0.10 255.255.255.0\nno shutdown \nexit \ndo copy run start \n"

    assert returned_comands == expected_comands

def test_vlans(monkeypatch):

    answers = iter(["", "r", "2", "x", "prueba", "s", "", "r", "2", "3", "4", "5", "6", "X", "", "r", "T", "", "2,5", "t", "r", "1", "", "A", "", "a", "6"])
    comandos = ""
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    returned_comands = vlans.vlan(comandos)
    expected_comands = "\nvlan 2\nname prueba\nexit\ninterface f0/2\ninterface f0/3\nswitchport mode trunk\nswitchport trunk allowed vlan 2,5\ninterface f0/4\nswitchport mode trunk\nswitchport trunk native vlan 1\ninterface f0/5\nswitchport mode access\ninterface f0/6\nswitchport mode access\nswitchport access vlan 6\nexit\ndo copy run start \n"

    assert returned_comands == expected_comands