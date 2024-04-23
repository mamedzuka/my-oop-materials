# Абстрактный тип КОМПЛЕКСНОЕ ЧИСЛО


# Конструктор - создает объект абстрактного типа!
def complex_constructor(real, imaginary):
    """
    Функция создания объекта комплексного числа
    real: int/float - реальная часть комплексного числа
    imaginary: int/float - мнимая часть комплексного числа
    Функция возвращает dict, симулирующий комплексное число
    """
    return {"real": real, "imaginary": imaginary}


# Функция-геттер, позволяющая получать изолировано свойства объектов абстрактных типов
def get_real(complex_number):
    """
    Функция получения реальной части комплексного числа
    """
    return complex_number["real"]


def get_imaginary(complex_number):
    """
    Функция получения реальной части комплексного числа
    """
    return complex_number["imaginary"]


# Функции арифметических операций
def add_complex(lhs, rhs):
    """
    Функция сложения двух комплексных чисел
    lhs: Complex - LEFT HAND SIDE - располагается слева от мат. операции
    rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции
    """
    result_real = get_real(lhs) + get_real(rhs)
    result_imaginary = get_imaginary(lhs) + get_imaginary(rhs)

    result_complex = complex_constructor(result_real, result_imaginary)
    return result_complex


def sub_complex(lhs, rhs):
    """
    Функция вычитания двух комплексных чисел
    lhs: Complex - LEFT HAND SIDE - располагается слева от мат. операции
    rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции
    """
    result_real = get_real(lhs) - get_real(rhs)
    result_imaginary = get_imaginary(lhs) - get_imaginary(rhs)

    result_complex = complex_constructor(result_real, result_imaginary)
    return result_complex


def mul_complex(lhs, rhs):
    """
    Функция умножения двух комплексных чисел
    lhs: Complex - LEFT HAND SIDE - располагается слева от мат. операции
    rhs: Complex - RIGHT HAND SIDE - располагается справа от мат. операции
    """
    real_real = get_real(lhs) * get_real(rhs)
    imag_imag = get_imaginary(lhs) * get_imaginary(rhs) * (-1)
    imag_real = get_imaginary(lhs) * get_real(rhs)
    real_imag = get_real(lhs) * get_imaginary(rhs)

    result_real = real_real + imag_imag
    result_imaginary = imag_real + real_imag

    result_complex = complex_constructor(result_real, result_imaginary)
    return result_complex


def div_complex(dividend, devider):
    """
    Функция деления комплексного числа на комплексное числл
    dividend: Complex - делимое
    devider: Complex  - делитель

    devider_linked - комплексное сопряженное к делителю
    """
    # комплексное сопряжение
    devider_linked = complex_constructor(get_real(devider), -get_imaginary(devider))

    # получение числителя и знаменателя дроби, возникающей в процессе деления
    # умножения делителя на комплексное сопряжение к делителю
    result_denominator = mul_complex(
        devider, devider_linked
    )  # вещественное число в результате
    # умножения делимого на комплексное сопряжение к делителю
    result_numerator = mul_complex(
        dividend, devider_linked
    )  # комплексное число в результате

    # учет знаменателя в числителе (деление комплексного числа на вещественное)
    # деление реальной части числителя на общий знаменатель
    result_numerator_real = get_real(result_numerator) / get_real(result_denominator)
    # деление мнимой части числителя на общий знаменатель
    result_numerator_imaginary = get_imaginary(result_numerator) / get_real(
        result_denominator
    )

    # получение итогового комплексного числа
    result_complex = complex_constructor(
        result_numerator_real, result_numerator_imaginary
    )
    return result_complex


# Функция вывода комплексного числа
def print_complex(complex_number):
    """
    Функция вывода в консоль комплексного числа
    """
    # Re + Im = a + bi
    if get_imaginary(complex_number) > 0:
        print(f"{get_real(complex_number)} + {get_imaginary(complex_number)}i")
    else:
        print(f"{get_real(complex_number)} - {-get_imaginary(complex_number)}i")


def complex_to_str(complex_number):
    """
    Функция превращения алгебраической формы комплексного числа в строку
    """
    if get_imaginary(complex_number) > 0:
        return f"{get_real(complex_number)} + {get_imaginary(complex_number)}i"
    else:
        return f"{get_real(complex_number)} - {-get_imaginary(complex_number)}i"


c1 = complex_constructor(-12, -2.41)
c2 = complex_constructor(21, 33)

print("Сумма: " + complex_to_str(add_complex(c1, c2)))
print("Вычитание: " + complex_to_str(sub_complex(c1, c2)))
print("Умножение: " + complex_to_str(mul_complex(c1, c2)))
print("Деление: " + complex_to_str(div_complex(c1, c2)))
