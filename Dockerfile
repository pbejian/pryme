FROM python:3.8

# Installer les dépendances de l'application
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier les fichiers de l'application dans le conteneur
COPY app.py .
COPY include.py .

# Exécuter l'application
#CMD streamlit run app.py
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
