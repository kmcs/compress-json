from number import num_to_s, s_to_num

def test(num, expected_s):
  s = num_to_s(num)

  if not s == expected_s:
    raise Exception(f"[num_to_s fail] num: {num}, expected_s: {expected_s} s: {s}")

  decoded_num = s_to_num(s)

  if not num == decoded_num:
    raise Exception(f"[s_to_num fail] num: {num}, s: {s}, decoded_num: {decoded_num}")

  print("[pass]", num)

# single digit positive integer
## 0-9
test(0, '0')
test(1, '1')
test(9, '9')
## A-Z
test(10, 'A')
test(11, 'B')
test(35, 'Z')
## a-z
test(36, 'a')
test(37, 'b')
test(61, 'z')

# single digit negative integer
test(-1, '-1')
test(-61, '-z')

# multi-digit positive integer
test(62, '10')
test(63, '11')
test(3843, 'zz')
test(3844, '100')

# multi-digit negative integer
test(-62, '-10')
test(-63, '-11')
test(-3843, '-zz')
test(-3844, '-100')
