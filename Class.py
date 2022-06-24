class Pessoa: 
    def __init__(self, Nome, Peso, AnoNascimento):
        self.Nome = Nome
        self.Peso = Peso
        self.AnoNascimento = AnoNascimento

    def alteraPeso(self, NovoPeso):
        self.Peso= NovoPeso
  
    def getPeso(self):
        return self.Peso
    def getNome(self):
        return self.Nome
    def getAnoNascimento(self):
        return self.AnoNascimento

Pedro = Pessoa('Pedro', 90, 1990)
print(Pedro.getNome(), 'tem', Pedro.getPeso(), 'kg e nasceu em', Pedro.getAnoNascimento(), '!')