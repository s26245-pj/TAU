import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, patch
from bank import Bank, Account
from exceptions import InsufficientFundsError, AccountNotFoundError, DuplicateAccountError, InvalidTransactionError

@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def account1():
    return Account("123456", "Anna", 1000.0)

@pytest.fixture
def account2():
    return Account("654321", "Marek", 500.0)

def test_deposit(account1):
    account1.deposit(500)
    assert account1.balance == 1500

def test_withdraw_success(account1):
    account1.withdraw(200)
    assert account1.balance == 800

def test_withdraw_insufficient_funds(account1):
    with pytest.raises(InsufficientFundsError):
        account1.withdraw(2000)

@pytest.mark.asyncio
async def test_transfer_success(account1, account2):
    await account1.transfer(account2, 300)
    assert account1.balance == 700
    assert account2.balance == 800

@pytest.mark.asyncio
async def test_transfer_insufficient_funds(account1, account2):
    with pytest.raises(InsufficientFundsError):
        await account1.transfer(account2, 2000)

def test_create_account(bank):
    bank.create_account("111111", "Zofia", 300)
    account = bank.get_account("111111")
    assert account.owner == "Zofia"
    assert account.balance == 300

def test_create_duplicate_account(bank):
    bank.create_account("222222", "Zofia", 400)
    with pytest.raises(ValueError):
        bank.create_account("222222", "Zofia", 300)

def test_get_account(bank):
    bank.create_account("111111", "Zofia", 300)
    account = bank.get_account("111111")
    assert account.account_number == "111111"

def test_get_nonexistent_account(bank):
    with pytest.raises(ValueError):
        bank.get_account("999999")

@pytest.mark.asyncio
async def test_process_transaction(bank, account1, account2):
    bank.accounts["123456"] = account1
    bank.accounts["654321"] = account2

    async def transaction():
        await account1.transfer(account2, 400)

    await bank.process_transaction(transaction)
    assert account1.balance == 600
    assert account2.balance == 900

@pytest.mark.asyncio
@patch("bank.Account.transfer", new_callable=AsyncMock)
async def test_transfer_with_mock(mock_transfer, account1, account2):
    await account1.transfer(account2, 100)
    mock_transfer.assert_called_once_with(account2, 100)
