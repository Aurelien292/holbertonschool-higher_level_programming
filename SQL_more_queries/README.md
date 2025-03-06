# SQL - More queries


### *INTRODUCTION* : 
Ce projet contient des scripts MySQL pour la gestion des utilisateurs, des bases de données et des tables. Il permet de pratiquer des concepts clés comme la création d’utilisateurs, la gestion des privilèges, et la manipulation des données à travers des requêtes SQL.

## Gestion des privilèges utilisateurs :

### *1. Lister les privilèges des utilisateurs user_0d_1 et user_0d_2*

Lister les privilèges de deux utilisateurs MySQL (user_0d_1 et user_0d_2) sur le serveur MySQL local.


*__Exemple__* : 
```
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
```

### *2. Création utilisateur et privilèges* 
#### Utilisateur avec tout les privilèges:
Créer un utilisateur user_0d_1 avec tous les privilèges sur le serveur MySQL. Si l'utilisateur existe déjà ,ne pas échouer . 

*__Exemple__* :
```
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
```
#### Utilisateur avec comme privilège SELECT dans la base de donnée hbtn_0d_2 :
*__Exemple__* :
```
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
```

### 3.Révoquer des privilèges

#### Révoquer des privilèges à un utilisateur, vous pouvez utiliser la commande REVOKE :

*__Exemple__* : 

Révoquer un privilège spécifique
```
REVOKE SELECT, INSERT ON nom_base.* FROM 'nom_utilisateur'@'localhost';
```
Cela supprime les privilèges SELECT et INSERT que l'utilisateur nom_utilisateur avait sur la base de données nom_base.

*__Exemple__* : 

Révoquer tous les privilèges
```
REVOKE ALL PRIVILEGES ON *.* FROM 'nom_utilisateur'@'localhost';
```
Cela révoque tous les privilèges de l'utilisateur nom_utilisateur sur toutes les bases de données et tables.

### 4.Exemple de privilège utilisateurs :


```
GRANT privilège_à_accorder ON hbtn_0d_2.* TO 'nom_utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';
```
*__Liste des principaux types de privilèges que vous pouvez attribuer à un utilisateur MySQL__* :

    ALL PRIVILEGES : Donne à l'utilisateur tous les privilèges disponibles pour une base de données ou un serveur.
    SELECT : Permet de lire des données dans les tables d'une base de données.
    INSERT : Permet d'insérer de nouvelles lignes dans une table.
    UPDATE : Permet de modifier les lignes existantes d'une table.
    DELETE : Permet de supprimer des lignes d'une table.
    CREATE : Permet de créer de nouvelles tables ou bases de données.
    DROP : Permet de supprimer des tables ou des bases de données.
    ALTER : Permet de modifier la structure des tables existantes (ex : ajouter des colonnes).
    GRANT OPTION : Permet à un utilisateur de donner (granter) ses privilèges à d'autres utilisateurs.
    INDEX : Permet de créer et de supprimer des index sur des tables.
    REFERENCES : Permet de créer des clés étrangères.
    EXECUTE : Permet d'exécuter des procédures stockées ou des fonctions.
    SHOW DATABASES : Permet de voir la liste des bases de données disponibles.


 ### 5.Privilèges globaux et spécifiques

Privilèges globaux : Si vous utilisez * . *, cela signifie que vous appliquez les privilèges à toutes les bases de données et toutes les tables du serveur MySQL.

*__Exemple__* :
```
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
```
Cela donne à l'utilisateur admin tous les privilèges sur toutes les bases de données et tables du serveur MySQL.
##  Importation d'un dump de base de données dans MySQL

L'importation d'un dump de base de données dans MySQL consiste à charger un fichier contenant les instructions SQL (généralement un fichier .sql) nécessaires à la création des tables, à l'insertion des données, et éventuellement à la création des utilisateurs ou à l'attribution de privilèges.

### Étapes détaillées :

__Se connecter à MySQL__ : 
```
mysql -u root -p
```
__Exécution de la commande pour importer le dump__ : 
```
mysql -u root -p < hbtn_0d_tvshows.sql
```
Permet de charger le fichier SQL dans MySQL. Vous devez la lancer dans le terminal . __<*Attention: dans l'exemple le fichier est dans le dossier de travail actuelle* >__

__Vérification__ : 

Une fois l'importation terminée, vous pouvez vérifier que la base de données a été correctement importée en vous connectant à MySQL et en vérifiant les bases de données disponibles 
```
mysql -u root -p
SHOW DATABASES;
```

## SQL : Quand les Tables Trouvent l'Amour et Se Lient pour Toujours !

Dans l'univers de SQL, les tables sont comme des entités indépendantes, mais parfois, elles doivent se connecter, s'associer et collaborer. Grâce aux clés étrangères et aux relations entre tables, les bases de données deviennent des systèmes interconnectés.

### Foreign Key (Clé étrangère) en SQL :
Elle permet de définir une relation entre deux tables, en garantissant l'intégrité des données. La clé étrangère est utilisée pour lier une colonne (ou un groupe de colonnes) dans une table à la clé primaire d'une autre table.

*__Exemple__* :

Imaginons les deux tables suivantes :

__Table_Parent__ :

Table_Parent avec une colonne id qui est la clé primaire (par exemple, des identifiants uniques pour chaque parent).
```
CREATE TABLE Table_Parent (
id INT PRIMARY KEY,
name VARCHAR(100)
);
```
__Table_Child avec la clé étrangère__ :
```
CREATE TABLE Table_Child (
id INT PRIMARY KEY,
parent_id INT,
CONSTRAINT fk_parent FOREIGN KEY (parent_id) REFERENCES Table_Parent(id)
);
```

Vous avez une table Table_Child avec une colonne __parent_id__ qui est la clé étrangère faisant référence à id dans la table Table_Parent. Cela signifie que chaque enregistrement dans __Table_Child__ doit avoir un __parent_id__ qui correspond à un id existant dans Table_Parent.

### EN BREF :

La contrainte de clé étrangère __fk_parent__ garantit que la colonne *__parent_id__* dans *__Table_Child__* fait référence à une valeur existante dans la colonne id de __Table_Parent__, ce qui permet de maintenir l'intégrité des données entre les deux tables.


## JOIN : L'Alliance Parfaite des Tables pour des Résultats Précis !

JOIN est une opération SQL utilisée pour combiner les lignes de deux ou plusieurs tables, en fonction d'une condition de correspondance. Cela permet de récupérer des données provenant de différentes tables et de les afficher sous une forme combinée.

### Types de JOIN :

* __INNER JOIN__ : Retourne les lignes lorsque les conditions de jointure sont remplies dans les deux tables.
* __LEFT JOIN__ (ou LEFT OUTER JOIN) : Retourne toutes les lignes de la table de gauche, même s'il n'y a pas de correspondance dans la table de droite.
* __RIGHT JOIN__ (ou RIGHT OUTER JOIN) : Retourne toutes les lignes de la table de droite, même s'il n'y a pas de correspondance dans la table de gauche.
* __FULL OUTER JOIN__ : Retourne toutes les lignes des deux tables, même si elles n'ont pas de correspondance.


*__Exemple__* :

Imaginons qu'un étudiant veuille savoir quels cours il suit. En utilisant un __INNER JOIN__ entre les tables *__students__* et *__courses__*, on relie les champs __student_id__ dans les deux tables. Cela permet de sélectionner les __students.name__ et __courses.course_name__, mais uniquement pour les étudiants qui sont inscrits dans des cours, c’est-à-dire là où il y a une correspondance d'__student_id__.

```
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.student_id = courses.student_id;
```
Dans cet exemple, nous utilisons un __INNER JOIN__ pour sélectionner les étudiants (students.name) et les cours (courses.course_name) où le student_id correspond dans les deux tables.

## Conclusion : 

Ce projet nous a permis de plonger dans l'univers de MySQL, en créant des utilisateurs, gérant des privilèges et administrant des tables. Nous avons aussi découvert comment les clés étrangères permettent aux tables de se lier comme des âmes sœurs, et comment le JOIN vient ajouter sa touche magique pour connecter plusieurs tables et révéler les trésors cachés des données. Bref, une base de données sans drame, mais avec de belles relations !
