from flask import Flask,render_template,request
import recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend',methods=['post'])
def predict():
    title = request.form.get('title')
    if title not in recommendation.final_rating['title'].unique():
        response = -1
    else:
        response = recommendation.recommend(title)

    return render_template('index.html',response=response)
if __name__ == '__main__':
    app.run(debug=True)
