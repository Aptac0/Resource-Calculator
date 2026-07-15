# RSS STORE APTAC - Calculatrice de Ressources

**[Español](README_es.md) | [English](README_en.md) | [Português](README_pt.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | Français**

Application de bureau pour extraire automatiquement les ressources du royaume à partir de captures d'écran à l'aide de l'OCR avec génération intelligente de surnoms.

---

## 📖 Table des Matières

1. [Guide Rapide](#-guide-rapide)
2. [Comment Prendre des Captures](#-comment-prendre-des-captures)
3. [Formats d'Entrée](#-formats-dentree)
4. [Boutons et Fonctions](#-boutons-et-fonctions)
5. [Résultats et Fichiers Enregistrés](#-resultats-et-fichiers-enregistres)
6. [Dépannage](#-depannage)
7. [Système de Mise à Jour](#-systeme-de-mise-a-jour)

---

## 🚀 Guide Rapide

### Étape par Étape

1. **Ouvrez l'application**
   - Exécutez `RSS STORE APTAC.exe`
   - Sélectionnez la langue dans le menu principal

2. **Ajoutez des images**
   - Cliquez sur le bouton `Ajouter des Images`
   - Sélectionnez vos captures d'écran
   - Les images se chargent dans la liste

3. **Configurez le royaume**
   - Choisissez le `Royaume` dans le menu déroulant
   - Les royaumes disponibles se mettent à jour depuis le serveur

4. **Remplissez les nombres**
   - `Numéro de début` : premier numéro de compte (ex : 1)
   - `Numéro de fin` : dernier numéro de compte (ex : 30)
   - `Numéros bloqués` (optionnel) : comptes à ignorer (ex : 3,5,7)

5. **Définissez les niveaux**
   - `Niveau de ville` : niveau du Marché (1–25)
   - `Niveau d'entrepôt` : niveau du Stockage (1–25)

6. **Traitez les ressources**
   - Cliquez sur le bouton de ressource dont vous avez besoin :
     - `Ressources Totales` : total par compte
     - `Ressources de Compte` : valeurs nettes
     - `Ressources de Sac à Dos` : inventaire uniquement

7. **Trouvez les résultats**
   - Enregistré automatiquement dans `GUARDADOS/`
   - Nom : `KINGDOM_results_YYYYMMDD_HHMMSS.txt`

## 📸 Comment Prendre des Captures

### Depuis le PC (Recommandé)

✅ **Bonne méthode :**
- Ouvrez le jeu en mode fenêtré
- Capturez clairement la fenêtre Ressources
- Assurez-vous que les chiffres ne sont pas coupés
- L'image doit être nette sans ombres

![Capture du PC](../../images/app/Foto-desde-PC.png)

**Conseils :**
- Utilisez l'outil de capture Windows (Win + Shift + S)
- Incluez uniquement le dialogue des ressources
- Les chiffres et les étiquettes doivent être lisibles

### Depuis Mobile

⚠️ **Important :**
1. Prenez la capture sur mobile
2. **Transférez sur PC** (USB, Google Drive, Telegram, etc.)
3. Évitez les photos inclinées ou floues
4. La capture doit être nette et claire

![Capture depuis Mobile](../../images/app/Foto-desde-Movil.png)

**Recommandations :**
- Utilisez la capture native du mobile (mieux qu'une photo)
- Bonne luminosité
- Pas de reflets ni d'ombres
- Transfert sans compression

## 🔢 Formats d'Entrée

### Numéro de Début et Numéro de Fin

- **Chiffres seulement** : `1` à `30` (ex : début=1, fin=30)
- **Doivent être des entiers positifs**
- **Le nombre d'images doit correspondre** aux comptes valides

### Numéros Bloqués (Optionnel)

**Deux formats autorisés :**

**Format 1 : Plage**
```
1-10      → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
3-5       → 3, 4, 5
```

**Format 2 : Liste**
```
1,3,5,7   → 1, 3, 5, 7
3, 5, 8   → 3, 5, 8 (espaces autorisés)
```

**Format 3 : Mixte**
```
1-5,8,10-15  → 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15
```

### Exemple Pratique

| Champ | Valeur | Résultat |
|-------|--------|----------|
| Début | 1 | Compte 1 |
| Fin | 10 | Compte 10 |
| Bloqués | 3,5 | Traite : 1,2,4,6,7,8,9,10 |
| Images | 8 | ✅ Valide (correspond)

⚠️ Si le nombre d'images ≠ comptes valides, vous verrez une erreur.

### Niveaux

- `Niveau de ville` (Marché) : 1-25
- `Niveau d'entrepôt` (Stockage) : 1-25



## 🎯 Boutons et Fonctions

### Ajouter des Images
- Ouvre le sélecteur de fichiers
- Sélectionnez plusieurs captures
- Ajoute à la liste de traitement

### Ajouter un Dossier
- Charge toutes les images valides d'un dossier
- Plus rapide pour les gros lots
- Recommandé pour traiter de nombreux comptes

### Supprimer une Image
- Retire une image sélectionnée de la liste
- Utile pour corriger une mauvaise capture sans tout vider
- Permet de valider le lot final avant traitement

### Vider la Liste
- Vide toutes les images chargées
- Supprime les données temporaires
- Utile pour commencer un nouveau lot

### Nouvelle Fenêtre
- Ouvre une autre instance de l'application
- Utile pour plusieurs tâches

### Mettre à Jour les Données
- Télécharge les derniers `kingdoms/` et `Iconos/` depuis la source de mise à jour
- Remplace les données locales
- Si vous utilisez le .exe, affiche la page des releases pour un nouvel installateur

### Ressources Totales
- Traite les images pour chaque compte
- Sauvegarde : Nourriture, Bois, Pierre, Or
- Affiche le total par compte
- Utile pour le suivi d'inventaire

### Ressources de Compte
- Calcule les ressources nettes (total - inventaire)
- Soustrait les éléments de sac à dos
- Montre les ressources réelles du compte
- Mieux pour la gestion des comptes

### Ressources de Sac à Dos
- Montre uniquement les éléments d'inventaire
- Extrait les valeurs "depuis objets"
- Utile pour l'analyse du sac à dos

## 💾 Résultats et Fichiers Enregistrés

### Emplacement des Fichiers

```
GUARDADOS/
├── KINGDOM_results_20260602_143022.txt
├── KINGDOM_results_20260602_145015.txt
└── KINGDOM_results_20260603_101530.txt
```

### Format du Fichier

```
Nickname: Account_1
Niveau de ville: 15
Niveau d'entrepôt: 18
Nourriture: 45.0K
Bois: 32.5K
Pierre: 28.7K
Or: 5.6K
---
Nickname: Account_2
Niveau de ville: 15
Niveau d'entrepôt: 18
Nourriture: 41.2K
Bois: 35.1K
Pierre: 26.8K
Or: 6.1K
---
```

### Comment Utiliser les Résultats

1. Ouvrez le fichier `.txt` dans un éditeur
2. Copiez les données dont vous avez besoin
3. Collez-les dans votre outil de gestion
4. Les surnoms sont générés automatiquement

---

## 🆘 Dépannage

### "Impossible de détecter 4 valeurs"
- Problème de qualité d'image : essayez une image plus claire
- Les chiffres doivent être lisibles
- Recadrez ou refaites la capture
- Ajustez la luminosité si les chiffres sont sombres

### "Erreur : X images sélectionnées mais Y comptes valides"
- Le nombre d'images ne correspond pas aux comptes valides
- Vérifiez les nombres de début/fin et les bloqués
- Utilisez la formule : (fin - début + 1) - bloqués = total nécessaire
- Ajoutez ou supprimez des images pour correspondre

### "Erreur de mise à jour"
- Vérifiez la connexion Internet
- Réessayez dans quelques minutes
- Redémarrez l'application si l'erreur persiste
- Vérifiez les paramètres du pare-feu

### Les images ne se traitent pas
- Vérifiez que le royaume est sélectionné
- Vérifiez que tous les champs numériques sont remplis
- Assurez-vous que le nombre d'images correspond aux comptes attendus
- Essayez de prévisualiser l'image pour vérifier la qualité OCR

### "Impossible d'ouvrir la fenêtre"
- Une autre instance peut être en cours d'exécution
- Fermez les fenêtres existantes et réessayez
- Essayez d'exécuter en tant qu'administrateur

---

## 🔄 Système de Mise à Jour

### Automatique
- L'application **vérifie les nouvelles versions au démarrage**
- Si une mise à jour est disponible, une notification apparaît
- Téléchargement automatique depuis le serveur configuré
- Installation sans intervention

### Manuel
- Exécutez `actualizar.bat` dans le dossier d'installation
- Il met à jour directement depuis la source configurée

### Ce qui se met à jour
- `kingdoms/` → nouveaux modèles
- `Iconos/` → nouvelles icônes
- .exe version → depuis les Releases

---

## 📋 Niveaux Disponibles

### Niveau de Ville (Marché)
- Plage : 1 à 25
- S'applique à toutes les ressources
- Enregistré dans les résultats



### Niveau d'Entrepôt (Stockage)
- Plage : 1 à 25
- Stockage disponible
- Enregistré dans les résultats



### Technologie Maximale
- Affecte la capacité des ressources
- Référence dans l'application



---

## 🎯 Exemple Complet

**Scénario :** Vous avez 5 comptes, vous voulez obtenir les ressources totales

1. **Préparez les captures**
   - Prenez 5 captures d'écran (une par compte)
   - Transférez au PC
   - Enregistrez dans un dossier accessible

2. **Configurez l'application**
   - Ajouter des Images → sélectionnez 5
   - Royaume → choisissez le bon
   - Numéro de début : 1
   - Numéro de fin : 5
   - Numéros bloqués : (vide)
   - Niveau de ville : 15
   - Niveau d'entrepôt : 18

3. **Traitez**
   - Cliquez sur `Ressources Totales`
   - Attendez la fin
   - Vous verrez la progression en %

4. **Résultats**
   - Fichier enregistré automatiquement
   - Ouvrez `GUARDADOS/REINO_results_*.txt`
   - Copiez les données vers votre outil
