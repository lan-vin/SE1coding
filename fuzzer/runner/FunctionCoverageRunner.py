from runner.FunctionRunner import FunctionRunner
from src.Coverage import Coverage


class FunctionCoverageRunner(FunctionRunner):
    def __init__(self, function):
        super().__init__(function)
        self._coverage = None

    def run_function(self, inp):
        with Coverage() as cov:
            try:
                result = super().run_function(inp)
            except Exception as exc:
                self._coverage = cov.coverage()
                raise exc

        self._coverage = cov.coverage()
        return result

    def coverage(self):
        return self._coverage
