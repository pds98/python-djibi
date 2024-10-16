from flask import Flask, request, render_template, redirect
import pandas as pd

app = Flask(__name__)

# Chemin du fichier Excel pour enregistrer les données
excel_file = 'feedback.xlsx'

# Créer le fichier Excel s'il n'existe pas encore
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Email/Numéro de téléphone', 'Satisfaction', 'Commentaire'])
    df.to_excel(excel_file, index=False)

# Page d'accueil pour l'inscription
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        contact = request.form['contact']
        return redirect(f'/feedback?contact={contact}')
    return render_template('home.html')

# Page pour le feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    contact = request.args.get('contact')
    if request.method == 'POST':
        satisfaction = request.form['satisfaction']
        commentaire = request.form['commentaire']
        
        # Enregistrer les données dans le fichier Excel
        df = pd.read_excel(excel_file)
        new_entry = {'Email/Numéro de téléphone': contact, 'Satisfaction': satisfaction, 'Commentaire': commentaire}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_excel(excel_file, index=False)
        
        return 'Merci pour votre feedback!'
    
    return render_template('feedback.html', contact=contact)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        contact = request.form['contact']
        return redirect(f'/feedback?contact={contact}')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)
