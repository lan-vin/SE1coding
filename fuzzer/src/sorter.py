def sort_by_coverage(seeds):
    return sorted(seeds, key=lambda x: x['coverage'], reverse=True)