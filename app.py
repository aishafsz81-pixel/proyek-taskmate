from flask import Flask, render_template, request, redirect, url_to

app = Flask(__name__)

# Tempat menyimpan tugas sementara
daftar_tugas = []

@app.route('/')
def index():
    return render_template('index.html', tugas=daftar_tugas)

@app.route('/tambah', methods=['POST'])
def tambah_tugas():
    tugas_baru = request.form.get('tugas')
    if tugas_baru:
        daftar_tugas.append(tugas_baru)
    return redirect('/')

@app.route('/hapus/<int:index_tugas>')
def hapus_tugas(index_tugas):
    if 0 <= index_tugas < len(daftar_tugas):
        daftar_tugas.pop(index_tugas)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)