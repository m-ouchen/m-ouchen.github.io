# -*- coding: utf-8 -*-
"""Corrigé interactif du TP 3 — la boucle for (séance 3, bloc 2).

Toutes les sorties ont été obtenues en exécutant les programmes. Aucune liste
n'apparaît : elles ne sont traitées qu'en séance 8.
"""

META = {
    "titre": "TP 3 — La boucle for",
    "titre_onglet": "Corrigé du TP 3 : la boucle for",
    "cle": "m355-tp3-corriges-vus",
}

PARTIES = [
{"partie": "Partie A — La fonction range", "exercices": [

 {"id": "a1", "titre": "A.1 — Prédire, puis exécuter",
  "enonce": "",
  "code": "for i in range(3, 8):\n    print(i, \"x 7 =\", i * 7)\nprint(\"Fin.\")",
  "questions": [
   {"ref": "", "texte": "Qu'affiche le programme ?",
    "reponse": "Cinq lignes de table, puis la ligne finale.",
    "sortie": "3 x 7 = 21\n4 x 7 = 28\n5 x 7 = 35\n6 x 7 = 42\n7 x 7 = 49\nFin.",
    "notes": ["`range(3, 8)` produit 3, 4, 5, 6, 7 : la borne de début est **comprise**, celle de fin ne l'est pas. Cinq valeurs, donc cinq tours — 8 − 3 = 5."],
    "erreurs": [
     {"titre": "Attendre une ligne `8 x 7 = 56`",
      "cause": "C'est l'erreur de référence sur `range` : la borne de fin n'est jamais produite. Pour aller jusqu'à 8, il faut écrire `range(3, 9)`."},
     {"titre": "Commencer à 0",
      "cause": "Avec deux arguments, le premier est le début. `range(8)` commencerait à 0, mais ce n'est pas ce qui est écrit."}]}]},

 {"id": "a2", "titre": "A.2 — Ce que produit range",
  "enonce": "On remplace l'appel à `range` par chacun de ceux du tableau.",
  "questions": [
   {"ref": "", "texte": "Quelles suites obtient-on ?",
    "reponse": "Les deux derniers appels produisent une suite **vide** : la boucle ne tourne pas.",
    "pile": {"entetes": ["Appel", "Suite produite", "Tours"],
             "lignes": [["`range(4)`", "0 1 2 3", "4"],
                        ["`range(2, 7)`", "2 3 4 5 6", "5"],
                        ["`range(0, 20, 5)`", "0 5 10 15", "4"],
                        ["`range(6, 1, -1)`", "6 5 4 3 2", "5"],
                        ["`range(4, 4)`", "— rien —", "0"],
                        ["`range(4, 1)`", "— rien —", "0"]]},
    "notes": ["`range(0, 20, 5)` s'arrête à 15 : 20 serait la borne de fin, qui n'est jamais produite.",
              "`range(6, 1, -1)` descend jusqu'à 2, non jusqu'à 1 : la règle de la borne exclue vaut aussi au pas négatif.",
              "`range(4, 1)` est vide parce que le pas vaut 1 par défaut : on ne peut pas aller de 4 à 1 en avançant. Il faut `range(4, 1, -1)`."],
    "erreurs": [
     {"titre": "Attendre une erreur sur `range(4, 1)`",
      "cause": "Une suite vide n'est pas une faute. Le programme s'exécute et n'affiche rien — ce qui est bien plus difficile à diagnostiquer qu'un message d'erreur."},
     {"titre": "Écrire que `range(0, 20, 5)` produit 0 5 10 15 20",
      "cause": "La borne de fin est exclue, quel que soit le pas."}]}]},

 {"id": "a3", "titre": "A.3 — Écrire le bon range",
  "enonce": "On donne l'appel qui produit exactement chaque suite.",
  "questions": [
   {"ref": "", "texte": "Quels appels ?",
    "reponse": "Dans chaque cas, la borne de fin dépasse d'un pas la dernière valeur voulue.",
    "pile": {"entetes": ["Suite voulue", "Appel", "Pourquoi"],
             "lignes": [["1 2 3 4 5 6", "`range(1, 7)`", "pour finir à 6, la borne est 7"],
                        ["0 5 10 15 20", "`range(0, 25, 5)`", "pour finir à 20, la borne est 20 + 5"],
                        ["100 90 80 70 60", "`range(100, 50, -10)`", "pas négatif, borne 60 − 10"],
                        ["7 8 9", "`range(7, 10)`", "trois valeurs : 10 − 7"]]},
    "notes": ["La règle tient en une phrase : **la borne de fin est la première valeur qu'on ne veut pas**. Avec un pas de 1 elle vaut « dernière + 1 » ; avec un pas `p`, « dernière + p »."],
    "erreurs": [
     {"titre": "`range(100, 60, -10)` pour la troisième suite",
      "cause": "60 est exclu : la suite s'arrêterait à 70. Il faut descendre la borne sous 60."},
     {"titre": "`range(0, 20, 5)` pour la deuxième",
      "cause": "Même oubli : 20 doit être produit, donc la borne est au-delà."}]}]},

 {"id": "a4", "titre": "A.4 — Une boucle qui ne tourne pas",
  "enonce": "",
  "code": "for i in range(6, 2):\n    print(i)\nprint(\"Terminé\")",
  "questions": [
   {"ref": "", "texte": "Pourquoi le programme n'affiche-t-il que `Terminé` ? Que faut-il écrire pour obtenir 6, 5, 4, 3 ?",
    "reponse": "`range(6, 2)` est vide : le pas vaut 1 par défaut, et on ne peut pas aller de 6 à 2 en avançant.",
    "sortie": "Terminé",
    "solutions": [
     {"verdict": "retenue", "nom": "Préciser le pas négatif",
      "code": "for i in range(6, 2, -1):\n    print(i)\nprint(\"Terminé\")",
      "texte": "Produit 6, 5, 4, 3 — la borne 2 reste exclue."}],
    "notes": ["Le programme ne contient aucune erreur : il fait exactement ce qui est écrit. C'est pourquoi « mon programme n'affiche rien » est presque toujours un `range` vide, non un plantage."],
    "erreurs": [
     {"titre": "Écrire `range(6, 3, -1)`",
      "cause": "La valeur 3 doit être produite, donc la borne descend à 2."},
     {"titre": "Écrire `range(-6, -2)`",
      "cause": "On change les valeurs au lieu du sens de parcours. Le pas, troisième argument, est ce qui décide du sens."}]}]},

 {"id": "a5", "titre": "A.5 — Écrire une boucle",
  "enonce": "Afficher les multiples de 3 compris entre 3 et 30.",
  "questions": [
   {"ref": "", "texte": "Écrivez le programme.",
    "reponse": "Dix lignes, de 3 à 30 inclus.",
    "sortie": "3\n6\n9\n12\n15\n18\n21\n24\n27\n30",
    "solutions": [
     {"verdict": "retenue", "nom": "Par le pas",
      "code": "for n in range(3, 31, 3):\n    print(n)"},
     {"verdict": "ok", "nom": "Par le test de divisibilité",
      "code": "for n in range(3, 31):\n    if n % 3 == 0:\n        print(n)",
      "texte": "Correct, mais vingt-huit tours pour dix affichages. Le pas exprime directement l'intention."},
     {"verdict": "eviter", "nom": "Par la multiplication",
      "code": "for k in range(1, 11):\n    print(3 * k)",
      "texte": "Le résultat est juste, mais la variable de boucle ne porte plus la valeur affichée : le lien entre `k` et ce qu'on lit à l'écran demande un calcul mental à chaque relecture."}],
    "erreurs": [
     {"titre": "Écrire `range(3, 30, 3)`",
      "cause": "30 est la borne de fin, donc exclu : la suite s'arrête à 27."}]}]}]},

{"partie": "Partie B — Parcourir une chaîne", "exercices": [

 {"id": "b1", "titre": "B.1 — Prédire, puis exécuter",
  "enonce": "",
  "code": "ville = \"Rabat\"\nfor c in ville:\n    print(c)",
  "questions": [
   {"ref": "a)", "texte": "Qu'affiche le programme ?",
    "reponse": "Une lettre par ligne, dans l'ordre du mot.",
    "sortie": "R\na\nb\na\nt",
    "notes": ["La variable `c` prend tour à tour **chaque caractère** de la chaîne. Aucun `range` n'intervient : on parcourt directement ce qu'on veut parcourir."]},
   {"ref": "b)", "texte": "Combien de tours la boucle fait-elle, et où ce nombre est-il écrit ?",
    "reponse": "Cinq tours — un par caractère de `\"Rabat\"`. Ce nombre n'est écrit **nulle part** dans le programme.",
    "notes": ["C'est la différence avec `range` : le nombre de tours est déterminé par la chaîne elle-même. Changez `\"Rabat\"` en `\"Casablanca\"` et la boucle fera dix tours sans qu'une ligne change."],
    "erreurs": [
     {"titre": "Répondre que le nombre de tours est dans la ligne `for`",
      "cause": "La ligne `for` dit *quoi* parcourir, non *combien de fois*. La différence devient essentielle dès qu'on parcourt une saisie dont on ignore la longueur."}]}]},

 {"id": "b2", "titre": "B.2 — Compter les tours",
  "enonce": "Afficher, après la boucle, le nombre de caractères du mot — sans fonction nouvelle.",
  "questions": [
   {"ref": "", "texte": "Écrivez le programme.",
    "reponse": "Un compteur initialisé avant la boucle, incrémenté à chaque tour, lu après.",
    "solutions": [
     {"verdict": "retenue", "nom": "Compter par accumulation",
      "code": "mot = input(\"Un mot : \")\nn = 0\nfor c in mot:\n    n = n + 1\nprint(\"Caractères :\", n)"},
     {"verdict": "expert", "nom": "Ce que fait la fonction len",
      "code": "print(\"Caractères :\", len(mot))",
      "texte": "Python offre bien sûr `len`. L'exercice consiste précisément à la réécrire : une fois qu'on a compris qu'elle n'est rien d'autre que ce compteur, elle cesse d'être magique."}],
    "notes": ["La variable `c` n'est pas utilisée dans le bloc — c'est normal : on ne s'intéresse qu'au **nombre** de tours, pas à leur contenu."],
    "erreurs": [
     {"titre": "Écrire `n = n + c`",
      "cause": "On tenterait d'ajouter un caractère à un nombre : `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. Compter, c'est ajouter 1."},
     {"titre": "Placer `print` dans la boucle",
      "cause": "On obtiendrait un décompte partiel à chaque tour. Un accumulateur se lit **après** la boucle."}]}]},

 {"id": "b3", "titre": "B.3 — Compter les voyelles",
  "enonce": "",
  "code": "mot = input(\"Un mot : \")\nvoyelles = 0\nfor c in mot:\n    # à compléter\nprint(\"Voyelles :\", voyelles)",
  "questions": [
   {"ref": "a)", "texte": "Complétez le programme.",
    "reponse": "Un compte sous condition : on n'incrémente que si le caractère est une voyelle.",
    "sortie": "Un mot : Rabat\nVoyelles : 2",
    "solutions": [
     {"verdict": "retenue", "nom": "Avec l'opérateur in",
      "code": "mot = input(\"Un mot : \")\nvoyelles = 0\nfor c in mot:\n    if c in \"aeiouy\":\n        voyelles = voyelles + 1\nprint(\"Voyelles :\", voyelles)"},
     {"verdict": "eviter", "nom": "Avec six comparaisons",
      "code": "if c == \"a\" or c == \"e\" or c == \"i\" or c == \"o\" or c == \"u\" or c == \"y\":",
      "texte": "Exact, mais six fois plus long, et il faudra le reprendre pour ajouter une lettre. `in` dit la même chose en six caractères."}]},
   {"ref": "b)", "texte": "Votre programme compte-t-il les majuscules ? Sinon, comment le corriger ?",
    "reponse": "**Non.** `\"Rabat\"` donne 2 et non 3 : le `A` majuscule n'est pas dans `\"aeiouy\"`.",
    "solutions": [
     {"verdict": "retenue", "nom": "Étendre la chaîne de référence",
      "code": "if c in \"aeiouyAEIOUY\":"},
     {"verdict": "ok", "nom": "Normaliser la casse avant de tester",
      "code": "mot = input(\"Un mot : \").lower()",
      "texte": "Une seule modification suffit, et le reste du programme n'a plus à se préoccuper de la casse. C'est la solution à préférer dès que plusieurs tests sont en jeu."}],
    "notes": ["C'est le même piège qu'en séance 2, avec la réponse `O` au lieu de `o` : une comparaison de chaînes distingue toujours majuscules et minuscules."]}]},

 {"id": "b4", "titre": "B.4 — Construire une chaîne",
  "enonce": "",
  "code": "mot = input(\"Un mot : \")\nenvers = \"\"\nfor c in mot:\n    envers = c + envers\nprint(envers)",
  "questions": [
   {"ref": "a)", "texte": "Remplissez le déroulé pour le mot `CHAT`.",
    "reponse": "Chaque caractère est placé **devant** ce qui a déjà été construit.",
    "pile": {"entetes": ["Tour", "c", "envers avant", "envers après"],
             "lignes": [["1", "C", "`\"\"`", "`\"C\"`"],
                        ["2", "H", "`\"C\"`", "`\"HC\"`"],
                        ["3", "A", "`\"HC\"`", "`\"AHC\"`"],
                        ["4", "T", "`\"AHC\"`", "`\"TAHC\"`"]]},
    "sortie": "TAHC",
    "notes": ["`envers` est un accumulateur, exactement comme une somme. Son initialisation est la **chaîne vide** `\"\"` : la valeur qui laisse une concaténation inchangée, comme 0 pour une addition."],
    "erreurs": [
     {"titre": "Initialiser `envers = mot`",
      "cause": "On part de ce qu'on veut transformer au lieu de partir de rien. Le résultat serait `CHATTAHC`."}]},
   {"ref": "b)", "texte": "Que produirait `envers = envers + c` ?",
    "reponse": "Le mot **inchangé** : `CHAT`.",
    "sortie": "CHAT",
    "notes": ["L'ordre des deux opérandes est tout ce qui distingue « reconstruire à l'identique » de « renverser ». La concaténation n'est pas commutative, à la différence de l'addition."]}]}]},

{"partie": "Partie C — Accumulateurs, break et continue", "exercices": [

 {"id": "c1", "titre": "C.1 — Un produit cumulé",
  "enonce": "",
  "code": "P = 1\nfor k in range(1, 6):\n    P = P * k\nprint(\"Produit :\", P)",
  "questions": [
   {"ref": "a)", "texte": "Remplissez le déroulé.",
    "reponse": "Le produit des entiers de 1 à 5, soit la factorielle de 5.",
    "pile": {"entetes": ["Tour", "k", "P avant", "P après"],
             "lignes": [["1", "1", "1", "1"], ["2", "2", "1", "2"],
                        ["3", "3", "2", "6"], ["4", "4", "6", "24"],
                        ["5", "5", "24", "120"]]},
    "sortie": "Produit : 120"},
   {"ref": "b)", "texte": "Que vaudrait le résultat si l'on initialisait `P` à 0 ?",
    "reponse": "**0**, quelles que soient les valeurs multipliées.",
    "notes": ["`0 * k` vaut 0 pour tout `k` : le premier tour écrase tout et plus rien ne peut faire remonter l'accumulateur.",
              "L'initialisation n'est jamais arbitraire : c'est l'**élément neutre** de l'opération. 0 pour une somme, 1 pour un produit, `\"\"` pour une concaténation."],
    "erreurs": [
     {"titre": "Penser que l'erreur se verra à l'exécution",
      "cause": "Le programme affiche `Produit : 0` sans la moindre protestation. C'est une erreur logique : seule la lecture du résultat peut la révéler."}]}]},

 {"id": "c2", "titre": "C.2 — Une moyenne de mesures saisies",
  "enonce": "",
  "code": "n = int(input(\"Combien de mesures ? \"))\ntotal = 0\nfor i in range(n):\n    # à compléter\nprint(\"Moyenne :\", total / n)",
  "questions": [
   {"ref": "a)", "texte": "Complétez le programme.",
    "reponse": "Une seule ligne manque : la saisie, ajoutée au total.",
    "solutions": [
     {"verdict": "retenue", "nom": "Accumuler la saisie",
      "code": "n = int(input(\"Combien de mesures ? \"))\ntotal = 0\nfor i in range(n):\n    total = total + float(input(\"Mesure : \"))\nprint(\"Moyenne :\", total / n)"}],
    "notes": ["`range(n)` est ici le bon choix : le nombre de tours est connu avant de boucler, puisque l'utilisateur vient de le donner. La variable `i` ne sert pas — seul le nombre de tours compte."]},
   {"ref": "b)", "texte": "Que se passe-t-il si l'utilisateur répond 0 ? Comment l'éviter ?",
    "reponse": "La boucle ne tourne pas, `total` reste à 0, et la division finale échoue.",
    "sortie": "ZeroDivisionError: division by zero",
    "solutions": [
     {"verdict": "retenue", "nom": "Valider la saisie avant de boucler",
      "code": "n = int(input(\"Combien de mesures ? \"))\nwhile n < 1:\n    print(\"Il faut au moins une mesure.\")\n    n = int(input(\"Combien de mesures ? \"))",
      "texte": "La validation est un `while` : le nombre de tentatives n'est pas connu."},
     {"verdict": "ok", "nom": "Traiter le cas après coup",
      "code": "if n == 0:\n    print(\"Aucune mesure.\")\nelse:\n    print(\"Moyenne :\", total / n)",
      "texte": "Acceptable, mais le programme accepte une donnée qu'il sait inutilisable. Mieux vaut refuser à l'entrée."}],
    "notes": ["C'est le premier cas limite du module : une entrée valide du point de vue du type — 0 est bien un entier — mais hors du domaine attendu. Les deux contrôles sont nécessaires."]}]},

 {"id": "c3", "titre": "C.3 — La plus grande valeur",
  "enonce": "",
  "code": "n = int(input(\"Combien de mesures ? \"))\nmaxi = float(input(\"Mesure 1 : \"))\nfor i in range(n - 1):\n    m = float(input(\"Mesure suivante : \"))\n    if m > maxi:\n        maxi = m\nprint(\"Maximum :\", maxi)",
  "questions": [
   {"ref": "a)", "texte": "Pourquoi la boucle ne fait-elle que `n - 1` tours ?",
    "reponse": "La première mesure a déjà été saisie **avant** la boucle, pour servir de valeur de départ au maximum. Il n'en reste que `n - 1` à lire.",
    "notes": ["Si la boucle faisait `n` tours, le programme demanderait `n + 1` mesures en tout."]},
   {"ref": "b)", "texte": "Pourquoi initialiser `maxi` avec la première mesure, et non avec 0 ?",
    "reponse": "Parce que 0 n'est pas l'élément neutre d'un maximum : c'est une valeur comme une autre, qui peut être plus grande que toutes les mesures.",
    "notes": ["Sur des températures en °C, l'erreur ne se verrait pas. Sur des températures en °C sous zéro, sur des variations ou sur des soldes, le programme annoncerait 0 comme maximum alors qu'aucune mesure ne vaut 0.",
              "Un maximum n'a pas d'élément neutre dans les nombres usuels : la seule initialisation juste est **la première valeur de la série**."],
    "erreurs": [
     {"titre": "Tester sur des valeurs positives et conclure que 0 convient",
      "cause": "Le jeu d'essai ne révèle pas la faute. C'est tout l'intérêt de se demander *quelle entrée ferait échouer ce programme* plutôt que *mon programme marche-t-il sur cet exemple*."}]},
   {"ref": "c)", "texte": "Faites afficher aussi la plus petite valeur.",
    "reponse": "Un second accumulateur, initialisé de la même façon et mis à jour dans le même tour.",
    "solutions": [
     {"verdict": "retenue", "nom": "Deux extremums en une boucle",
      "code": "n = int(input(\"Combien de mesures ? \"))\npremiere = float(input(\"Mesure 1 : \"))\nmaxi = premiere\nmini = premiere\nfor i in range(n - 1):\n    m = float(input(\"Mesure suivante : \"))\n    if m > maxi:\n        maxi = m\n    if m < mini:\n        mini = m\nprint(\"Maximum :\", maxi, \"— Minimum :\", mini)"}],
    "notes": ["Les deux `if` sont indépendants : ce ne sont pas `if` / `else`, car une mesure peut n'être ni le nouveau maximum ni le nouveau minimum."],
    "erreurs": [
     {"titre": "Écrire `if m > maxi: … else: mini = m`",
      "cause": "Toute mesure qui n'est pas un nouveau maximum deviendrait le minimum. Deux conditions distinctes demandent deux `if` distincts."}]}]},

 {"id": "c4", "titre": "C.4 — S'arrêter dès qu'on a trouvé",
  "enonce": "On cherche une lettre dans un mot ; le programme n'annonce rien lorsqu'elle est absente.",
  "code": "mot = input(\"Un mot : \")\ncherche = input(\"Lettre cherchée : \")\nfor c in mot:\n    if c == cherche:\n        print(\"Lettre présente.\")\n        break",
  "questions": [
   {"ref": "a)", "texte": "Écrivez la version qui annonce aussi l'absence.",
    "reponse": "Un **témoin** booléen, créé avant la boucle, mis à `True` dès la rencontre, consulté après.",
    "solutions": [
     {"verdict": "retenue", "nom": "Avec un témoin",
      "code": "mot = input(\"Un mot : \")\ncherche = input(\"Lettre cherchée : \")\ntrouvee = False\n\nfor c in mot:\n    if c == cherche:\n        trouvee = True\n        break\n\nif trouvee:\n    print(\"Lettre présente.\")\nelse:\n    print(\"Lettre absente.\")"},
     {"verdict": "eviter", "nom": "Un else dans la boucle",
      "code": "for c in mot:\n    if c == cherche:\n        print(\"Lettre présente.\")\n        break\n    else:\n        print(\"Lettre absente.\")",
      "texte": "Le message d'absence serait affiché à **chaque** lettre qui ne convient pas. Une conclusion sur l'ensemble du parcours ne peut pas se tirer à l'intérieur du parcours."}],
    "notes": ["Le `break` reste utile : il évite de parcourir la fin du mot une fois la lettre trouvée. Mais il n'apprend rien à la suite du programme — c'est le témoin qui transporte l'information hors de la boucle."]},
   {"ref": "b)", "texte": "Pourquoi le témoin doit-il être créé **avant** la boucle ?",
    "reponse": "Parce qu'il doit exister même si la boucle ne tourne pas, et surtout parce qu'il doit **survivre** à la boucle pour être lu après.",
    "notes": ["Créé dans la boucle, il serait réinitialisé à chaque tour. Créé dans le `if`, il n'existerait tout simplement pas lorsque la lettre est absente : le `if trouvee` final lèverait `NameError: name 'trouvee' is not defined`."],
    "erreurs": [
     {"titre": "Initialiser le témoin à `True`",
      "cause": "Le témoin part de l'hypothèse **contraire** à ce qu'on cherche à établir : on suppose l'absence, et c'est la rencontre qui dément. Initialisé à `True`, il annoncerait toujours la présence."}]}]},

 {"id": "c5", "titre": "C.5 — Sauter un tour",
  "enonce": "Somme des entiers de 1 à 20 qui ne sont pas multiples de 3.",
  "questions": [
   {"ref": "a)", "texte": "Écrivez les deux versions, avec puis sans `continue`.",
    "reponse": "Les deux donnent le même résultat.",
    "sortie": "Somme : 147",
    "solutions": [
     {"verdict": "ok", "nom": "Avec continue",
      "code": "total = 0\nfor n in range(1, 21):\n    if n % 3 == 0:\n        continue\n    total = total + n\nprint(\"Somme :\", total)"},
     {"verdict": "retenue", "nom": "Avec un simple if",
      "code": "total = 0\nfor n in range(1, 21):\n    if n % 3 != 0:\n        total = total + n\nprint(\"Somme :\", total)"}],
    "notes": ["La somme de 1 à 20 vaut 210 ; les multiples de 3 qu'elle contient (3, 6, 9, 12, 15, 18) totalisent 63. 210 − 63 = 147."]},
   {"ref": "b)", "texte": "Laquelle est la plus lisible ?",
    "reponse": "La seconde, ici — mais ce n'est pas une règle générale.",
    "notes": ["Avec un seul traitement conditionnel, le `if` positif dit directement ce qu'on fait ; `continue` oblige à lire la condition à l'envers, comme une exclusion.",
              "`continue` reprend l'avantage quand le bloc est long ou quand plusieurs cas sont à écarter en tête de boucle : il évite d'indenter tout le corps sous un `if`."],
    "erreurs": [
     {"titre": "Croire que `continue` sort de la boucle",
      "cause": "C'est `break` qui sort. `continue` abandonne seulement le **tour en cours** et passe au suivant."}]}]},

 {"id": "c6", "titre": "C.6 — for ou while ?",
  "enonce": "",
  "questions": [
   {"ref": "a)", "texte": "Quelle boucle convient à chaque situation ?",
    "reponse": "La question à se poser est toujours la même : **le nombre de tours est-il connu avant d'entrer dans la boucle ?**",
    "pile": {"entetes": ["Situation", "Boucle", "Pourquoi"],
             "lignes": [["Afficher les douze mois de l'année", "`for`", "douze tours, connus d'avance"],
                        ["Demander un mot de passe jusqu'à ce qu'il soit correct", "`while`", "on ignore combien de tentatives"],
                        ["Calculer la somme des entiers de 1 à 100", "`for`", "cent tours"],
                        ["Lire des mesures jusqu'à ce que l'utilisateur tape `fin`", "`while`", "c'est l'utilisateur qui décide"]]},
    "notes": ["Les deux cas en `while` ont un trait commun : ce qui arrête la boucle est une **saisie**, donc quelque chose que le programme ne peut pas prévoir."]},
   {"ref": "b)", "texte": "Écrivez le programme de la deuxième ligne.",
    "reponse": "Une saisie validée, dans la forme vue au TP 2.",
    "solutions": [
     {"verdict": "retenue", "nom": "Redemander jusqu'au bon mot de passe",
      "code": "mot_de_passe = input(\"Mot de passe : \")\nwhile mot_de_passe != \"python\":\n    print(\"Mot de passe incorrect.\")\n    mot_de_passe = input(\"Mot de passe : \")\nprint(\"Accès autorisé.\")"},
     {"verdict": "ok", "nom": "Avec un nombre d'essais limité",
      "code": "essais = 0\nmot_de_passe = input(\"Mot de passe : \")\nwhile mot_de_passe != \"python\" and essais < 2:\n    essais = essais + 1\n    mot_de_passe = input(\"Mot de passe : \")\n\nif mot_de_passe == \"python\":\n    print(\"Accès autorisé.\")\nelse:\n    print(\"Trop de tentatives.\")",
      "texte": "La boucle s'arrête désormais pour **deux** raisons : le bon mot de passe, ou l'épuisement des essais. Le `if` qui suit doit donc déterminer laquelle des deux."}],
    "notes": ["Un vrai programme ne comparerait jamais un mot de passe ainsi, en clair et dans le code. Ce n'est ici qu'un prétexte à boucle : la question de la sécurité des mots de passe n'est pas au programme du module."]}]}]},
]
