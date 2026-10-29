from personagem import Personagem
from utils import registrar_acao
 
 
class Heroi(Personagem):
    """Herói: tem raça, arma, poções e pode salvar reféns."""
 
    def __init__(self, nome, vida, ataque, defesa, raca, arma, pocoes=2):
        super().__init__(nome, vida, ataque, defesa)
        self.raca = raca
        self.arma = arma
        self.pocoes = pocoes
        self.refens_salvos = 0
 
    def usar_pocao(self):
        """Usa uma poção para recuperar 30 de vida."""
        if self.pocoes <= 0:
            print(f"{self.nome} não tem mais poções!")
            return False
        self.pocoes -= 1
        print(f"{self.nome} bebeu uma poção. (restam {self.pocoes})")
        registrar_acao(f"{self.nome} usou uma poção.")
        self.upgrade_vida(30)
        return True
 
    def salvar_refem(self):
        """Salva um refém e ganha um pequeno bônus de ataque."""
        self.refens_salvos += 1
        self.ataque += 2
        msg = (f"{self.nome} salvou um refém! (total: {self.refens_salvos}) "
               f"Ataque aumentou para {self.ataque}.")
        print(msg)
        registrar_acao(msg)
 
    def __str__(self):
        return (f"Herói: {self.nome} ({self.raca}), Vida: {self.vida}, "
                f"Ataque: {self.ataque}, Defesa: {self.defesa}, "
                f"Arma: {self.arma}, Poções: {self.pocoes}")