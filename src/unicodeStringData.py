def dbl2singleChar(a):
    # 전각문자
    full = a
    # 전각문자와 반각문자의 차이
    diff = '0xfee0'
    # 전각문자 블랭크
    blank = '0x3000'

    # 16진수인 ascii code
    hex_ascii_full = ord(full)
    hex_ascii_diff = int(diff, 16)
    hex_ascii_blank = int(blank, 16)

    # 16진수 형태의 string
    hex_full = hex(hex_ascii_full)
    hex_blank = hex(hex_ascii_blank)

    result = a
    # 전각일 경우 전각 기준인 값을 차감해 반각으로 변경
    if hex_ascii_full >= hex_ascii_diff:
        result = hex_ascii_full - hex_ascii_diff
    # 빈칸이 전각일 경우는 위 공식에 어긋나므로 강제로 반각형태의 빈칸을 지정
    elif hex_ascii_full == hex_ascii_blank:
        result = hex_blank
    return str(result)

def dbl2singleStr(s):
    ret = u""
    for i in s:
        ret += dbl2singleChar(i)
    return ret

