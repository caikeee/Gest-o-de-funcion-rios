from datetime import datetime # para manipular datas
from decimal import Decimal #manipula decimais de maneira precisa
from collections import defaultdict #criação de dicionários com valores padrão.
from operator import attrgetter #pega atributos de objetos de forma fácil.


class Pessoa:
  def __init__(self, nome , data_nascimento):
    self.nome = nome
    self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y") ## Converte  data_nascimento para um objeto datetime
 
  def __str__(self): ## método que retorna uma representação em string do objeto
        return f'{self.nome} ({self.data_nascimento.strftime("%d/%m/%Y")})'
  


class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, salario, funcao):
        super().__init__(nome, data_nascimento)
        self.salario = Decimal(salario)  # converte salario para um objeto Decimal
        self.funcao = funcao
        
    def __str__(self):
        salario_formatado = f'{self.salario:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")# formata o salário com separadores de milhar e decimal
        return f'{self.nome}, {self.data_nascimento.strftime("%d/%m/%Y")}, {self.funcao}, {salario_formatado}' # devolve os atributos como string

    



funcionarios = [
    Funcionario("Maria", "18/10/2000", "2009.44", "Operador"),
    Funcionario("João", "12/05/1990", "2284.38", "Operador"),
    Funcionario("Caio", "02/05/1961", "9836.14", "Coordenador"),
    Funcionario("Miguel", "14/10/1988", "19119.88", "Diretor"),
    Funcionario("Alice", "05/01/1995", "2234.68", "Recepcionista"),
    Funcionario("Heitor", "19/11/1999", "1582.72", "Operador"),
    Funcionario("Arthur", "31/03/1993", "4071.84", "Contador"),
    Funcionario("Laura", "08/07/1994", "3017.45", "Gerente"),
    Funcionario("Heloísa", "24/05/2003", "1606.85", "Eletricista"),
    Funcionario("Helena", "02/09/1996", "2799.93", "Gerente")
]

# REMOVE JOÃO DA LISTA
funcionarios = [f for f in funcionarios if f.nome != "João"] 

# IMPRIMI FUNCIONARIOS E SUAS INFORMAÇÕES
print("Funcionários:")
for f in funcionarios:
    print(f)

# AUMENTANDO SALARIO
for f in funcionarios:
    f.salario *= Decimal("1.10")

# AGRUPANDO PELA FUNÇÃO
funcionarios_por_funcao = defaultdict(list)
for f in funcionarios:
    funcionarios_por_funcao[f.funcao].append(f)

# IMPRIME FUNCIONARIOS AGRUPADOS NA FUNÇÃO
print("\nFuncionários agrupados por função:")
for funcao, funcs in funcionarios_por_funcao.items():
    print(funcao + ":")
    for f in funcs:
        print("  " + f.nome)

#IMPRIME FUNCIONARIOS QUE FAZEM ANIVERSARIO NOS MESES 10 E 12
print("\nFuncionários que fazem aniversário em outubro e dezembro:")
for f in funcionarios:
    if f.data_nascimento.month in [10, 12]:
        print(f.nome)

# IMPRIME FUNCIOANRIO MAIS VELHO
mais_velho = min(funcionarios, key=attrgetter('data_nascimento'))
idade_mais_velho = (datetime.now() - mais_velho.data_nascimento).days // 365
print(f"\nFuncionário com a maior idade: {mais_velho.nome}, {idade_mais_velho} anos")

# IMPRIME A LISTA DE FUNCIONARIOS POR ORDEM ALFABETICA
print("\nFuncionários em ordem alfabética:")
for f in sorted(funcionarios, key=attrgetter('nome')):
    print(f.nome)

# IMPRIMIR O TOTAL DE SALARIOS POR FUNCIOINARIO
total_salarios = sum(f.salario for f in funcionarios)
print("\nTotal dos salários: " + f'{total_salarios:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))

# IMPRIMIR QUANTOS SALARIOS MINIMOS O FUNCIONARIO GANHA
salario_minimo = Decimal("1212.00")
print("\nSalários em múltiplos do salário mínimo:")
for f in funcionarios:
    multiplos_salario_minimo = f.salario / salario_minimo
    print(f"{f.nome}: {multiplos_salario_minimo:.2f}")