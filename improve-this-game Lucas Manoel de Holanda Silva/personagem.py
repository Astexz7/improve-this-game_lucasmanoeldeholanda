from utils import registrar_acao, barra_vida
 
 
class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
 
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        # Dicionário de habilidades: nome -> bônus de dano
        self.habilidades = {}
 
    def esta_vivo(self):
        """Devolve True se o personagem ainda tem vida."""
        return self.vida > 0
 
    def upgrade_vida(self, incremento=10):
        """Cura o personagem, sem passar da vida máxima."""
        antes = self.vida
        self.vida = min(self.vida + incremento, self.vida_maxima)
        curado = self.vida - antes
        msg = f"{self.nome} recuperou {curado} de vida. ({self.vida}/{self.vida_maxima})"
        print(msg)
        registrar_acao(msg)
 
    def dano_vida(self, dano):
        """Reduz a vida do personagem, sem deixar ficar negativa."""
        self.vida = max(self.vida - dano, 0)
 
    def calcular_dano(self, alvo, bonus=0):
        """Dano = ataque (+ bônus) - defesa do alvo, com mínimo de 1."""
        dano = self.ataque + bonus - alvo.defesa
        if dano < 1:
            dano = 1
        return dano
 
    def atacar(self, alvo):
        """Ataque básico contra outro personagem."""
        dano = self.calcular_dano(alvo)
        alvo.dano_vida(dano)
        msg = f"{self.nome} atacou {alvo.nome} e causou {dano} de dano."
        print(msg)
        registrar_acao(msg)
 
    def usar_habilidade(self, nome_habilidade, alvo):
        """Usa uma habilidade do dicionário: causa dano extra."""
        if nome_habilidade not in self.habilidades:
            print(f"{self.nome} não conhece '{nome_habilidade}'.")
            return
        bonus = self.habilidades[nome_habilidade]
        dano = self.calcular_dano(alvo, bonus)
        alvo.dano_vida(dano)
        msg = (f"{self.nome} usou {nome_habilidade} em {alvo.nome} "
               f"e causou {dano} de dano!")
        print(msg)
        registrar_acao(msg)
 
    def dialogar(self, fala):
        """Faz o personagem falar uma frase."""
        msg = f'{self.nome} diz: "{fala}"'
        print(msg)
        registrar_acao(msg)
 
    def update_nome(self, nome_editado):
        """Atualiza o nome do personagem."""
        self.nome = nome_editado
 
    def status(self):
        """Linha de status com barra de vida."""
        return f"{self.nome:<12} {barra_vida(self.vida, self.vida_maxima)}"
 
    def __str__(self):
        return (f"Personagem: {self.nome}, Vida: {self.vida}, "
                f"Ataque: {self.ataque}, Defesa: {self.defesa}")