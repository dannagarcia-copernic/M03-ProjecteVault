import os

# Configuració de Producció
MAX_RETRIES = 3

# Versió segura: llegeix el token de l'entorn, no està hardcoded
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
