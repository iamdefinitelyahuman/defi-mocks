from pathlib import Path

import pytest

from brownie.project import compile_source

base_path = Path(__file__).parent

with base_path.joinpath("ERC20-no-return.sol").open() as fp:
    ERC20_NO_RETURN = fp.read()

with base_path.joinpath("ERC20.sol").open() as fp:
    ERC20 = fp.read()


@pytest.fixture(scope="session")
def DAI(accounts):
    token = compile_source(ERC20).Token
    yield token.deploy("DAI", "DAI Stablecoin", 18, {"from": accounts[0]})


@pytest.fixture(scope="module")
def USDT(accounts):
    token = compile_source(ERC20_NO_RETURN).Token
    yield token.deploy("USDT", "Tether USD", 6, {"from": accounts[0]})


@pytest.fixture(scope="module")
def USDC(accounts):
    token = compile_source(ERC20).Token
    yield token.deploy("USDC", "USD//C", 6, {"from": accounts[0]})


@pytest.fixture(scope="module")
def SUSD(accounts):
    token = compile_source(ERC20).Token
    yield token.deploy("sUSD", "Synth sUSD", 18, {"from": accounts[0]})


@pytest.fixture(scope="module")
def TUSD(accounts):
    token = compile_source(ERC20).Token
    yield token.deploy("TUSD", "TrueUSD", 18, {"from": accounts[0]})


@pytest.fixture(scope="module")
def BUSD(accounts):
    token = compile_source(ERC20).Token
    yield token.deploy("BUSD", "Binance USD", 18, {"from": accounts[0]})
