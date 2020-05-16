import importlib
from pathlib import Path

from brownie._config import CONFIG

base_path = Path(__file__).parent


def pytest_configure(config):

    if config.getoption("network"):
        network = config.getoption("network")
    else:
        network = CONFIG.settings['networks']['default']

    # add forked or local fixtures depending on the active network
    plugin_target = "forked" if "fork" in network else "local"
    for path in base_path.glob(f"fixtures/**/{plugin_target}.py"):
        path = path.relative_to(base_path)
        path = path.with_suffix('')
        import_path = f"tests/{path.as_posix()}".replace('/', '.')

        module = importlib.import_module(import_path)
        config.pluginmanager.register(module, f"defi-fixtures-{path.parent.stem}")


def pytest_ignore_collect(path, config):
    # only load smoke tests when `tests/fixtures` is specifically targetted
    test_folder = Path(path).relative_to(base_path).parts[0]
    invocation_path = config.invocation_params.args[0]
    if test_folder == "fixtures" and not invocation_path.startswith("tests/fixtures"):
        return True
