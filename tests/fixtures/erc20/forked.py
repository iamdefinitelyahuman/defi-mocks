import pytest


@pytest.fixture(scope="module")
def _MintableTestToken(Contract, accounts, uniswap_factory):

    class MintableTestToken(Contract):

        def __init__(self, address):
            super().__init__(address)
            self._uniswap = Contract(uniswap_factory.getExchange(address))

        def _mint_for_testing(self, amount, tx={'from': accounts[0]}):
            account = tx.get('from', self._accounts[0])
            self._uniswap.ethToTokenSwapOutput(
                amount, 10000000000, {'from': account, "value": account.balance()}
            )

    yield _MintableTestToken


@pytest.fixture(scope="module")
def DAI(_MintableTestToken):
    yield _MintableTestToken("0x6B175474E89094C44Da98b954EedeAC495271d0F")


@pytest.fixture(scope="module")
def USDT(_MintableTestToken):
    yield _MintableTestToken("0xdAC17F958D2ee523a2206206994597C13D831ec7")


@pytest.fixture(scope="module")
def USDC(_MintableTestToken):
    yield _MintableTestToken("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")


@pytest.fixture(scope="module")
def SUSD(_MintableTestToken):
    yield _MintableTestToken("0x57Ab1ec28D129707052df4dF418D58a2D46d5f51")


@pytest.fixture(scope="module")
def TUSD(_MintableTestToken):
    yield _MintableTestToken("0x0000000000085d4780B73119b644AE5ecd22b376")


@pytest.fixture(scope="module")
def BUSD(_MintableTestToken):
    yield _MintableTestToken("0x4Fabb145d64652a948d72533023f6E7A623C7C53")
