import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Récupération des identifiants depuis les variables d'environnement
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# On demande l'accès à Google Business
SCOPES = ['https://www.googleapis.com/auth/business.manage']

def get_token():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("❌ GOOGLE_CLIENT_ID et GOOGLE_CLIENT_SECRET doivent être définis.")
        return
    
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        SCOPES
    )
    
    print("Ouverture du navigateur pour l'autorisation...")
    credentials = flow.run_local_server(port=0)
    
    print("\n✅ AUTHENTIFICATION REUSSIE !")
    print(f"Votre REFRESH_TOKEN est : {credentials.refresh_token}")
    print("\nCopiez ce jeton et gardez-le pour GitHub !")

if __name__ == "__main__":
    get_token()
