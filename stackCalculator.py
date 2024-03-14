from GUI import *
import GUI
priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}  # 연사자의 우선 순위(숫자가 클수록 더 높은 우선 순위)
num = []
output_stack = None
stack = None

class Stack():
    def __init__(self):
        self.stack = []
        print("생성 완료")

    def __len__(self):
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) <= 0

    def is_full(self) -> bool:
        return len(self.stack) >= 256

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            print("Stack is empty")

    def push(self, value):
        if self.is_full():
            print("Stack is OverFlow!")
        else:
            self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is UnderFlow! It's Empty!")
        else:
            return self.stack.pop()

    def pop1(self):  # 파이썬에서는 오버로딩을 지원하지 않는다.
        # 오버로딩, 오버라이딩 개념 다시 정리
        # https://junior-datalist.tistory.com/96
        # 오버로딩시 @dispatch 어노테이션을 사용해서 오버로딩 사용가능
        if self.is_empty():
            print("Stack is UnderFlow! It's Empty!")
        else:
            return self.stack.pop(0)

    def find(self, value):
        try:
            print("Exist : ", value, " at ", self.stack.index(value))
            return self.stack.index(value)
        except ValueError:
            return -1

    def Stack_Print(self):
        return self.stack

    def peek(self):
        return self.stack[-1]

    def Clear(self):
        self.stack = []
        print("Stack is Clear!")


output_stack = Stack()
stack = Stack()


def IsDigit(num):
    try:
        num = int(num)
        return True
    except:
        return False


def click_number(value):
    num.append(value)


def list_to_int():
    return int("".join(num))


def list_to_float():
    return float("".join(num))


def Calculation(operator, x, y):
    result = 0
    if operator == '*':
        result = y * x
        print("result : ", result)
    elif operator == '/':
        if x == 0:
            print("0은 나눌 수 없습니다. \n 프로그램을 종료합니다.")
            return 0
        result = y / x
        print("result : ", result)
    elif operator == '+':
        result = y + x
        print("result : ", result)
    elif operator == '-':
        result = y - x
        print("result : ", result)
    if output_stack.is_empty():
        print("Final : ", result)
        #answer_text(str(result))

        return result
    stack.push(result)


def PostFix(calline):
    print("postfix")

    print("cal : ", calline)
    tmp = []
    for i in calline:
        if IsDigit(i) or i == ".":
            num.append(i)
        elif i == "(":
            tmp.append(i)
        elif i == ")":
            if len(num) == 0:
                tmp.append(i)
            else:
                if "." in num:
                    tmp.append(list_to_float())
                else:
                    tmp.append(list_to_int())
                num.clear()
                tmp.append(i)
        elif i in priority:
            if len(num) == 0:
                tmp.append(i)
            else:
                if "." in num:
                    tmp.append(list_to_float())
                    print(num)
                    num.clear()
                else:
                    tmp.append(list_to_int())
                    print(num)
                    num.clear()

                tmp.append(i)
                print(num)
    if len(num) != 0:
        if "." in num:
            tmp.append(list_to_float())
        else:
            tmp.append(list_to_int())
    print(tmp)
    for i in tmp:
        # 정수인가
        if IsDigit(i):
            output_stack.push(i)
        # 연산자인가
        elif i == "(":
            stack.push("(")
        elif i == ")":
            print(")")
            while stack.top() != "(":
                output_stack.push(stack.pop())
            a = stack.pop()
            print(a)
        elif stack.is_empty():
            stack.push(i)
        elif i in priority:
            while (not stack.is_empty()) and (priority[stack.top()] >= priority[i]):
                # if priority[stack.top()] >= priority[a]:
                output_stack.push(stack.pop())
            stack.push(i)
    while not stack.is_empty():
        output_stack.push(stack.pop())
    while not output_stack.is_empty():
        outputstackvalue = output_stack.pop1()
        if IsDigit(outputstackvalue):
            stack.push(outputstackvalue)
        else:
            x = stack.pop()
            y = stack.pop()
            print("x : ", x)
            print("y : ", y)
            a = Calculation(outputstackvalue, x, y)
        print("outputstackvalue", outputstackvalue)
        print("stack : ", stack.Stack_Print())
    print("Finish")

    print(stack.Stack_Print())
    print(output_stack.Stack_Print())
    print(calline)
    tmp.clear()
    return a