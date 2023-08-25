from typing import Union


def format_number(value: Union[int, float], prefix: str = "R$") -> str:
    """
    Format number according to the Brazilian standard
    :param value: number to be formatted
    :param prefix: prefix to be added to the number
    :return: formatted number
    """
    suffixes = ["", " mil", " mi", " bi"]
    divisor = [1, 1000, 1000000, 1000000000]
    for i in range(len(divisor) - 1, -1, -1):
        if value >= divisor[i]:
            return f"{prefix}{value/divisor[i]:,.2f}{suffixes[i]}".replace(
                ",", "."
            ).replace("$", "$ ")
    return f"{prefix}{value:,.2f}".replace(",", ".").replace("$", "$ ")
