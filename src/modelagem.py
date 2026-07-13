from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def criar_modelo_logistico():
    return LogisticRegression()


def criar_modelo_random_forest():
    return RandomForestClassifier(random_state=42)