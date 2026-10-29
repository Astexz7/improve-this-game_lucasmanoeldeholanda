import random
 
from personagem import Personagem
 
 
class Vilao(Personagem):
    """Vilão: tem uma mutação e escolhe sozinho como agir."""
 
    def __init__(self, nome, vida, ataque, defesa, mutacao):
        super().__init__(nome, vida, ataque, defesa)
        self.mutacao = mutacao
 
    def agir(self, alvo):
        """Decide a ação do turno: 30% de chance de usar habilidade."""
        if self.habilidades and random.random() < 0.3:
            nome_habilidade = random.choice(list(self.habilidades))
            self.usar_habilidade(nome_habilidade, alvo)
        else:
            self.atacar(alvo)
 
    def __str__(self):
        return (f"Vilão: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, "
                f"Defesa: {self.defesa}, Mutação: {self.mutacao}")