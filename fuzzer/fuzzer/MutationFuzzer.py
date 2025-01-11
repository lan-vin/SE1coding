import random

from fuzzer.Fuzzer import Fuzzer
from src.mutator import mutate


class MutationFuzzer(Fuzzer):
    def __init__(self, seed, min_mutations=2, max_mutations=10):
        super().__init__()
        self.seed_index = None
        self.population = None
        self.seed = seed
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.reset()

    def reset(self):
        self.population = self.seed
        self.seed_index = 0


class MutationFuzzer(MutationFuzzer):
    def mutate(self, inp):
        return mutate(inp)


class MutationFuzzer(MutationFuzzer):
    # 从当前（self.population）中随机选择一些输入，然后在min_mutations和max_mutations之间变异步骤应用，返回最终结果
    def create_candidate(self):
        candidate = random.choice(self.population)
        trials = random.randint(self.min_mutations, self.max_mutations)
        for i in range(trials):
            candidate = self.mutate(candidate)
        return candidate


class MutationFuzzer(MutationFuzzer):
    # fuzz()方法设置为首先使用seed；当这些用完后，我们进行变异
    def fuzz(self):
        if self.seed_index < len(self.seed):
            # Still seeding
            self.inp = self.seed[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp
