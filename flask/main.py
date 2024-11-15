from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)

# Load the dataset and train the model
def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, 'iris_model.pkl')
    return model

# Train the model
model = train_model()

@app.route('/', methods=['GET', 'POST'])
def main():
    prediction = None
    if request.method == 'POST':
        # Retrieve form data and convert to float
        try:
            sepal_length = float(request.form['sepal_length_cm'])
            sepal_width = float(request.form['sepal_width_cm'])
            petal_length = float(request.form['petal_length_cm'])
            petal_width = float(request.form['petal_width_cm'])
            
            # Make a prediction
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])#[0]
        except ValueError:
            prediction = "Invalid input. Please enter valid numbers."
    
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)