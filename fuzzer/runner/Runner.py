class Runner(object):
    # Test outcomes
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self):
        """Initialize"""
        pass

    # 用于将input（字符串）传递给程序运行。run（）会返回一对值（result，outcome），这里的result是run运行后结果的返回值
    def run(self, inp):
        """Run the runner with the given input"""
        return inp, Runner.UNRESOLVED
