def log_results(execution_time: float, coverage: float):
    with open('results/log.txt', 'a') as f:
        f.write(f'Execution Time: {execution_time}, Coverage: {coverage}\n')