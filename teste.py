class Pessoa:
    def __init__(self, nome: str, idade: int, altura:float, peso:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def se_apresentar(self):
        print (f"Meu nome é {self.nome}, tenho {self.idade} anos de idade e minha altura é {self.altura} e peso {self.peso}")

    def calcular_imc (self):
        return self.peso / self.altura ** 2


pessoa = Pessoa("Raphael", 30, 1.80, 85)
pessoa.se_apresentar()
imc = pessoa.calcular_imc()
print(f"Meu IMC é {imc:.2f}")