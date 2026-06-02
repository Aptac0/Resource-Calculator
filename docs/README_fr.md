# RSS STORE APTAC - Calculatrice de Ressources

**[Español](README_es.md) | [English](README_en.md) | [Português](README_pt.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | Français**

---

## 📱 Qu'est-ce que RSS STORE APTAC?

Application de bureau pour extraire automatiquement les ressources du royaume à partir de captures d'écran à l'aide de la technologie OCR avec gestion intelligente des comptes.

## ✨ Caractéristiques

- ✅ Extraction automatique des ressources avec OCR
- 🎯 Interface multilingue (6 langues prises en charge)
- 🔄 Mises à jour automatiques depuis GitHub
- 📊 Traitement par lots (jusqu'à 100 images)
- 💾 Export vers fichiers TXT/CSV
- 🌍 Tous les messages respectent votre langue sélectionnée

## 🚀 Installation Rapide

1. Téléchargez `RSS_STORE_APTAC_Installer.exe` depuis [Releases](https://github.com/Aptac0/Resource-Calculator/releases)
2. Exécutez le programme d'installation
3. Terminé! L'application se mettra à jour automatiquement lorsque de nouvelles versions seront disponibles

## 📖 Guide Utilisateur

### Processus Rapide

1. **Ouvrir l'application:** Exécutez `RSS STORE APTAC.exe`
2. **Ajouter des images:** Cliquez sur "Ajouter des Images" et sélectionnez vos captures d'écran
3. **Sélectionner un royaume:** Choisissez le royaume approprié dans le menu déroulant
4. **Configurer les nombres:**
   - `Numéro de début`: Premier numéro de compte (ex: 1)
   - `Numéro de fin`: Dernier numéro de compte (ex: 30)
   - `Numéros bloqués`: (facultatif) Numéros à ignorer (ex: 3,5,7)
5. **Définir les niveaux:** Sélectionnez "Niveau Ville" et "Niveau Entrepôt" (1-25)
6. **Traiter:** Cliquez sur le bouton de ressource dont vous avez besoin

### Comment Prendre des Captures d'Écran

#### À partir du PC (Recommandé)
- Ouvrez le jeu en mode fenêtré
- Prenez une capture d'écran claire de la fenêtre Ressources
- Assurez-vous que les chiffres et les étiquettes sont lisibles

![Capture du PC](../Ejemplos/Foto-desde-PC.png)

#### À partir du Mobile
- Transférez l'image vers le PC (USB, Google Drive, etc.)
- Évitez les photos inclinées ou floues
- Assurez-vous que l'image est nette et claire

![Capture du Mobile](../Ejemplos/Foto-desde-Movil.png)

### Formats de Saisie

#### Numéros de Début et de Fin
- Chiffres uniquement (ex: `1` et `30`)
- Doivent être des entiers positifs valides

#### Numéros Bloqués (Facultatif)
Deux formats disponibles:
- **Plage:** `1-10` (tous les nombres de 1 à 10)
- **Liste:** `1,3,5,7` (nombres spécifiques)
- **Mixte:** `1-5,8,10-15`

**Exemples:**
- `début=1`, `fin=10`, `bloqués=3,5` → traite: 1,2,4,6,7,8,9,10
- L'application valide que vous avez suffisamment d'images

#### Niveaux
- `Niveau Ville` (Marché): 1-25
- `Niveau Entrepôt` (Stockage): 1-25

![Niveaux du Marché](../Ejemplos/Niveles-Puesto-de-Venta.png)
![Niveaux de l'Entrepôt](../Ejemplos/Niveles-de-Almacen.png)

## 🔄 Système de Mise à Jour

### Automatique
L'application vérifie les nouvelles versions au démarrage. Si trouvé:
- Vous recevrez une notification
- Téléchargez directement depuis l'application
- Installation automatique

### Manuel
Exécutez `actualizar.bat` depuis le dossier d'installation

## 🆘 Dépannage

### "Impossible de détecter 4 valeurs"
- Assurez-vous que la capture d'écran est claire et lisible
- Les chiffres doivent être visibles
- Essayez de prendre une autre capture d'écran plus claire

### "Erreur de mise à jour"
- Vérifiez votre connexion Internet
- Réessayez dans quelques minutes
- Si le problème persiste, redémarrez l'application

### Les images ne sont pas traitées
- Vérifiez que vous avez sélectionné un royaume
- Vérifiez que les nombres sont valides
- Assurez-vous que vous avez suffisamment d'images

## 📞 Support

- **GitHub:** https://github.com/Aptac0/Resource-Calculator
- **Issues:** https://github.com/Aptac0/Resource-Calculator/issues
- **Releases:** https://github.com/Aptac0/Resource-Calculator/releases

## 📝 Configuration Requise

- Windows 10 ou version ultérieure
- Pas besoin d'installer Python
- Connexion Internet (pour les mises à jour)
- Tesseract OCR (inclus dans le programme d'installation)

## 🔐 Confidentialité

L'application:
- ✅ Fonctionne complètement hors ligne
- ✅ N'envoie jamais vos images à aucun serveur
- ✅ Aucune inscription ou compte requis
- ✅ Vos données restent sur votre ordinateur

---

**Version:** 1.0.0  
**Dernière mise à jour:** Juin 2026  
**Licence:** GPL-3.0
