import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave_secreta_aconchego_social"

def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row #Acesso as colunas pelo nome
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

#1----Página inicial----
@app.route('/')
def index():
    return render_template('index.html')

#2----Página de Consulta e Listagem com Busca----
@app.route('/doacoes')
def consultar():
    busca = request.args.get('busca', '').strip()
    conn = get_db_connection()

    if busca:
        query = '''
            SELECT doacao.id, abrigo.nome AS abrigo_nome
            FROM doacao
            JOIN abrigo ON doacao.abrigo_id = abrigo.id
            WHERE doacao.item LIKE ? OR doacao.categoria LIKE ? OR abrigo.nome LIKE ?
        '''
        termo =  f'%{busca}%'
        doacoes = conn.execute(query, (termo, termo, termo)).fetchall()

    else:
        query = '''
            SELECT doacao.*, abrigo.nome AS abrigo_nome
            FROM doacao
            JOIN abrigo ON doacao.abrigo_id = abrigo.id
        '''
        doacoes = conn.execute(query).fetchall()

    conn.close()
    return render_template('consultar.html', doacoes=doacoes, busca=busca)

#3----Página de Cadastro de Doações----
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    conn = get_db_connection()

    if request.method == 'POST':
        item = request.form.get('item', '').strip()
        categoria = request.form.get('categoria', '').strip()
        detalhes = request.form.get('detalhes', '').strip()
        quantidade = request.form.get('quantidade', '').strip()
        status = request.form.get('status', '').strip()
        abrigo_id = request.form.get('abrigo_id', '').strip()

        # Validação dos campos obrigatórios
        if not item or not categoria or not quantidade or not status or not abrigo_id:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            abrigos = conn.execute('SELECT * FROM abrigo').fetchall()
            conn.close()
            return render_template('cadastrar.html', abrigos=abrigos)

        conn.execute(''' 
            INSERT INTO doacao (item, categoria, detalhes, quantidade, status, abrigo_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (item, categoria, detalhes, int(quantidade), status, int(abrigo_id)))
        conn.commit()
        conn.close()
        flash('Doação cadastrada com sucesso!', 'success')
        return redirect(url_for('consultar'))

    abrigos = conn.execute('SELECT * FROM abrigo').fetchall()
    conn.close()
    return render_template('cadastrar.html', abrigos=abrigos)

#4----Página de Edição de Doações----
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    doacao = conn.execute('SELECT * FROM doacao WHERE id = ?', (id,)).fetchone()

    if not doacao:
        conn.close()
        flash('Doação não encontrada.', 'error')
        return redirect(url_for('consultar'))

    if request.method == 'POST':
        item = request.form.get('item', '').strip()
        categoria = request.form.get('categoria', '').strip()
        detalhes = request.form.get('detalhes', '').strip()
        quantidade = request.form.get('quantidade', '').strip()
        status = request.form.get('status', '').strip()
        abrigo_id = request.form.get('abrigo_id', '').strip()

        # Validação dos campos obrigatórios
        if not item or not categoria or not quantidade or not status or not abrigo_id:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            abrigos = conn.execute('SELECT * FROM abrigo').fetchall()
            conn.close()
            return render_template('editar.html', doacao=doacao, abrigos=abrigos)

        conn.execute('''
            UPDATE doacao
            SET item = ?, categoria = ?, detalhes = ?, quantidade = ?, status = ?, abrigo_id = ?
            WHERE id = ?
        ''', (item, categoria, detalhes, int(quantidade), status, int(abrigo_id), id))
        conn.commit()
        conn.close()
        flash('Doação atualizada com sucesso!', 'success')
        return redirect(url_for('consultar'))

    abrigos = conn.execute('SELECT * FROM abrigo').fetchall()
    conn.close()
    return render_template('editar.html', doacao=doacao, abrigos=abrigos)

#5----Página de Exclusão de Doações----
@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM doacao WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Doação excluída com sucesso!', 'success')
    return redirect(url_for('consultar'))

if __name__ == '__main__':
    app.run(debug=True)

    '''
    :) <--> (:
    '''