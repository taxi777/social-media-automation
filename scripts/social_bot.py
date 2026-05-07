import os
import requests
import random
import tweepy

# --- CONFIGURATION COMMERCIALE ---
PHONE = "07 50 53 56 58"
SITE = "www.taximarnelavallee.com"

MESSAGES = [
    f"🚖 Besoin d'un Taxi à Marne-la-Vallée ? Disneyland (30€), CDG (100€), Orly (130€). Appelez-nous 24h/7j au {PHONE} ! #TaxiMLV #Disneyland",
    f"✈️ Transfert Aéroport serein ? Suivi de vol gratuit et chauffeur ponctuel. Réservez sur {SITE} ou au {PHONE}. #Taxi #CDG #Orly",
    f"🏰 Direction Disneyland Paris ? Profitez d'un trajet confortable en famille (sièges enfants offerts). Tél: {PHONE} #Disney #VTC",
    f"🏢 Professionnels : Un trajet business vers Paris ou les gares ? Confort et discrétion garantis. Infos: {SITE} #BusinessTaxi"
]

# --- RÉCUPÉRATION DES SECRETS (GITHUB) ---
TWITTER_KEYS = {
    'consumer_key': os.getenv("TWITTER_API_KEY"),
    'consumer_secret': os.getenv("TWITTER_API_SECRET"),
    'access_token': os.getenv("TWITTER_ACCESS_TOKEN"),
    'access_token_secret': os.getenv("TWITTER_ACCESS_SECRET")
}

FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")

GOOGLE_LOCATION_ID = os.getenv("GOOGLE_LOCATION_ID")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REFRESH_TOKEN = os.getenv("GOOGLE_REFRESH_TOKEN")

TIKTOK_KEYS = {
    'client_key': os.getenv("TIKTOK_CLIENT_KEY"),
    'client_secret': os.getenv("TIKTOK_CLIENT_SECRET")
}

def get_google_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "refresh_token": GOOGLE_REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    r = requests.post(url, data=data)
    return r.json().get("access_token")

def post_to_twitter(message):
    print("🐦 Tentative Twitter...")
    if not all(TWITTER_KEYS.values()):
        print("⚠️ Clés Twitter manquantes. Passage au suivant.")
        return
    try:
        client = tweepy.Client(**TWITTER_KEYS)
        client.create_tweet(text=message)
        print("✅ Twitter OK")
    except Exception as e: print(f"❌ Twitter: {e}")

def post_to_facebook(message):
    print("📘 Tentative Facebook...")
    url = f"https://graph.facebook.com/{FB_PAGE_ID}/feed"
    payload = {'message': message, 'access_token': FB_PAGE_ACCESS_TOKEN}
    try:
        r = requests.post(url, data=payload)
        if r.status_code == 200: print("✅ Facebook OK")
        else: print(f"❌ Facebook: {r.text}")
    except Exception as e: print(f"❌ Facebook: {e}")

def post_to_google(message):
    print("🏢 Tentative Google Business...")
    token = get_google_access_token()
    url = f"https://mybusinessbusinessinformation.googleapis.com/v1/{GOOGLE_LOCATION_ID}/localPosts"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "languageCode": "fr",
        "summary": message,
        "topicType": "STANDARD",
        "callToAction": {"actionType": "BOOK", "url": f"https://{SITE}"}
    }
    try:
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code == 200: print("✅ Google OK")
        else: print(f"❌ Google: {r.text}")
    except Exception as e: print(f"❌ Google: {e}")

def post_to_tiktok(message):
    # Note: TikTok nécessite une validation d'App pour l'API Content Posting
    print("🎵 TikTok: En attente de validation de l'App...")
    pass

if __name__ == "__main__":
    msg = random.choice(MESSAGES)
    print(f"🚀 Publication du message : {msg}")
    
    post_to_twitter(msg)
    post_to_facebook(msg)
    post_to_google(msg)
    post_to_tiktok(msg)
