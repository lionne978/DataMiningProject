from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from reco import recommend_products

# Charger les règles
with open('rules.pkl', 'rb') as f:
    rules = pickle.load(f)

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'  # Nécessaire pour utiliser les sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'recommandations' not in session:
        session['recommandations'] = []

    if request.method == 'POST':
        panier = request.form['panier']
        produits = set([x.strip().lower() for x in panier.split(',')])
        session['recommandations'] = recommend_products(rules, produits)
        session.modified = True  # Indique que la session a été modifiée

    recommandations = session['recommandations']
    return render_template('index.html', recommandations=recommandations)

@app.route('/Effacer', methods=['POST'])
def Effacer():
    produit_a_supprimer = request.form['produit']
    recommandations = session.get('recommandations', [])
    
    if produit_a_supprimer in recommandations:
        recommandations.remove(produit_a_supprimer)
        session['recommandations'] = recommandations
        session.modified = True  # Indique que la session a été modifiée

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)