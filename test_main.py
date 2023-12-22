import pytest
from main import create_menu

def test_user_choice_exit(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    
    # Run the function that takes user input
    create_menu()
    
    captured = capsys.readouterr()
    
    assert "Thank you for using OnePWD Manager! See you soon!" in captured.out
    assert "Enter 5 to exit" in captured.out
    assert "Enter 1 if you are a new user" in captured.out
    assert "Enter 2 to login" in captured.out
    assert "Enter 3 for FAQs" in captured.out
