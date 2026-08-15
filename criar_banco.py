import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # Ativa suporte a Chaves Estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Tabela 1: Ponto de Acolhimento / Abrigo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS abrigo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            responsavel TEXT,
            telefone TEXT
        )
    ''')
    
    # Tabela 2: Doações (Roupas, Brinquedos, Alimentos)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            categoria TEXT NOT NULL,
            detalhes TEXT,
            quantidade INTEGER NOT NULL,
            status TEXT NOT NULL,
            abrigo_id INTEGER NOT NULL,
            FOREIGN KEY (abrigo_id) REFERENCES abrigo (id) ON DELETE CASCADE
        )
    ''')
    
    # Insere dados de teste se o banco estiver vazio
    cursor.execute("SELECT COUNT(*) FROM abrigo")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO abrigo (nome, cidade, responsavel, telefone) VALUES (?, ?, ?, ?)",
                       ('Abrigo Esperança', 'Belo Horizonte', 'Maria Silva', '(31) 98888-7777'))
        
        abrigo_id = cursor.lastrowid
        
        cursor.execute('''
            INSERT INTO doacao (item, categoria, detalhes, quantidade, status, abrigo_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Cesta Básica 10kg', 'Alimento', 'Validade para 6 meses', 5, 'Pendente', abrigo_id))
        
        cursor.execute('''
            INSERT INTO doacao (item, categoria, detalhes, quantidade, status, abrigo_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Casaco de Frio Infantil', 'Roupa', 'Tamanho 8 - Em bom estado', 2, 'Recebido', abrigo_id))

    conn.commit()
    conn.close()
    print("✅ Banco de dados 'banco.db' e tabelas criados com sucesso!")

if __name__ == '__main__':
    inicializar_banco()