import importlib
import unittest


class ImportTests(unittest.TestCase):
    def test_server_module_imports(self):
        module = importlib.import_module("illustrator.server")
        self.assertTrue(callable(module.main))

    def test_cli_exposes_run_server(self):
        module = importlib.import_module("illustrator.cli")
        self.assertTrue(callable(module.run_server))


if __name__ == "__main__":
    unittest.main()
