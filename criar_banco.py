import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreing_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS abrigo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            responsavel TEXT,
            telefone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doacao(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            categoria TEXT NOT NULL, -- 'Brinquedo', 'Roupa', 'Alimento'
            detalhes TEXT, -- ex: 'Tamanho M', 'Validade 12/2026'
            quantidade INTEGER NOT NULL,
            status TEXT NOT NULL, -- 'Pendente', 'Recebido', 'Entregue'
            abrigo_id INTEGER NOT NULL,
            FOREING KEY (abrigo_id) REFERENCES abrigo (id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso :)")

if __name__ == '__main__':
    inicializar_banco()

    '''
    :) <--> (:
    '''