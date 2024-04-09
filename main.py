def main(calc_data: str):
    calc_list = calc_data.split(' ')
    operators = ['+', '-', '*', '/']

    if len(calc_list) < 3 or len(calc_list) > 3:
        return Exception('throws Exception 1')

    try:
        left_operand = int(calc_list[0])
        right_operand = int(calc_list[2])
    except:
        return Exception('throws Exception 2')

    if left_operand > 10 or right_operand > 10:
        return Exception('throws Exception 3')

    if calc_list[1] in operators:
        return calculation(left_operand, right_operand, calc_list[1])
    else:
        return Exception('throws Exception 4')


def calculation(left_operand: int, right_operand: int, operator: str):
    if operator == '+':
        return f'{left_operand + right_operand}'
    elif operator == '-':
        return f'{left_operand - right_operand}'
    elif operator == '*':
        return f'{left_operand * right_operand}'
    elif operator == '/':
        try:
            return f'{left_operand // right_operand}'
        except:
            return Exception('throws Exception 5')


calc_input = input()
p = main(calc_input)
print(p)
