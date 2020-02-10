# coding : utf-8

## Allô Jean-Hugues! Je vais ajouter mes commentaires au code comme tu me l'as demandé lors du premier travail. 

## Le script utilisé en est un inspiré de forums et de vidéos sur Youtube. C'est honnêtement la seule option qui a fonctionnée pour moi... (Ce message avait été écrit quand mon script n'était pas tout à fait terminé. Maintenant, je comprends pourquoi j'ai utilisé ces variables, la commande if et la commande from. Avec du recul, tout fait beaucoup plus de sens maintenant.)

import csv
import json
import requests 


fichier = "lobby.csv"

url = "http://jhroy.ca/uqam/lobby.json"

entetes = {
    "User-Agent":"Charles Mathieu - 514-746-5481 : requête envoyée dans le cadre d'une démarche journalistique", 
    "From":"charlesbmathieu@hotmail.com"
}

## Je pourrais peut-être l'utiliser pour savoir combien il y a de fichiers au total:
# n = 0      
# ##Finalement je l'ai utilisé une fois pour remarquer qu'il n'y a pas exactement 72000 lignes dans le fichier. 

r = requests.get(url,headers=entetes)

print(r)

## Avec ce début de script, j'ai enfin pu accéder au fichier que tu [J-H] as envoyé. À partir de ce moment, je peux commencer à trier les données qui s'y trouvent.


## Je vais créer ici une boucle dans laquelle si le status_code est 200, je vais pouvoir sélectionner TOUTES les lignes présentes dans le document JSON. Je me suis inspiré d'un vidéo que j'ai trouvé sur Youtube. Le voici: https://www.youtube.com/watch?v=Badod-8GuVU. Finalement, j'ai réalisé que c'était la même matière que tu nous avais montré en classe. 
## La fonction for each in Lobby["registre"] vient jouer ce rôle. Cela veut dire que toutes les listes qui se retrouvent dans "registre", je vais aller sélectionner certains éléments. 

if r.status_code == 200:
    lobby = r.json()
    for ligne in lobby["registre"]:

       ## J'ai ici tenté de trouver les autres objets et obje
        # if ligne[1][1]["objet"] in lobby["registre"]:
        #     sujet2 = ligne[1][1]["objet"]
        #     sujetC2 = ligne[1][1]["objet_autre"]
        #     infos.append(sujet2)
        #     infos.append(sujetC2)
            
        if "limat" in ligne[1][0]["objet"] or "limat" in ligne[1][0]["objet_autre"]:

            ## Définir la liste dans laquelle je vais .append mes éléments. 
            infos = []
    
            ## Il faut définir mes variables
            NomA = ligne[0]["en_client_org_corp_nm"]
            NomF = ligne[0]["fr_client_org_corp_nm"]
            Date = ligne[0]["date_comm"]
            Num = ligne[0]["client_org_corp_num"]
            sujet1 = ligne[1][0]["objet"]
            sujetC1 = ligne[1][0]["objet_autre"]
            institutionvisée = ligne[2][0]["institution"]
            
      ## Je ne comprends pas pourquoi les sujets suivants ne fonctionnent pas... Cela dit que je ne peux pas les trouver dans le fichier. Ça dit: "out of range"... 
            ## Je ne suis toutefois pas certain que cela soit nécessaire pour le travail... Bien hâte de le savoir. 
            # sujet2 = ligne[1][1]["objet"]
            # sujetC2 = ligne[1][1]["objet_autre"]
            # sujet3 = ligne[1][2]["objet"]
            # sujetC3 = ligne[1][2]["objet_autre"]
        
            infos.append(NomA)
            infos.append(NomF)
            infos.append(Date)
            infos.append(Num)
            infos.append(sujet1)
            infos.append(sujetC1)
            infos.append(institutionvisée)
            # infos.append(sujet2)
            # infos.append(sujetC2)
            # infos.append(sujet3)
            # infos.append(sujetC3)

            ## Vérifier si tout est beau avec la liste créée. Je vois qu'il y a seulement "climate" que l'on retrouve comme sujet de discussion. 

            print(infos)

            ## Création du fichier csv demandé. En esperant que Ginette Reno m'apportera une victoire comme elle l'avait fait pour les Canadiens en séries éliminatoires. 

            ginette = open(fichier, "a")
            reno = csv.writer(ginette)
            reno.writerow(infos)



## Ici est un script que j'ai tenté au tout début avant de fouiller sur Youtube. Comme tu l'as surement deviné, cela ne fonctionnait pas. J'ai tout de même décidé de te le laisser en bas de page pour que tu puisses voir l'évolution du processus. 

# for m in range(0, 72000):
    #     NomA = lobby[{}][0]["en_client_org_corp_nm"].format(m)
    #     NomF = lobby[{}][0]["fr_client_org_corp_nm"].format(m)
    #     Date = lobby[{}][0]["date_comm"].format(m)
    #     Num = lobby[{}][0]["client_org_corp_num"].format(m)
    #     sujet1 = lobby[{}][1][0]["objet"].format(m)
    #     sujetA1 = lobby[{}][1][0]["objet_autre"].format(m)
    #     sujet2 = lobby[{}][1][0]["objet"].format(m)
    #     sujetA2 = lobby[{}][1][0]["objet_autre"].format(m)
    #     sujet3 = lobby[{}][1][0]["objet"].format(m)
    #     sujetA3 = lobby[{}][1][0]["objet_autre"].format(m)
        
    #     infos = []

    #     infos.append(NomA)
    #     infos.append(NomF)
    #     infos.append(Date)
    #     infos.append(Num)
    #     infos.append(sujet1)
    #     infos.append(sujetA1)
    #     infos.append(sujet2)
    #     infos.append(sujetA2)
    #     infos.append(sujet3)
    #     infos.append(sujetA3)

    # print(infos)
