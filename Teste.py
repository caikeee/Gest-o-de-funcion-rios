from datetime import datetime 
from decimal import Decimal
from collections import defaultdict
from decimal import Decimal
from operator import attrgetter


class Pessoa:
  def __init__(self, nome , data_nascimento):
    self.nome = nome
    self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y") 
 
  def __str__(self):
        return f'{self.nome} ({self.data_nascimento.strftime("%d/%m/%Y")})'
  


class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, salario, funcao):
        super().__init__(nome, data_nascimento)
        self.salario = Decimal(salario)
        self.funcao = funcao
        
    def __str__(self):
        salario_formatado = f'{self.salario:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")
        return f'{self.nome}, {self.data_nascimento.strftime("%d/%m/%Y")}, {self.funcao}, {salario_formatado}'
    



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

# 3.2 – Remover o funcionário “João” da lista.
funcionarios = [f for f in funcionarios if f.nome != "João"]

# 3.3 – Imprimir todos os funcionários com todas suas informações.
print("Funcionários:")
for f in funcionarios:
    print(f)

# 3.4 – Aumentar salário em 10%
for f in funcionarios:
    f.salario *= Decimal("1.10")

# 3.5 – Agrupar por função
funcionarios_por_funcao = defaultdict(list)
for f in funcionarios:
    funcionarios_por_funcao[f.funcao].append(f)

# 3.6 – Imprimir agrupados por função
print("\nFuncionários agrupados por função:")
for funcao, funcs in funcionarios_por_funcao.items():
    print(funcao + ":")
    for f in funcs:
        print("  " + f.nome)

# 3.8 – Imprimir funcionários que fazem aniversário no mês 10 e 12
print("\nFuncionários que fazem aniversário em outubro e dezembro:")
for f in funcionarios:
    if f.data_nascimento.month in [10, 12]:
        print(f.nome)

# 3.9 – Imprimir o funcionário com a maior idade
mais_velho = min(funcionarios, key=attrgetter('data_nascimento'))
idade_mais_velho = (datetime.now() - mais_velho.data_nascimento).days // 365
print(f"\nFuncionário com a maior idade: {mais_velho.nome}, {idade_mais_velho} anos")

# 3.10 – Imprimir a lista de funcionários por ordem alfabética
print("\nFuncionários em ordem alfabética:")
for f in sorted(funcionarios, key=attrgetter('nome')):
    print(f.nome)

# 3.11 – Imprimir o total dos salários dos funcionários
total_salarios = sum(f.salario for f in funcionarios)
print("\nTotal dos salários: " + f'{total_salarios:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))

# 3.12 – Imprimir quantos salários mínimos ganha cada funcionário
salario_minimo = Decimal("1212.00")
print("\nSalários em múltiplos do salário mínimo:")
for f in funcionarios:
    multiplos_salario_minimo = f.salario / salario_minimo
    print(f"{f.nome}: {multiplos_salario_minimo:.2f}")