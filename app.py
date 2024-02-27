from flask import Flask, render_template
import plotly.express as px
import seaborn as sns

app = Flask(__name__)

# Carga el dataset 'iris'
df = sns.load_dataset('iris')

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para el primer plot: scatter plot de 'sepal_length' vs 'sepal_width'
@app.route('/plot1')
def plot1():
    fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
    plot_div = fig.to_html(full_html=False)
    return render_template('plot.html', plot_div=plot_div)

# Ruta para el segundo plot: scatter plot de 'petal_length' vs 'petal_width'
@app.route('/plot2')
def plot2():
    fig = px.scatter(df, x='petal_length', y='petal_width', color='species')
    plot_div = fig.to_html(full_html=False)
    return render_template('plot.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)
