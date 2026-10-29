from heroi import Heroi
from vilao import Vilao
from utils import (titulo, linha, escolher_opcao, pausa,
                   registrar_acao, mostrar_historico)
 
# Dicionários com os dados de cada personagem
DADOS_HEROIS = [
    {"nome": "Thorfinn", "vida": 100, "ataque": 25, "defesa": 10,
     "raca": "humano", "arma": "duas adagas",
     "habilidades": {"Golpe Duplo": 12},
     "fala": "Eu vou te derrotar!"},
    {"nome": "Kirito", "vida": 100, "ataque": 20, "defesa": 15,
     "raca": "humano", "arma": "duas espadas",
     "habilidades": {"Starburst Stream": 15},
     "fala": "Não vou recuar!"},
]
 
DADOS_VILOES = [
    {"nome": "Gui Ogata", "vida": 120, "ataque": 20, "defesa": 10,
     "mutacao": "demônio",
     "habilidades": {"Garra Sombria": 10},
     "fala": "Ninguém escapa de mim!"},
    {"nome": "Shadow", "vida": 150, "ataque": 30, "defesa": 8,
     "mutacao": "radiação atômica",
     "habilidades": {"Chaos Control": 20},
     "fala": "Você não é páreo pra mim."},
]
 
 
def criar_herois():
    herois = []
    for d in DADOS_HEROIS:
        h = Heroi(d["nome"], d["vida"], d["ataque"], d["defesa"],
                  d["raca"], d["arma"])
        h.habilidades = dict(d["habilidades"])
        h.fala = d["fala"]
        herois.append(h)
    return herois
 
 
def criar_viloes():
    viloes = []
    for d in DADOS_VILOES:
        v = Vilao(d["nome"], d["vida"], d["ataque"], d["defesa"], d["mutacao"])
        v.habilidades = dict(d["habilidades"])
        v.fala = d["fala"]
        viloes.append(v)
    return viloes
 
 
def escolher_personagem(lista, mensagem):
    """Mostra uma lista numerada e devolve o personagem escolhido."""
    for i, p in enumerate(lista, start=1):
        print(f"  {i}. {p}")
    opcoes = [str(i) for i in range(1, len(lista) + 1)]
    escolha = escolher_opcao(mensagem, opcoes)
    return lista[int(escolha) - 1]
 
 
def turno_heroi(heroi, vilao):
    """Mostra o menu e executa a ação escolhida. Devolve True se o turno foi gasto."""
    print("\nO que fazer?")
    print("  1. Atacar")
    print("  2. Usar habilidade")
    print("  3. Usar poção")
    print("  4. Salvar refém")
    escolha = escolher_opcao("> ", ["1", "2", "3", "4"])
 
    if escolha == "1":
        heroi.atacar(vilao)
    elif escolha == "2":
        nomes = list(heroi.habilidades)
        for i, n in enumerate(nomes, start=1):
            print(f"  {i}. {n} (+{heroi.habilidades[n]} de dano)")
        opcoes = [str(i) for i in range(1, len(nomes) + 1)]
        e = escolher_opcao("Habilidade: ", opcoes)
        heroi.usar_habilidade(nomes[int(e) - 1], vilao)
    elif escolha == "3":
        return heroi.usar_pocao()
    elif escolha == "4":
        heroi.salvar_refem()
    return True
 
 
def batalha(heroi, vilao):
    titulo(f"BATALHA: {heroi.nome} VS {vilao.nome}")
    registrar_acao(f"Início da batalha: {heroi.nome} vs {vilao.nome}.")
    heroi.dialogar(heroi.fala)
    vilao.dialogar(vilao.fala)
 
    rodada = 1
    while heroi.esta_vivo() and vilao.esta_vivo():
        print(f"\n--- Rodada {rodada} ---")
        print(heroi.status())
        print(vilao.status())
 
        # Turno do jogador (repete se a ação não foi possível)
        gasto = False
        while not gasto:
            gasto = turno_heroi(heroi, vilao)
 
        # Turno do vilão (só se ainda estiver vivo)
        if vilao.esta_vivo():
            print()
            vilao.agir(heroi)
 
        rodada += 1
 
    print()
    if heroi.esta_vivo():
        vilao.dialogar("Impossível... eu perdi...")
        msg = f"{heroi.nome} venceu a batalha!"
    else:
        heroi.dialogar("Eu... não consegui...")
        msg = f"{vilao.nome} venceu a batalha!"
    print(msg)
    registrar_acao(msg)
    return heroi.esta_vivo()
 
 
def main():
    herois = criar_herois()
    viloes = criar_viloes()
 
    titulo("IMPROVE THIS GAME")
    print("Escolha seu herói:")
    heroi = escolher_personagem(herois, "Herói: ")
    registrar_acao(f"O jogador escolheu {heroi.nome}.")
 
    # Laço principal: enfrenta os vilões em sequência
    for vilao in viloes:
        pausa()
        if not batalha(heroi, vilao):
            break
        if vilao is not viloes[-1]:
            print(f"\n{heroi.nome} descansa um pouco antes do próximo inimigo.")
            heroi.upgrade_vida(20)
 
    titulo("FIM DE JOGO")
    if heroi.esta_vivo():
        print(f"{heroi.nome} derrotou todos os vilões! Vitória!")
    else:
        print(f"{heroi.nome} foi derrotado. Fim de jogo.")
 
    if escolher_opcao("\nVer histórico de ações? (s/n): ", ["s", "n"]) == "s":
        mostrar_historico()
 
 
if __name__ == "__main__":
    main()