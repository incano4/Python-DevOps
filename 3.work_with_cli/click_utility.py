#!/usr/bin/env python

"""
С помощью библиотеки click создать утилиту командной строки, принимающую в качестве аргумента название и 
выводящую его в случае, если оно начинается не с символа p.
"""

import click

@click.command()
@click.option('--name', help='Определяет аргумент функции')
def using_click(name):
    if (name[0] == 'p') or (name[0] == 'P'):
        print(f"Имя не должно начинаться с 'P'")
    else:
        print(f"Введеное название аргумента: ", name)

if __name__ == '__main__':
    using_click()