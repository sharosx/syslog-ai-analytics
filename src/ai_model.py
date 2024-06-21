import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    data = pd.read_csv('data/processed/logs.csv')
    X = data['log']
    y = data['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model accuracy: {score}")

if __name__ == "__main__":
    train_model()
