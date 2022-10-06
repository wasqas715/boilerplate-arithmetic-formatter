def arithmetic_arranger(problems, solution=False):
    line_a, line_b, line_c, line_d = [], [], [], []
    
    # Checks if input was more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Split the input into the two numbers and sign
        eq_1 = problem.split()
        num_1, sign, num_2 = eq_1[0], eq_1[1], eq_1[2]

        # Ensure nums are digits
        if not num_1.isdigit() or not num_2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Ensure sign is + | -
        if sign == '+':
            Ans = str(int(num_1) + int(num_2))
        elif sign == '-':
            Ans = str(int(num_1) - int(num_2))
        else:
            return "Error: Operator must be '+' or '-'."
        sign = sign + ' '

        # Spacing of digits
        if len(num_1) >= len(num_2):
            diff = len(num_1) - len(num_2)
            num_2 = ' ' * diff + num_2
        elif len(num_2) >= len(num_1):
            diff = len(num_2) - len(num_1)
            num_1 = ' ' * diff + num_1

       # Formatting and Appending results to list
        secondline = sign + num_2
        thirdline = len(secondline) * '-'

        line_a.append('  ' + num_1)
        line_b.append(sign + num_2)
        line_c.append(len(secondline) * '-')
        line_d.append(' ' * (len(thirdline) - len(Ans)) + Ans)
    # Spacing for the final result
    master_a = '    '.join(line_a)
    master_b = '    '.join(line_b)
    master_c = '    '.join(line_c)
    master_d = '    '.join(line_d)

    if solution == True:
        return master_a + '\n' + master_b + '\n' + master_c + '\n' + master_d
    else:
        return master_a + '\n' + master_b + '\n' + master_c