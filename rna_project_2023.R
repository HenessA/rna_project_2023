# Créer un vecteur avec vos données
fichier_concatene <- c(NA, 176.6, 34.4, 163.5, 161.3, -175.7, 162.1, 11.5, 162.9, 139.4)

# Supprimer les valeurs NA
fichier_concatene <- fichier_concatene[!is.na(fichier_concatene)]

# Créer l'histogramme
hist(fichier_concatene, main = "Histogramme de la distribution", xlab = "Valeurs", col = "skyblue", border = "black")
