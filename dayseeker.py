# Déclaration des variables permettant de saisir la date recherchée

def est_bissextile(annee):
    """
    :param annee: Reçoit une année afin de déterminer si l'année est bissextile
    :return: retourne True ou False
    """
    res = False

    # Vérifie si l'année est divisible par 4
    if annee % 4 == 0:
        # Détermine si l'année n'est pas divisible par 100
        if annee % 100 != 0:
            # Retourne True si l'année n'est pas divisible par 100
            res = True
        # Détermine si l'année est divisible par 400 dans le cas où celle-ci est divisible par 100
        elif annee % 400 == 0:
            # Retourne True si l'année est divisible par 400
            res = True
    return res


def soustraction_bissextile(year, month):
    """
    :param year: prend en paramètre une année sélectionnée par l'utilisateur
    :param month: prend en paramètre un mois sélectionné par l'utilisateur
    :return: retourne un int dont la valeur est soit 0 ou -1
    """
    res = 0
    # Vérifie que l'année est bissextile et que le mois vaut 1 ou 2
    if est_bissextile(year) and (month == 1 or month == 2):
        res = -1
    return res


def recherche_siecle(year):
    """
    :param year: prend en paramètre une année sélectionnée par l'utilisateur
    :return: retourne la valeur dans la liste siecle en fonction des deux premiers chiffres de l'année
    """
    # Extrait les deux premiers chiffres de l'année
    siecle_a_chercher = int(str(year)[:-2])
    # Boucle permettant de chercher dans la liste siecle si la valeur de siecle_a_chercher est présente
    for i in range(len(siecle)):
        # Si la valeur siecle_a_chercher est présente dans la liste, on retourne sa valeur
        if siecle_a_chercher == siecle[i][0]:
            return siecle[i][1]


# Saisie du jour, du mois et de l'année par l'utilisateur
jour, mois, annee = 0, 0, 0
while not(1 <= jour <= 31):
    jour = int(input("Saisissez la date au format JJ >>> "))  # Jour au format JJ - type: int

while not(1 <= mois <= 12):
    mois = int(input("Saisissez le mois au format MM >>> "))  # Mois au format MM - type: int

while not(1600 <= annee < 2200):
    annee = int(input("Saisissez l'année au format AAAA (comprise entre 1600 et 2199 inclus) >>> "))  # Année au format AAAA - type int


# Liste de correspondance entre les mois de l'année et leur valeur associée pour le calcul du jour
calendrier = [['Janvier', 0], ['Février', 3], ['Mars', 3], ['Avril', 6], ['Mai', 1], ['Juin', 4], ['Juillet', 6],
              ['Août', 2], ['Septembre', 5], ['Octobre', 0], ['Novembre', 3], ['Décembre', 5]]

# Liste de correspondance entre le siècle et leur valeur associée pour le calcul du jour
siecle = [[16, 6], [17, 4], [18, 2], [19, 0], [20, 6], [21, 4]]

# Liste des jours de la semaine
liste_jours = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']

"""
Déclaration de la variable permettant d'obtenir le jour
On récupère les 2 derniers chiffres de l'année puis on les caste en int
"""
num_jour = int(str(annee)[-2:])
# On ajoute 1/3 de l'année à num_jour
num_jour += int(num_jour / 4) + jour + calendrier[mois - 1][1] + soustraction_bissextile(annee, mois) + recherche_siecle(annee)
num_jour %= 7

print("Le %s/%s/%s est un %s" % (jour, mois, annee, liste_jours[num_jour]))
