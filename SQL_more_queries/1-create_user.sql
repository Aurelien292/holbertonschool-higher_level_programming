-- Crée l'utilisateur user_0d_1 avec le mot de passe user_0d_1_pwd, si cet utilisateur n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password_0d_1_pwd';

-- Accorde tous les privilèges à l'utilisateur user_0d_1 sur toutes les bases de données et tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Applique immédiatement les changements
FLUSH PRIVILEGES;