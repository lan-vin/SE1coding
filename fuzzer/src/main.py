# def main():
#     target = 'your_target_program'
#     instrument(target)
#
#     seeds = [{'data': b'seed1', 'coverage': 0, 'execution_time': 0}]
#     for seed in seeds:  
#         mutated_seed = bitflip(seed['data'])
#         execution_time = execute('instrumented_' + target)
#         log_results(execution_time, seed['coverage'])
#         # 更新覆盖率等信息
#         # ...
#
#     plot_coverage([seed['coverage'] for seed in seeds])
#
# if __name__ == '__main__':
#     main()
from matplotlib import pyplot as plt

from fuzzer.MutationCoverageFuzzer import MutationCoverageFuzzer
from fuzzer.MutationFuzzer import MutationFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from runner.FunctionRunner import FunctionRunner
from src.Coverage import read_gcov_coverage, population_coverage
from src.mutator import mutate
from tests.url.urlparse import is_valid_url, http_program

# # 产生随机的字符，并将它们添加到缓冲区字符串变量（out）里，最后返回字符串
# def fuzzer(max_length=100, char_start=32, char_range=32):
#     """一个字符串最多有`max_length`个字符，随机生成字符的ASCII码范围为 [`char_start`, `char_start` + `char_range`]"""
#     string_length = random.randrange(0, max_length + 1)
#     out = ""
#     for i in range(0, string_length):
#         out += chr(random.randrange(char_start, char_start + char_range))
#     return out


cgi_c_code = """
/* CGI decoding as C program */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

"""
cgi_c_code += r"""
int hex_values[256];

void init_hex_values() {
    for (int i = 0; i < sizeof(hex_values) / sizeof(int); i++) {
        hex_values[i] = -1;
    }
    hex_values['0'] = 0; hex_values['1'] = 1; hex_values['2'] = 2; hex_values['3'] = 3;
    hex_values['4'] = 4; hex_values['5'] = 5; hex_values['6'] = 6; hex_values['7'] = 7;
    hex_values['8'] = 8; hex_values['9'] = 9;

    hex_values['a'] = 10; hex_values['b'] = 11; hex_values['c'] = 12; hex_values['d'] = 13;
    hex_values['e'] = 14; hex_values['f'] = 15;

    hex_values['A'] = 10; hex_values['B'] = 11; hex_values['C'] = 12; hex_values['D'] = 13;
    hex_values['E'] = 14; hex_values['F'] = 15;
}
"""
cgi_c_code += r"""
int cgi_decode(char *s, char *t) {
    while (*s != '\0') {
        if (*s == '+')
            *t++ = ' ';
        else if (*s == '%') {
            int digit_high = *++s;
            int digit_low = *++s;
            if (hex_values[digit_high] >= 0 && hex_values[digit_low] >= 0) {
                *t++ = hex_values[digit_high] * 16 + hex_values[digit_low];
            }
            else
                return -1;
        }
        else
            *t++ = *s;
        s++;
    }
    *t = '\0';
    return 0;
}
"""
cgi_c_code += r"""
int main(int argc, char *argv[]) {
    init_hex_values();

    if (argc >= 2) {
        char *s = argv[1];
        char *t = malloc(strlen(s) + 1); /* output is at most as long as input */
        int ret = cgi_decode(s, t);
        printf("%s\n", t);
        return ret;
    }
    else
    {
        printf("cgi_decode: usage: cgi_decode STRING\n");
        return 1;
    }
}
"""

if __name__ == '__main__':
    http_runner = FunctionCoverageRunner(http_program)
    print(http_runner.run("https://foo.bar/"))

    seed_input = "http://www.google.com/search?q=fuzzing"
    mutation_fuzzer = MutationCoverageFuzzer(seed=[seed_input])
    mutation_fuzzer.runs(http_runner, trials=10000)

    all_coverage, cumulative_coverage = population_coverage(
        mutation_fuzzer.population, http_program)

    plt.plot(cumulative_coverage)
    plt.title('Coverage of urlparse() with random inputs')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')
    plt.show()
