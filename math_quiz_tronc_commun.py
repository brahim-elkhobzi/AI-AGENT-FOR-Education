
# Math Quiz Questions for tronc commun Level
questions_by_topic = {
    "Ensembles de nombres": [
        {
            "question": "Quel ensemble contient tous les nombres entiers ?",
            "options": ["ℕ", "ℤ", "ℚ", "ℝ"],
            "correct": "ℤ",
            "explanation": "ℤ contient tous les entiers (positifs, négatifs, zéro).",
            "level": "Tronc Commun",
            "topic": "Ensembles de nombres"
        },
        {
            "question": "√2 appartient à quel ensemble ?",
            "options": ["ℤ", "ℚ", "ℝ", "ℕ"],
            "correct": "ℝ",
            "explanation": "√2 est irrationnel, donc dans ℝ mais pas dans ℚ.",
            "level": "Tronc Commun",
            "topic": "Ensembles de nombres"
        },
        {
            "question": "L’ensemble {0, 1, 2, …} est :",
            "options": ["ℤ", "ℕ", "ℚ", "ℝ⁺"],
            "correct": "ℕ",
            "explanation": "ℕ contient les entiers naturels (0 inclus).",
            "level": "Tronc Commun",
            "topic": "Ensembles de nombres"
        },
        # ... 17 more questions
        {
            "question": "L’union de ℕ et ℤ⁻ donne :",
            "options": ["ℤ", "ℚ", "ℝ", "ℕ"],
            "correct": "ℤ",
            "explanation": "ℕ ∪ ℤ⁻ = {…, -2, -1, 0, 1, …} = ℤ.",
            "level": "Tronc Commun",
            "topic": "Ensembles de nombres"
        }
    ],
    "Arithmétique dans ℕ": [
        {
            "question": "PGCD de 12 et 18 ?",
            "options": ["6", "12", "3", "9"],
            "correct": "6",
            "explanation": "PGCD par l'algorithme d'Euclide.",
            "level": "Tronc Commun",
            "topic": "Arithmétique dans ℕ"
        },
        {
            "question": "PPCM de 6 et 8 ?",
            "options": ["24", "48", "12", "16"],
            "correct": "24",
            "explanation": "PPCM = (6×8)/PGCD(6,8).",
            "level": "Tronc Commun",
            "topic": "Arithmétique dans ℕ"
        },
        {
            "question": "15 est-il premier ?",
            "options": ["Non", "Oui", "Parfois", "Toujours"],
            "correct": "Non",
            "explanation": "15 = 3×5, donc pas premier.",
            "level": "Tronc Commun",
            "topic": "Arithmétique dans ℕ"
        },
        # ... 17 more questions
        {
            "question": "Nombre de diviseurs de 12 ?",
            "options": ["6", "4", "3", "5"],
            "correct": "6",
            "explanation": "Diviseurs : 1, 2, 3, 4, 6, 12.",
            "level": "Tronc Commun",
            "topic": "Arithmétique dans ℕ"
        }
    ],
    "Calcul vectoriel": [
        {
            "question": "Somme de u(1,2) et v(3,4) ?",
            "options": ["(4,6)", "(2,6)", "(3,2)", "(1,4)"],
            "correct": "(4,6)",
            "explanation": "u + v = (1+3, 2+4) = (4,6).",
            "level": "Tronc Commun",
            "topic": "Calcul vectoriel"
        },
        {
            "question": "Produit de u(2,1) par 3 ?",
            "options": ["(6,3)", "(5,4)", "(3,2)", "(2,3)"],
            "correct": "(6,3)",
            "explanation": "3u = (3×2, 3×1) = (6,3).",
            "level": "Tronc Commun",
            "topic": "Calcul vectoriel"
        },
        # ... 18 more questions
        {
            "question": "Vecteur nul dans ℝ² ?",
            "options": ["(0,0)", "(1,0)", "(0,1)", "(-1,-1)"],
            "correct": "(0,0)",
            "explanation": "Le vecteur nul a toutes ses coordonnées à 0.",
            "level": "Tronc Commun",
            "topic": "Calcul vectoriel"
        }
    ],
    "Projection": [
        {
            "question": "Projection de A(2,3) sur l’axe des x ?",
            "options": ["(2,0)", "(0,3)", "(2,3)", "(0,0)"],
            "correct": "(2,0)",
            "explanation": "Projection sur x : (x,0).",
            "level": "Tronc Commun",
            "topic": "Projection"
        },
        {
            "question": "Projection de B(1,4) sur l’axe des y ?",
            "options": ["(0,4)", "(1,0)", "(1,4)", "(4,1)"],
            "correct": "(0,4)",
            "explanation": "Projection sur y : (0,y).",
            "level": "Tronc Commun",
            "topic": "Projection"
        },
        # ... 18 more questions
        {
            "question": "Coordonnée y de la projection de (5,2) sur y ?",
            "options": ["2", "5", "0", "1"],
            "correct": "2",
            "explanation": "Projection sur y : (0,2), donc y = 2.",
            "level": "Tronc Commun",
            "topic": "Projection"
        }
    ],
    "Ordre dans ℝ": [
        {
            "question": "Si x > 2, alors x + 1 > ?",
            "options": ["3", "2", "1", "0"],
            "correct": "3",
            "explanation": "x + 1 > 2 + 1 = 3.",
            "level": "Tronc Commun",
            "topic": "Ordre dans ℝ"
        },
        {
            "question": "Solution de x < -1 ?",
            "options": ["(-∞,-1)", "(-1,∞)", "[0,1]", "[-1,0]"],
            "correct": "(-∞,-1)",
            "explanation": "x < -1 donne (-∞,-1).",
            "level": "Tronc Commun",
            "topic": "Ordre dans ℝ"
        },
        # ... 18 more questions
        {
            "question": "Si x ≤ 0, alors -x ≥ ?",
            "options": ["0", "-1", "1", "-2"],
            "correct": "0",
            "explanation": "Multiplier par -1 inverse l’inégalité.",
            "level": "Tronc Commun",
            "topic": "Ordre dans ℝ"
        }
    ],
    "Droite dans le plan": [
        {
            "question": "Équation de la droite passant par (0,1) et (1,2) ?",
            "options": ["y = x + 1", "y = x", "y = 2x", "y = x - 1"],
            "correct": "y = x + 1",
            "explanation": "Pente = (2-1)/(1-0) = 1, ordonnée à l’origine = 1.",
            "level": "Tronc Commun",
            "topic": "Droite dans le plan"
        },
        {
            "question": "Pente de y = 2x + 3 ?",
            "options": ["2", "3", "1", "-2"],
            "correct": "2",
            "explanation": "Pente = coefficient de x.",
            "level": "Tronc Commun",
            "topic": "Droite dans le plan"
        },
        # ... 18 more questions
        {
            "question": "Intersection de y = x et y = -x + 2 ?",
            "options": ["(1,1)", "(0,2)", "(2,0)", "(1,0)"],
            "correct": "(1,1)",
            "explanation": "Résoudre x = -x + 2 donne x = 1, y = 1.",
            "level": "Tronc Commun",
            "topic": "Droite dans le plan"
        }
    ],
    "Polynômes": [
        {
            "question": "Degré de P(x) = 2x³ + x ?",
            "options": ["3", "2", "1", "4"],
            "correct": "3",
            "explanation": "Degré = plus grand exposant.",
            "level": "Tronc Commun",
            "topic": "Polynômes"
        },
        {
            "question": "Racine de P(x) = x² - 4 ?",
            "options": ["2", "1", "0", "3"],
            "correct": "2",
            "explanation": "x² - 4 = 0 donne x = ±2.",
            "level": "Tronc Commun",
            "topic": "Polynômes"
        },
        # ... 18 more questions
        {
            "question": "P(x) = x² + 1 a-t-il des racines réelles ?",
            "options": ["Non", "Oui", "Une", "Infini"],
            "correct": "Non",
            "explanation": "x² + 1 ≥ 1, pas de racines réelles.",
            "level": "Tronc Commun",
            "topic": "Polynômes"
        }
    ],
    "Équations et systèmes": [
        {
            "question": "Solution de 2x + 3 = 7 ?",
            "options": ["2", "1", "3", "0"],
            "correct": "2",
            "explanation": "2x = 4, x = 2.",
            "level": "Tronc Commun",
            "topic": "Équations et systèmes"
        },
        {
            "question": "Solution de x + y = 3, x - y = 1 ?",
            "options": ["(2,1)", "(1,2)", "(3,0)", "(0,3)"],
            "correct": "(2,1)",
            "explanation": "Additionner : 2x = 4, x = 2, y = 1.",
            "level": "Tronc Commun",
            "topic": "Équations et systèmes"
        },
        # ... 18 more questions
        {
            "question": "Solution de 3x - 6 = 0 ?",
            "options": ["2", "1", "3", "0"],
            "correct": "2",
            "explanation": "3x = 6, x = 2.",
            "level": "Tronc Commun",
            "topic": "Équations et systèmes"
        }
    ],
    "Trigonométrie 1": [
        {

            "question": "Valeur de sin(π/6) ?",
            "options": ["1/2", "√3/2", "1", "0"],
            "correct": "1/2",
            "explanation": "Valeur usuelle de sin(30°).",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 1"
        },
        {
            "question": "cos(π/4) = ?",
            "options": ["√2/2", "1/2", "√3/2", "1"],
            "correct": "√2/2",
            "explanation": "Valeur usuelle de cos(45°).",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 1"
        },
        # ... 18 more questions
        {
            "question": "tan(π/6) = ?",
            "options": ["1/√3", "√3", "1", "0"],
            "correct": "1/√3",
            "explanation": "tan(π/6) = sin(π/6)/cos(π/6).",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 1"
        }
    ],
    "Trigonométrie 2": [
        {
            "question": "sin²(x) + cos²(x) = ?",
            "options": ["1", "0", "2", "-1"],
            "correct": "1",
            "explanation": "Identité trigonométrique fondamentale.",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 2"
        },
        {
            "question": "Valeur de tan(π/3) ?",
            "options": ["√3", "1", "1/√3", "0"],
            "correct": "√3",
            "explanation": "Valeur usuelle de tan(60°).",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 2"
        },
        # ... 18 more questions
        {
            "question": "cos(π/2 - x) = ?",
            "options": ["sin(x)", "cos(x)", "-sin(x)", "-cos(x)"],
            "correct": "sin(x)",
            "explanation": "Identité : cos(π/2 - x) = sin(x).",
            "level": "Tronc Commun",
            "topic": "Trigonométrie 2"
        }
    ],
    "Fonctions": [
        {
            "question": "Domaine de f(x) = 1/x ?",
            "options": ["ℝ\\{0}", "ℝ", "[0,∞)", "[-1,1]"],
            "correct": "ℝ\\{0}",
            "explanation": "x ≠ 0 pour éviter division par 0.",
            "level": "Tronc Commun",
            "topic": "Fonctions"
        },
        {
            "question": "f(x) = x² est-elle paire ?",
            "options": ["Oui", "Non", "Parfois", "Jamais"],
            "correct": "Oui",
            "explanation": "f(-x) = f(x), donc paire.",
            "level": "Tronc Commun",
            "topic": "Fonctions"
        },
        # ... 18 more questions
        {
            "question": "Image de f(x) = x + 1 ?",
            "options": ["ℝ", "[1,∞)", "[-1,∞)", "[0,∞)"],
            "correct": "ℝ",
            "explanation": "f(x) prend toutes les valeurs réelles.",
            "level": "Tronc Commun",
            "topic": "Fonctions"
        }
    ],
    "Transformations": [
        {
            "question": "Translation de (1,2) par u(3,4) ?",
            "options": ["(4,6)", "(2,6)", "(3,2)", "(1,4)"],
            "correct": "(4,6)",
            "explanation": "(1+3, 2+4) = (4,6).",
            "level": "Tronc Commun",
            "topic": "Transformations"
        },
        {
            "question": "Symétrie de (2,1) par rapport à l’axe des x ?",
            "options": ["(2,-1)", "(-2,1)", "(1,2)", "(-2,-1)"],
            "correct": "(2,-1)",
            "explanation": "Symétrie sur x : (x,-y).",
            "level": "Tronc Commun",
            "topic": "Transformations"
        },
        # ... 18 more questions
        {
            "question": "Homothétie de (2,2) par rapport à (0,0), rapport 2 ?",
            "options": ["(4,4)", "(1,1)", "(2,2)", "(0,0)"],
            "correct": "(4,4)",
            "explanation": "(2×2, 2×2) = (4,4).",
            "level": "Tronc Commun",
            "topic": "Transformations"
        }
    ],
    "Produit scalaire": [
        {
            "question": "Produit scalaire de u(1,2) et v(3,4) ?",
            "options": ["11", "7", "5", "9"],
            "correct": "11",
            "explanation": "u·v = 1×3 + 2×4 = 11.",
            "level": "Tronc Commun",
            "topic": "Produit scalaire"
        },
        {
            "question": "u(1,0) et v(0,1) sont-ils orthogonaux ?",
            "options": ["Oui", "Non", "Parfois", "Jamais"],
            "correct": "Oui",
            "explanation": "u·v = 0, donc orthogonaux.",
            "level": "Tronc Commun",
            "topic": "Produit scalaire"
        },
        # ... 18 more questions
        {
            "question": "Norme de u(1,1) ?",
            "options": ["√2", "2", "1", "√3"],
            "correct": "√2",
            "explanation": "||u|| = √(1² + 1²) = √2.",
            "level": "Tronc Commun",
            "topic": "Produit scalaire"
        }
    ],
    "Géométrie dans l'espace": [
        {
            "question": "Distance entre A(1,0,0) et B(0,1,0) ?",
            "options": ["√2", "1", "2", "√3"],
            "correct": "√2",
            "explanation": "d = √((1-0)² + (0-1)² + (0-0)²).",
            "level": "Tronc Commun",
            "topic": "Géométrie dans l'espace"
        },
        {
            "question": "Vecteur AB si A(1,1,1), B(2,3,4) ?",
            "options": ["(1,2,3)", "(2,3,4)", "(1,1,1)", "(3,4,5)"],
            "correct": "(1,2,3)",
            "explanation": "AB = (2-1, 3-1, 4-1).",
            "level": "Tronc Commun",
            "topic": "Géométrie dans l'espace"
        },
        # ... 18 more questions
        {
            "question": "Norme de u(1,1,1) ?",
            "options": ["√3", "3", "√2", "1"],
            "correct": "√3",
            "explanation": "||u|| = √(1² + 1² + 1²) = √3.",
            "level": "Tronc Commun",
            "topic": "Géométrie dans l'espace"
        }
    ],
    "Statistiques": [
        {
            "question": "Moyenne de 2, 4, 6 ?",
            "options": ["4", "3", "5", "6"],
            "correct": "4",
            "explanation": "(2+4+6)/3 = 4.",
            "level": "Tronc Commun",
            "topic": "Statistiques"
        },
        {
            "question": "Médiane de 1, 3, 5, 7 ?",
            "options": ["4", "3", "5", "1"],
            "correct": "4",
            "explanation": "Valeur moyenne des termes centraux : (3+5)/2 = 4.",
            "level": "Tronc Commun",
            "topic": "Statistiques"
        },
        # ... 18 more questions
        {
            "question": "Écart-type de 1, 1, 1 ?",
            "options": ["0", "1", "2", "3"],
            "correct": "0",
            "explanation": "Variance = 0, donc écart-type = 0.",
            "level": "Tronc Commun",
            "topic": "Statistiques"
        }
    ]
}