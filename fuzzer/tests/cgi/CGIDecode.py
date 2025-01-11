def cgi_decode(s):
    """Decode the CGI-encoded string `s`:
       * replace "+" by " "
       * replace "%xx" by the character with hex number xx.
       Return the decoded string.  Raise `ValueError` for invalid inputs."""

    # Mapping of hex digits to their integer values
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }

    t = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == '+':
            t += ' '
        elif c == '%':
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 2
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t

    # with Coverage() as cov:
    #     cgi_decode("a+b")
    #
    # print(cov.coverage())

    # 可以找出某个测试用例涵盖哪些行，而某些测试用例则无法覆盖;定义cov_max为我们可以实现的最大覆盖范围
    # with Coverage() as cov_plus:
    #     cgi_decode("a+b")
    # with Coverage() as cov_standard:
    #     cgi_decode("abc")
    #
    # print(cov_plus.coverage() - cov_standard.coverage())

    # 还可以比较集合以找出哪些行仍需要覆盖
    # with Coverage() as cov_max:
    #     cgi_decode('+')
    #     cgi_decode('%20')
    #     cgi_decode('abc')
    #     try:
    #         cgi_decode('%?a')
    #     except:
    #         pass
