# -*- coding: utf-8 -*-
"""Corrigé interactif du TP 2 — la boucle while (séance 3, bloc 1).

Toutes les sorties ont été obtenues en exécutant les programmes.
"""

META = {
    "titre": "TP 2 — La boucle while",
    "titre_onglet": "Corrigé du TP 2 : la boucle while",
    "cle": "m355-tp2-corriges-vus",
}

PARTIES = [
{"partie": "Partie A — Cas de base", "exercices": [

 {"id": "a1", "titre": "A.1 — Prédire, puis exécuter",
  "enonce": "On recopie ce programme dans `a1.py`, et on écrit sa prédiction avant de l'exécuter.",
  "code": "p = 0\nwhile p <= 5:\n    p = p + 1\n    print(\"p=\", p)\nprint(\"Done !\")",
  "questions": [
   {"ref": "a)", "texte": "Qu'affiche le programme ?",
    "reponse": "Sept lignes : six tours de boucle, puis la ligne finale.",
    "sortie": "p= 1\np= 2\np= 3\np= 4\np= 5\np= 6\nDone !",
    "notes": ["La boucle tourne **six** fois, pour `p` valant successivement 0, 1, 2, 3, 4 et 5 au moment du test. Au septième test, `p` vaut 6 : `6 <= 5` est faux, et la boucle s'arrête.",
              "Comme `p = p + 1` précède le `print`, la première valeur affichée est 1 et non 0, et la dernière est 6 et non 5."],
    "erreurs": [
     {"titre": "Annoncer cinq lignes",
      "cause": "On compte les valeurs 1 à 5 en oubliant que le test porte sur `p <= 5`, bornes comprises : la valeur 5 passe encore le test et produit un sixième tour."},
     {"titre": "Annoncer `p= 0` sur la première ligne",
      "cause": "C'est ce qu'on obtiendrait si le `print` venait **avant** l'incrémentation. L'ordre des deux lignes du bloc décide de ce qui s'affiche — voir D.6 du cours."},
     {"titre": "Oublier `Done !`",
      "cause": "Le dernier `print` n'est pas indenté : il n'appartient pas à la boucle et s'exécute une fois, à la sortie."}]}]},

 {"id": "a2", "titre": "A.2 — Les trois ingrédients",
  "enonce": "On retrouve dans le programme de A.1 les trois étapes indispensables de toute boucle `while`.",
  "questions": [
   {"ref": "", "texte": "Quelle ligne joue chacun des trois rôles ?",
    "reponse": "Chaque rôle tient en une ligne, et les trois sont présentes.",
    "pile": {"entetes": ["Rôle", "Ligne"],
             "lignes": [["Initialiser la variable de contrôle", "`p = 0`"],
                        ["Tester cette variable", "`while p <= 5:`"],
                        ["Modifier cette variable", "`p = p + 1`"]]},
    "notes": ["La variable de contrôle est `p` : c'est elle que la condition examine. Les trois rôles portent **sur la même variable** — c'est ce qui en fait une boucle qui s'arrête."],
    "erreurs": [
     {"titre": "Désigner `print(\"p=\", p)` comme la modification",
      "cause": "`print` lit `p` mais ne le change pas. Afficher une variable ne la fait pas avancer : une boucle dont le bloc ne contient que des `print` ne s'arrête jamais."}]}]},

 {"id": "a3", "titre": "A.3 — Une boucle qui ne démarre pas",
  "enonce": "",
  "code": "t = 0\nwhile t > 0:\n    print(t)\n    t = t - 1\nprint(\"Terminé\")",
  "questions": [
   {"ref": "", "texte": "Combien de fois le bloc s'exécute-t-il ? Pourquoi ?",
    "reponse": "**Aucune.** Le programme n'affiche qu'une ligne.",
    "sortie": "Terminé",
    "notes": ["La condition est évaluée **avant** le premier tour. `t` vaut 0, donc `0 > 0` est faux dès l'entrée : le bloc est enjambé et l'exécution reprend après la boucle.",
              "Une boucle `while` peut donc tourner zéro fois. Ce n'est ni une erreur ni un cas rare : c'est exactement ce qu'on veut d'une boucle de validation lorsque la première saisie est déjà correcte."],
    "erreurs": [
     {"titre": "Répondre « une fois »",
      "cause": "On suppose qu'un bloc s'exécute au moins une fois avant que la condition ne soit vérifiée. C'est le comportement d'un `do … while` dans d'autres langages ; Python n'en a pas."},
     {"titre": "Répondre que le programme plante",
      "cause": "Rien n'est anormal ici. Une suite d'instructions non exécutée ne produit aucune erreur."}]}]},

 {"id": "a4", "titre": "A.4 — Changer le pas",
  "enonce": "Écrire `a4.py` qui compte de 0 à 10 de deux en deux.",
  "questions": [
   {"ref": "", "texte": "Écrivez le programme.",
    "reponse": "Seul le pas change par rapport à A.1 : on ajoute 2 au lieu de 1.",
    "sortie": "0\n2\n4\n6\n8\n10",
    "solutions": [
     {"verdict": "retenue", "nom": "Compter par pas de deux",
      "code": "p = 0\nwhile p <= 10:\n    print(p)\n    p = p + 2"},
     {"verdict": "ok", "nom": "Compter de un en un et ne retenir que les pairs",
      "code": "p = 0\nwhile p <= 10:\n    if p % 2 == 0:\n        print(p)\n    p = p + 1",
      "texte": "Correct, mais la boucle fait onze tours pour six affichages. Quand le pas suffit, il est préférable au filtrage."}],
    "erreurs": [
     {"titre": "Écrire `while p < 10`",
      "cause": "La valeur 10 doit être affichée : la borne est **comprise**, donc `<=`. Avec `<`, la suite s'arrête à 8."},
     {"titre": "Placer `p = p + 2` avant le `print`",
      "cause": "La suite commencerait à 2 et finirait à 12 — l'erreur que A.1 a déjà montrée."}]}]},

 {"id": "a5", "titre": "A.5 — Compter dans l'autre sens",
  "enonce": "Écrire `a5.py` qui affiche les entiers de 20 à 10, un par ligne.",
  "questions": [
   {"ref": "", "texte": "Écrivez le programme.",
    "reponse": "Compter à rebours demande deux changements simultanés : le sens du test et le sens de la modification.",
    "sortie": "20\n19\n18\n17\n16\n15\n14\n13\n12\n11\n10",
    "solutions": [
     {"verdict": "retenue", "nom": "Décompte",
      "code": "n = 20\nwhile n >= 10:\n    print(n)\n    n = n - 1"}],
    "notes": ["Onze lignes sont affichées : de 20 à 10 inclus, il y a 20 − 10 + 1 = 11 valeurs. L'oubli du « + 1 » est l'erreur de comptage la plus fréquente."],
    "erreurs": [
     {"titre": "Garder `n = n + 1` en inversant seulement le test",
      "cause": "La condition `n >= 10` est vraie dès le départ et le reste à jamais, puisque `n` ne fait que grandir : boucle infinie. Le test et la modification doivent être **cohérents**."},
     {"titre": "Écrire `while n > 10`",
      "cause": "La valeur 10 n'est alors pas affichée. Pour inclure la borne, il faut `>=`."}]}]}]},

{"partie": "Partie B — Boucles infinies", "exercices": [

 {"id": "b1", "titre": "B.1 — Provoquer l'accident",
  "enonce": "On reprend `a1.py` en supprimant `p = p + 1`.",
  "code": "p = 0\nwhile p <= 5:\n    print(\"p=\", p)",
  "questions": [
   {"ref": "", "texte": "Que s'est-il passé ?",
    "reponse": "Le programme affiche `p= 0` indéfiniment, jusqu'à ce qu'on l'interrompe par **Ctrl + C**.",
    "sortie": "p= 0\np= 0\np= 0\n…",
    "notes": ["`p` garde la valeur 0 : la condition `0 <= 5` reste vraie à chaque test, et rien dans le bloc ne peut la rendre fausse.",
              "Le programme ne « plante » pas : il fonctionne exactement comme écrit. C'est le programme qui est faux, pas la machine — et aucun message d'erreur ne viendra le signaler."],
    "erreurs": [
     {"titre": "Croire que Python finira par s'arrêter de lui-même",
      "cause": "Rien n'arrête une boucle infinie : ni le nombre de tours, ni la quantité affichée. Seule une interruption extérieure — **Ctrl + C** — y met fin."}]}]},

 {"id": "b3", "titre": "B.3 — Trois boucles à réparer",
  "enonce": "Pour chacune, dire ce qui cloche, puis corriger.",
  "questions": [
   {"ref": "1)", "texte": "`n = 1` ; `while n < 5:` ; `print(n)` ; `n = n - 1`",
    "reponse": "La variable est modifiée **dans le mauvais sens** : `n` décroît alors que la condition attend qu'il croisse.",
    "notes": ["C'est la deuxième question du diagnostic : *est-elle modifiée dans le bon sens ?* La boucle affiche 1, 0, −1, −2… sans fin."],
    "solutions": [
     {"verdict": "retenue", "nom": "Inverser l'opération",
      "code": "n = 1\nwhile n < 5:\n    print(n)\n    n = n + 1"}]},

   {"ref": "2)", "texte": "`n = 1` ; `while n < 5:` ; `print(n)` ; puis `n = n + 1` non indenté",
    "reponse": "La modification existe, mais elle est **hors du bloc** : elle ne s'exécutera qu'après la boucle, c'est-à-dire jamais.",
    "notes": ["C'est la troisième question du diagnostic. L'indentation n'est pas une mise en forme : elle décide de ce qui appartient à la boucle."],
    "solutions": [
     {"verdict": "retenue", "nom": "Indenter la modification",
      "code": "n = 1\nwhile n < 5:\n    print(n)\n    n = n + 1"}],
    "erreurs": [
     {"titre": "Chercher l'erreur dans la condition",
      "cause": "`n < 5` est correct. Devant une boucle infinie, on vérifie d'abord que la modification existe, puis son sens, puis son indentation — dans cet ordre."}]},

   {"ref": "3)", "texte": "`reponse = input(…)` ; `while reponse == \"o\":` ; `print(\"On continue.\")`",
    "reponse": "La variable testée n'est **jamais modifiée** dans le bloc : la saisie a lieu une seule fois, avant la boucle.",
    "notes": ["Si l'utilisateur répond autre chose que `o`, la boucle ne tourne pas du tout ; s'il répond `o`, elle ne s'arrête plus. Les deux comportements viennent de la même cause."],
    "solutions": [
     {"verdict": "retenue", "nom": "Redemander dans la boucle",
      "code": "reponse = input(\"Continuer ? (o/n) \")\nwhile reponse == \"o\":\n    print(\"On continue.\")\n    reponse = input(\"Continuer ? (o/n) \")"}],
    "erreurs": [
     {"titre": "Déplacer la saisie avant la boucle en croyant corriger",
      "cause": "Elle y est déjà. Ce qui manque est une **seconde** saisie, à l'intérieur du bloc, pour que la condition puisse changer de valeur."}]}]}]},

{"partie": "Partie C — Accumulateurs et sorties contrôlées", "exercices": [

 {"id": "c1", "titre": "C.1 — Accumuler au fil des tours",
  "enonce": "",
  "code": "somme = 0\nn = 1\nwhile n <= 5:\n    somme = somme + n\n    n = n + 1\nprint(\"Somme :\", somme)",
  "questions": [
   {"ref": "", "texte": "Remplissez le tableau de déroulé, puis donnez l'affichage.",
    "reponse": "La boucle fait cinq tours ; `somme` passe de 0 à 15.",
    "pile": {"entetes": ["Tour", "n avant", "somme avant", "somme après"],
             "lignes": [["1", "1", "0", "1"], ["2", "2", "1", "3"],
                        ["3", "3", "3", "6"], ["4", "4", "6", "10"],
                        ["5", "5", "10", "15"]]},
    "sortie": "Somme : 15",
    "notes": ["`somme` est l'**accumulateur**, `n` la variable de contrôle. Les deux changent à chaque tour, mais elles ne jouent pas le même rôle : la condition ne porte que sur `n`."],
    "erreurs": [
     {"titre": "Placer `somme = 0` dans la boucle",
      "cause": "L'accumulateur serait remis à zéro à chaque tour et le programme afficherait 5, la dernière valeur ajoutée. Aucun message d'erreur : le résultat est simplement faux."}]}]},

 {"id": "c2", "titre": "C.2 — Compter combien",
  "enonce": "Compléter le programme pour compter, parmi cinq températures saisies, combien dépassent 38.0.",
  "code": "saisies = 0\nnb_fievre = 0\nwhile saisies < 5:\n    t = float(input(\"Température : \"))\n    # à compléter",
  "questions": [
   {"ref": "", "texte": "Complétez le programme.",
    "reponse": "Deux accumulateurs cohabitent : `saisies` contrôle la boucle, `nb_fievre` compte.",
    "solutions": [
     {"verdict": "retenue", "nom": "Compter sous condition",
      "code": "saisies = 0\nnb_fievre = 0\nwhile saisies < 5:\n    t = float(input(\"Température : \"))\n    if t > 38.0:\n        nb_fievre = nb_fievre + 1\n    saisies = saisies + 1\nprint(\"Au-dessus de 38 :\", nb_fievre)"}],
    "notes": ["`saisies = saisies + 1` doit être **hors du `if`** : on compte une saisie à chaque tour, qu'elle dépasse le seuil ou non. Placée dans le `if`, elle rendrait la boucle infinie dès la première température normale."],
    "erreurs": [
     {"titre": "Indenter `saisies = saisies + 1` sous le `if`",
      "cause": "La variable de contrôle n'avance plus que lorsque la condition est vraie. Une seule température normale suffit à bloquer le programme."},
     {"titre": "Écrire `nb_fievre = nb_fievre + t`",
      "cause": "On additionne les températures au lieu de compter les cas. Un **compte** s'incrémente de 1 ; une **somme** ajoute la valeur."}]}]},

 {"id": "c3", "titre": "C.3 — while True et la sortie par break",
  "enonce": "",
  "code": "while True:\n    ligne = input(\"Température (vide pour finir) : \")\n    if ligne == \"\":\n        break\n    print(\"Reçu :\", float(ligne))\nprint(\"Fin de la saisie.\")",
  "questions": [
   {"ref": "a)", "texte": "Combien de températures pouvez-vous saisir ?",
    "reponse": "Autant qu'on veut : le nombre de tours n'est pas fixé, c'est l'utilisateur qui décide d'arrêter en validant une ligne vide.",
    "notes": ["C'est précisément le cas où `while` s'impose : la condition d'arrêt ne peut être évaluée qu'**après** avoir lu la saisie, donc au milieu du bloc."]},
   {"ref": "b)", "texte": "Que se passe-t-il si vous oubliez le `break` ?",
    "reponse": "La boucle devient infinie, et la ligne vide provoque en plus une erreur.",
    "sortie": "ValueError: could not convert string to float: ''",
    "notes": ["`while True` est une condition qui ne peut jamais devenir fausse : sans `break`, rien n'arrête la boucle. Ici l'exécution s'interrompt tout de même, mais sur une erreur de conversion — ce qui masque la vraie faute."],
    "erreurs": [
     {"titre": "Conclure que le programme « marche quand même »",
      "cause": "Il s'arrête sur une exception, ce qui n'est pas un arrêt voulu. Un programme qui se termine par une erreur n'a pas fonctionné."}]}]},

 {"id": "c4", "titre": "C.4 — Un menu qui tourne",
  "enonce": "On ajoute au menu une entrée « 4 — Afficher le nombre de saisies effectuées ».",
  "questions": [
   {"ref": "", "texte": "Quel code ajouter, et où ?",
    "reponse": "Un accumulateur déclaré **avant** la boucle, incrémenté dans la branche de saisie, et lu dans la nouvelle branche.",
    "solutions": [
     {"verdict": "retenue", "nom": "Les trois endroits à modifier",
      "code": "nb_saisies = 0          # avant la boucle\nchoix = \"\"\nwhile choix != \"3\":\n    print()\n    print(\"1 — Saisir une température\")\n    print(\"2 — Afficher le seuil de fièvre\")\n    print(\"3 — Quitter\")\n    print(\"4 — Afficher le nombre de saisies effectuées\")\n    choix = input(\"Votre choix : \")\n\n    if choix == \"1\":\n        print(\"Saisie :\", float(input(\"Valeur : \")))\n        nb_saisies = nb_saisies + 1      # dans la branche\n    elif choix == \"2\":\n        print(\"Seuil : 38.0 °C\")\n    elif choix == \"3\":\n        print(\"Au revoir.\")\n    elif choix == \"4\":\n        print(\"Saisies effectuées :\", nb_saisies)\n    else:\n        print(\"Choix inconnu.\")"}],
    "notes": ["Le `print` du menu doit lui aussi être complété : une entrée qui fonctionne mais que rien n'annonce reste invisible.",
              "La nouvelle branche est un `elif`, non un `if` : les quatre choix s'excluent, et un `if` indépendant ferait tester la condition même après qu'un autre choix a été reconnu."],
    "erreurs": [
     {"titre": "Déclarer `nb_saisies = 0` dans la boucle",
      "cause": "Le compteur repartirait de zéro à chaque passage au menu et afficherait toujours 0 ou 1."},
     {"titre": "Incrémenter à chaque tour de boucle",
      "cause": "On compterait les passages au menu, non les saisies. L'incrémentation appartient à la branche `choix == \"1\"`."}]}]},

 {"id": "c5", "titre": "C.5 — Insister jusqu'à une saisie valide",
  "enonce": "On compare les deux écritures possibles de la saisie validée.",
  "questions": [
   {"ref": "a)", "texte": "Écrivez `c5.py`.",
    "reponse": "La boucle ne s'arrête que lorsque la valeur tombe dans l'intervalle.",
    "solutions": [
     {"verdict": "retenue", "nom": "Saisie validée",
      "code": "t = float(input(\"Température : \"))\nwhile t < 30 or t > 45:\n    print(\"Température invalide.\")\n    t = float(input(\"Température : \"))\nprint(\"Valeur retenue :\", t)"}],
    "notes": ["La condition dit ce qui est **invalide**, donc ce qui fait continuer la boucle. L'écrire à l'envers — `while t >= 30 and t <= 45` — ferait boucler sur les valeurs correctes."]},

   {"ref": "b)", "texte": "Les deux écritures font-elles le même travail ?",
    "reponse": "**Oui**, elles produisent le même résultat ; elles diffèrent par la forme, non par le comportement.",
    "pile": {"entetes": ["", "Écriture 1", "Écriture 2"],
             "lignes": [["Saisie correcte du premier coup", "un seul appel à `input`", "un seul appel à `input`"],
                        ["Trois saisies invalides", "quatre appels", "quatre appels"],
                        ["Ligne `input` écrite", "deux fois", "une seule fois"],
                        ["Condition exprimée", "ce qui est invalide", "ce qui est valide"]]},
    "notes": ["L'écriture 2 n'écrit la ligne de saisie qu'une fois : si le message doit changer, il n'y a qu'un endroit à corriger. L'écriture 1 n'emploie pas `break`, ce qui la rend plus facile à lire tant qu'on débute.",
              "Les deux sont acceptées. Ce qui compte est de savoir **justifier** son choix."],
    "erreurs": [
     {"titre": "Affirmer que l'écriture 2 demande toujours au moins une saisie de plus",
      "cause": "Non : `break` s'exécute dès que la valeur est correcte, donc dès le premier tour si la saisie est bonne. Les deux écritures appellent `input` le même nombre de fois."}]}]}]},
]
