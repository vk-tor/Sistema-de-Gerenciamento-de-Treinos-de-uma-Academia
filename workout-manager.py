import json
import os

# Define o nome do arquivo de texto que armazenará os dados
NOME_ARQUIVO = "dados_academia.json"

def carregar_dados():
    """Carrega a lista de fichas do arquivo JSON."""
    # Se o arquivo não existir, retorna uma lista vazia
    if not os.path.exists(NOME_ARQUIVO):
        return []

    # Tenta ler o arquivo
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados
    except json.JSONDecodeError:
        # Se o arquivo estiver vazio ou corrompido, retorna lista vazia
        return []

def salvar_dados(fichas):
    """Salva a lista principal de fichas no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        # Usa indent=4 para o arquivo ficar legível
        json.dump(fchas, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Dados salvos com sucesso em {NOME_ARQUIVO}!")

def registrar_ficha(lista_principal_fichas):
    """Registra uma nova ficha de treino."""
    print("\n--- 📝 Cadastro de Nova Ficha ---")

    # Coleta os dados conforme solicitado
    nome = input("Nome do aluno: ").strip()
    objetivo = input("Objetivo (Ex: Hipertrofia, Emagrecimento): ").strip()
    data_inicio = input("Data de início (DD/MM/AAAA): ").strip()

    # Cria uma LISTA interna para os exercícios
    exercicios_lista = []
    print("\n--- Adicionar Exercícios ---")

    while True:
        nome_ex = input("Nome do exercício (ou digite 'fim' para parar): ").strip()
        if nome_ex.lower() == 'fim':
            break

        series_reps = input(f"Séries e repetições para {nome_ex} (Ex: 3x12): ")

        # REQUISITO: Usando TUPLA para armazenar o par (exercício, reps)
        exercicio_tupla = (nome_ex, series_reps)

        # Adiciona a tupla na lista de exercícios
        exercicios_lista.append(exercicio_tupla)
        print(f"Exercício '{nome_ex}' adicionado.")

    # Cria um dicionário para a nova ficha
    nova_ficha = {
        "nome": nome,
        "objetivo": objetivo,
        "data_inicio": data_inicio,
        "exercicios": exercicios_lista  # Esta é uma lista de tuplas
    }

    # REQUISITO: Adiciona a ficha (dicionário) à LISTA principal
    lista_principal_fichas.append(nova_ficha)
    print("\n✅ Ficha registrada com sucesso!")

def consultar_ficha(lista_principal_fichas):
    """Consulta fichas por nome do aluno."""
    print("\n--- 🔎 Consultar Ficha por Nome ---")
    if not lista_principal_fichas:
        print("Nenhuma ficha cadastrada para consultar.")
        return

    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().lower()
    encontrado = False

    # Itera pela LISTA principal
    for ficha in lista_principal_fichas:
        # Busca case-insensitive
        if ficha["nome"].lower() == nome_busca:
            print("\n--- Ficha Encontrada ---")
            print(f"Aluno: {ficha['nome']}")
            print(f"Objetivo: {ficha['objetivo']}")
            print(f"Data de Início: {ficha['data_inicio']}")
            print("Exercícios:")

            # Itera sobre a LISTA de TUPLAS
            for ex, reps in ficha["exercicios"]:
                print(f"  - {ex}: {reps}")

            print("-" * 23)
            encontrado = True

    if not encontrado:
        print(f"Nenhuma ficha encontrada para o aluno '{nome_busca}'.")

def listar_fichas(lista_principal_fichas):
    """Lista um resumo de todas as fichas cadastradas."""
    print("\n--- 📋 Lista de Todos os Treinos ---")
    if not lista_principal_fichas:
        print("Nenhum treino cadastrado no momento.")
        return

    # Itera pela LISTA principal e mostra um resumo
    for i, ficha in enumerate(lista_principal_fichas, start=1):
        print(f"\n--- Ficha {i} ---")
        print(f"Aluno: {ficha['nome']}")
        print(f"Objetivo: {ficha['objetivo']}")
        print(f"Nº de Exercícios: {len(ficha['exercicios'])}")

    print(f"\nTotal de {len(lista_principal_fichas)} fichas cadastradas.")

def mostrar_menu():
    """Exibe o menu principal e retorna a escolha do usuário."""
    print("\n" + "="*30)
    print("   💪 Academia Corpo em Movimento 💪")
    print("="*30)
    print("1. Registrar nova ficha de treino")
    print("2. Consultar ficha por aluno")
    print("3. Listar todos os treinos")
    print("4. Salvar e Sair")
    print("="*30)
    return input("Escolha uma opção (1-4): ")

# --- Função Principal (Main) ---
def main():
    # REQUISITO: Carrega os dados do arquivo ao iniciar
    fichas_de_treino = carregar_dados()
    print(f"Bem-vindo! {len(fichas_de_treino)} fichas carregadas do arquivo.")

    while True:
        escolha = mostrar_menu()

        if escolha == '1':
            registrar_ficha(fichas_de_treino)

        elif escolha == '2':
            consultar_ficha(fichas_de_treino)

        elif escolha == '3':
            listar_fichas(fichas_de_treino)

        elif escolha == '4':
            # REQUISITO: Salva os dados antes de sair
            salvar_dados(fichas_de_treino)
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("❌ Opção inválida! Por favor, escolha de 1 a 4.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
