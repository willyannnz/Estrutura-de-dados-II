class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __repr__(self):
        return f"{self.nome} (senha {self.senha}, prioridade {self.prioridade})"
