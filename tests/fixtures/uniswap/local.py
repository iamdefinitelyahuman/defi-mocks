import json
from pathlib import Path
import pytest

base_path = Path(__file__).parent


@pytest.fixture(scope="module")
def uniswap_factory(Contract, accounts):
    with base_path.joinpath("bytecode.json").open() as fp:
        bytecode = json.load(fp)

    with base_path.joinpath("abi-factory.json").open() as fp:
        factory_abi = json.load(fp)

    template_address = accounts[0].transfer(data=bytecode["exchange_template"]).contract_address
    factory_address = accounts[0].transfer(data=bytecode["factory"]).contract_address

    factory = Contract.from_abi("UniswapFactory", factory_address, factory_abi)
    factory.initializeFactory(template_address, {"from": accounts[0]})

    yield factory


@pytest.fixture(scope="module")
def uniswap_dai(Contract, accounts, uniswap_factory, dai):
    with base_path.joinpath("abi-exchange.json").open() as fp:
        exchange_abi = json.load(fp)

    tx = uniswap_factory.createExchange(dai, {"from": accounts[0]})
    exchange_address = tx.new_contracts[0]

    yield Contract.from_abi("UniswapFactory", exchange_address, exchange_abi)
