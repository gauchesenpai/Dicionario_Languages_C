# Constituido por: Gauchesenpai
print ('Dicionário só suporta o idioma inglês por enquanto, criado by: t.me/Gauchesenpai')
print ('Para mais projetos como este, não deixe de me seguir: https://github.com/gauchesenpai')

import sqlite3

# Função para buscar significado de uma palavra
def search_word(conn, word):
    cursor = conn.cursor()
    cursor.execute('SELECT meaning FROM dictionary WHERE word=?', (word,))
    result = cursor.fetchone()
    return result[0] if result else None

# Função para obter lista de palavras associadas a uma letra
def get_words_by_letter(conn, letter):
    cursor = conn.cursor()
    cursor.execute('SELECT word FROM dictionary WHERE word LIKE ?', (letter+'%',))
    results = cursor.fetchall()
    return [result[0] for result in results]

# Conectar ao banco de dados
conn = sqlite3.connect('SQLite_Languages_C.db')

#Caso der erro na conexão do banco de dados
try:
    conn = sqlite3.connect('SQLite_Languages_C.db')
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")


# Menu interativo
while True:
    print("\nMenu:")
    print("1. Buscar significado de uma palavra")
    print("2. Obter lista de palavras associadas a uma letra")
    print("3. Sair")

    choice = input("Escolha uma opção (1/2/3): ")

    if choice == '1':
        word = input("Digite a palavra que deseja consultar: ")
        meaning = search_word(conn, word)
        if meaning:
            print(f"O significado de '{word}' é: {meaning}")
        else:
            print(f"A palavra '{word}' não foi encontrada no dicionário.")
    elif choice == '2':
        letter = input("Digite a letra que deseja consultar: ")
        words = get_words_by_letter(conn, letter)
        if words:
            print(f"Palavras associadas à letra {letter.upper()}:")
            print(", ".join(words))
        else:
            print(f"Nenhuma palavra encontrada para a letra {letter.upper()}.")
    elif choice == '3':
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Fechar a conexão
conn.close()
