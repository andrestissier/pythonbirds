class Pessoa:
    olhos = 2 #atributo default ou atributo de classe, todos vão ter esse atributo
                #atributo de classe
    def __init__(self, *filhos, nome=None, idade=35): #atributo de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod    #decorator
    def metodo_estatico():  #independe do valor da definição
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): #cls referência a class
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' #atributo dinamicamente através de atribuição e removidos por del
    del luciano.filhos
    #removido apenas em luciano
    luciano.olhos = 1 #agora ele irá passar a fazer parte do dander dict do luciano e será um objeto diferente
    del luciano.olhos #apagando apenas do luciano e não da classe, irá receber o atributo de classe novamente
    #dander dict mostra todos os atributos
    print(luciano.__dict__) #dander dict apresenta apenas atributos de instância e não de classe geral
    print(renzo.__dict__)
    Pessoa.olhos = 3 #mudei o atributo da classe, mas o de luciano continua 1
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

