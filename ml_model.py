from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from ml_data import generate_training_data

def train_fault_classifier():
    df = generate_training_data()
    X = df[["delay", "jitter", "packet_loss"]]
    y = df["fault_type"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Model Evaluation:")
    print(classification_report(y_test, model.predict(X_test)))

    return model