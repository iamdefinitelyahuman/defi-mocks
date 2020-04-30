# defi-mocks

[Brownie](https://github.com/iamdefinitelyahuman/brownie) `pytest` fixtures for testing popular DeFi projects.

## Disclaimer

This project is an early work in progress. No guarantees are made about stability or functionality. Force pushes to master are likely. **USE AT YOUR OWN RISK!**

If you find this interesting and want to contribute, feel free to reach out in the Brownie [Gitter channel](https://gitter.im/eth-brownie/community).

## Usage

This repository provides two sets of test fixtures:

* **Local** fixtures primarily rely on mocking and are intended for quick testing during development
* **Forked** fixtures interact with real deployments on a forked mainnet

Both fixture sets have identical APIs and may be used interchangeably within your tests. A pytest hook in `tests/conftest.py` determines which set to load based on the active network.

To use these fixtures, add the contents of this project's `tests/` folder within your own project.

To run your test suite using the local fixtures:

```bash
brownie test --network development
```

To run using the forked fixtures:

```bash
brownie test --network mainnet-fork
```

## Testing

Each fixture set includes a set of tests in `test_smoke.py`. These tests are normally skipped when running your regular test suite. To run them:

```bash
brownie test tests/fixtures
```

Be sure to include the `--network` flag to target a specific fixture set.

## Development

Each fixture set should be placed within it's own folder inside `tests/fixtures`. A fixture set should include the following files:

* `__init__.py`: can be empty, but must be included
* `forked.py`: fixtures for forked mainnet testing
* `local.py`: fixtures for local testing
* `README.md`: documentation on how to use the fixtures
* `test_smoke.py`: fixture unit tests

See the existing fixture sets for examples to help you get started.

## License

This project is licensed under the [MIT license](LICENSE).
