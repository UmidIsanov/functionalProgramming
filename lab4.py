class Command:
    def execute(self):
        raise NotImplementedError()

    def undo(self):
        raise NotImplementedError()


class Calculator:
    def __init__(self):
        self._value = 0

    def add(self, value):
        self._value += value
        print(f"Добавлено {value}. Текущее значение: {self._value}.")

    def subtract(self, value):
        self._value -= value
        print(f"Вычтено {value}. Текущее значение: {self._value}.")


class AddCommand(Command):
    def __init__(self, calculator, value):
        self._calculator = calculator
        self._value = value

    def execute(self):
        self._calculator.add(self._value)

    def undo(self):
        self._calculator.subtract(self._value)


class SubtractCommand(Command):
    def __init__(self, calculator, value):
        self._calculator = calculator
        self._value = value

    def execute(self):
        self._calculator.subtract(self._value)

    def undo(self):
        self._calculator.add(self._value)


class CalculatorInvoker:
    def __init__(self):
        self._history = []

    def execute_command(self, command):
        command.execute()
        self._history.append(command)

    def undo_last_command(self):
        if self._history:
            command = self._history.pop()
            command.undo()


calculator = Calculator()
invoker = CalculatorInvoker()

add_command = AddCommand(calculator, 10)
subtract_command = SubtractCommand(calculator, 5)

invoker.execute_command(add_command)
invoker.execute_command(subtract_command)
invoker.undo_last_command()
