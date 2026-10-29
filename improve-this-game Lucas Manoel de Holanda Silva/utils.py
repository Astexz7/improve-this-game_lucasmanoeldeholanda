"""Funções auxiliares: histórico de ações e formatação de texto."""
 
# Lista global que guarda tudo o que acontece no jogo (requisito 7)
historico = []
 
 
def registrar_acao(texto):
    """Guarda um evento no histórico do jogo."""
    historico.append(texto)
 
 
def mostrar_historico():
    """Mostra todos os eventos registrados, numerados."""
    titulo("HISTÓRICO DE AÇÕES")
    if not historico:
        print("Nenhuma ação registrada.")
    for numero, evento in enumerate(historico, start=1):
        print(f"{numero:>3}. {evento}")
 
 
def linha(caractere="=", tamanho=50):
    print(caractere * tamanho)
 
 
def titulo(texto):
    """Imprime um título centralizado entre linhas."""
    print()
    linha()
    print(texto.center(50))
    linha()
 
 
def barra_vida(vida, vida_maxima, tamanho=20):
    """Devolve uma barra de vida em texto. Ex: [##########----------] 50/100"""
    cheio = int(tamanho * vida / vida_maxima) if vida_maxima > 0 else 0
    return f"[{'#' * cheio}{'-' * (tamanho - cheio)}] {vida}/{vida_maxima}"
 
 
def escolher_opcao(mensagem, opcoes_validas):
    """Pergunta ao jogador até ele digitar uma opção válida."""
    while True:
        resposta = input(mensagem).strip()
        if resposta in opcoes_validas:
            return resposta
        print("Opção inválida, tente de novo.")
 
 
def pausa():
    input("\n(pressione ENTER para continuar)")