# Introdução

#   A classe string do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho triviç, porém, em Python esse trabalho é muito simples

# Maiúscula, minúscula e título


curso = "pYtHon"

print(curso.upper())
#>>>PYTHON

print(curso.lower())
#>>>python

print(curso.title())
#>>>Python

# Eliminando espaços em branco

curso = "      Python"

print(curso.strip())
#>>>"Python"

print(curso.lstrip())
#>>>"Python    "

print(curso.rstrip)
#>>>"  Python"

#Junções e centralizações

curso = "Python"

print(curso.center(10, "#"))
#>>>"##Python#"

print(".".join(curso))
#>>>"P.y.t.h.o.n"