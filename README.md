# 🚀 Automatisation Réseaux Sociaux (Gratuit)

Ce projet permet de poster automatiquement sur **Twitter**, **Facebook** et **Google Business Profile** via GitHub Actions.

## 📁 Installation

1. Créez un nouveau dépôt sur GitHub (ex: `mon-bot-social`).
2. Copiez les fichiers de ce dossier dans votre dépôt.
3. Allez dans **Settings** > **Secrets and variables** > **Actions**.
4. Ajoutez les secrets suivants :

### 🐦 Twitter (X)
*   `TWITTER_API_KEY`
*   `TWITTER_API_SECRET`
*   `TWITTER_ACCESS_TOKEN`
*   `TWITTER_ACCESS_SECRET`
*(Obtenez-les sur [developer.x.com](https://developer.x.com))*

### 📘 Facebook
*   `FB_PAGE_ID` : L'ID de votre page Facebook.
*   `FB_PAGE_ACCESS_TOKEN` : Un jeton d'accès permanent pour la page.
*(Obtenez-les sur [developers.facebook.com](https://developers.facebook.com))*

### 🏢 Google Business Profile
*   `GOOGLE_LOCATION_ID` : L'ID de votre établissement.
*   `GOOGLE_ACCESS_TOKEN` : Jeton OAuth2.
*(Obtenez-les via [Google Cloud Console](https://console.cloud.google.com))*

## ⚙️ Fonctionnement
*   Le script se lance automatiquement tous les jours à **9h00**.
*   Vous pouvez le lancer manuellement dans l'onglet **Actions** de GitHub en cliquant sur "Run workflow".
