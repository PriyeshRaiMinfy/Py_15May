def calculate():
    try:
        op = input('''
Choose operation: + | - | * | /
''')

        nums = input("Enter numbers separated by space: ").split()
        print(nums)
        nums = [float(n) for n in nums]
        # print(nums)

        if len(nums) < 2:
            print("Enter at least two numbers.")
            return

        result = nums[0]

        if op == '+':
            for n in nums[1:]:
                result += n
            print(" + ".join(map(str, nums)), '=', result)

        elif op == '-':
            for n in nums[1:]:
                result -= n
            print(" - ".join(map(str, nums)), '=', result)

        elif op == '*':
            for n in nums[1:]:
                result *= n
            print(" * ".join(map(str, nums)), '=', result)

        elif op == '/':
            try:
                for n in nums[1:]:
                    if n == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    result /= n
                print(" / ".join(map(str, nums)), '=', result)
            except ZeroDivisionError as e:
                print("Error:", e)

        else:
            print("Invalid operator.")

    except ValueError:
        print("Error: Please enter valid numbers.")

calculate()
