# Класс КОМПЛЕКСНОЕ ЧИСЛО


class ComplexNumber:
    """
    Класс ComplexNumber без перегрузки операторов
    """

    # Конструктор - магический метод, который создает объект класс и инициализирует поля этого объекта
    def __init__(self, real, imaginary):
        """
        Магический метод создания объекта комплексного числа (Метод-Конструктор)

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса
            real: int/float - реальная часть комплексного числа
            imaginary: int/float - мнимая часть комплексного числа

        Магический метод __init__ не возвращает ничего и не должен этого делать по правилам Python
        """
        self.real = real
        self.imaginary = imaginary

    # Методы-геттеры
    def get_real(self):
        return self.real

    def get_imaginary(self):
        return self.imaginary

    # Метод сложения двух комплексных чисел
    def add(self, rhs):
        """
        Метод сложения двух комплексных чисел

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса
                   в данном случае self заменяет LEFT HAND SIDE
            rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции

        Метод возвращает результат сложения - сумму
        """
        result_real = self.get_real() + rhs.get_real()
        result_imaginary = self.get_imaginary() + rhs.get_imaginary()

        return ComplexNumber(result_real, result_imaginary)

    # Метод вычитания двух комплексных чисел
    def sub(self, rhs):
        """
        Метод вычитания двух комплексных чисел

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса
                   в данном случае self заменяет LEFT HAND SIDE
            rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции

        Метод возвращает результат вычитания - разность
        """
        result_real = self.get_real() - rhs.get_real()
        result_imaginary = self.get_imaginary() - rhs.get_imaginary()

        return ComplexNumber(result_real, result_imaginary)

    # Метод умножения двух комплексных чисел
    def mul(self, rhs):
        """
        Метод умножения двух комплексных чисел

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса
                   в данном случае self заменяет LEFT HAND SIDE
            rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции

        Метод возвращает результат умножение - произведение
        """

        real_real = self.get_real() * rhs.get_real()
        imag_imag = self.get_imaginary() * rhs.get_imaginary() * (-1)
        imag_real = self.get_imaginary() * rhs.get_real()
        real_imag = self.get_real() * rhs.get_imaginary()

        result_real = real_real + imag_imag
        result_imaginary = imag_real + real_imag

        return ComplexNumber(result_real, result_imaginary)

    # Метод деления одного комплексного числа на другое
    def div(self, devider):
        """
        Метод умножения двух комплексных чисел

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса
                   в данном случае self заменяет devidend (делимое)
            devider: ComplexNumber - делитель

        Метод возвращает результат умножение - произведение
        """
        # комплексное сопряжение
        devider_linked = ComplexNumber(devider.get_real(), -devider.get_imaginary())

        # получение числителя и знаменателя дроби, возникающей в процессе деления
        # умножения делителя на комплексное сопряжение к делителю
        result_denominator = devider.mul(
            devider_linked
        )  # вещественное число в результате

        # умножения делимого на комплексное сопряжение к делителю
        result_numerator = self.mul(devider_linked)  # комплексное число в результате

        # учет знаменателя в числителе (деление комплексного числа на вещественное)
        # деление реальной части числителя на общий знаменатель
        result_numerator_real = (
            result_numerator.get_real() / result_denominator.get_real()
        )
        # деление мнимой части числителя на общий знаменатель
        result_numerator_imaginary = (
            result_numerator.get_imaginary() / result_denominator.get_real()
        )

        # получение итогового комплексного числа
        return ComplexNumber(result_numerator_real, result_numerator_imaginary)

    # Магический метод приведение класса комплексного числа в арифметической форме к строке
    def __str__(self):
        """
        Метод приведение класса комплексного числа в арифметической форме к строке

        Аргументы:
            self - специальный параметр, передаваемый во все методы класса

        Метод __str__ должен возвращать СТРОКУ, которая будет являться символьным
        обозначением объекта вашего класса
        """
        if self.imaginary > 0:
            return f"{self.real} + {self.imaginary}"
        else:
            return f"{self.real} - {-self.imaginary}"


c1 = ComplexNumber(-12, -2.41)
c2 = ComplexNumber(21, 33)

print("Сумма: " + str(c1.add(c2)))
print("Вычитание: " + str(c1.sub(c2)))
print("Умножение: " + str(c1.mul(c2)))
print("Деление: " + str(c1.div(c2)))
