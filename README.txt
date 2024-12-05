							Mini Blog Application - Présentation Générale
Ce projet est une Mini Application de Blog construite avec Django, un framework web en Python. Cette application permet à un utilisateur de créer, modifier, afficher et supprimer des articles de blog, ainsi que d'ajouter, modifier et supprimer des commentaires sur ces articles.

									Fonctionnalités principales :
	
	Gestion des Articles de Blog :
Créer un article : L'utilisateur peut créer un nouvel article de blog en remplissant un formulaire avec
un titre et un contenu.
Modifier un article : L'utilisateur peut modifier un article existant.
Supprimer un article : L'utilisateur peut supprimer un article de blog.
Voir un article : Chaque article peut être consulté individuellement, et les commentaires associés sont
également affichés.

	Gestion des Commentaires :
Ajouter un commentaire : Les utilisateurs peuvent ajouter des commentaires aux articles de blog.
Modifier un commentaire : Les utilisateurs peuvent éditer leurs commentaires existants.
Supprimer un commentaire : Les utilisateurs peuvent supprimer leurs commentaires.
	Navigation Intuitive :
Listes des articles : L'écran principal affiche tous les articles avec des options pour les voir, les
modifier ou les supprimer.
Détails de l'article : Lors de l'affichage d'un article, les commentaires associés sont également
visibles, avec des liens pour les ajouter, les modifier ou les supprimer.


									Structure du projet

	Models :
BlogPost : Représente un article de blog. Il contient un titre, un contenu et une date de création.
Comment : Représente un commentaire associé à un article de blog. Il contient l'auteur du commentaire
le texte du commentaire et une date de création.
	Views :
Liste des articles : Affiche une liste de tous les articles de blog.
Détails d'un article : Affiche un article spécifique ainsi que les commentaires associés.
Création, Modification, et Suppression des articles : Permet à l'utilisateur de créer, modifier et
supprimer des articles de blog.
Ajout, Modification, et Suppression des commentaires : Permet à l'utilisateur d'ajouter, modifier et
supprimer des commentaires pour un article.
	Templates :
Base Template : Un fichier HTML de base qui est étendu dans toutes les pages pour garantir la cohérence
de la mise en page.
Pages spécifiques : Les pages de création, modification, et suppression des articles et des
commentaires, ainsi que la page de liste des articles.

									Fonctionnement de l'application

			Page d'accueil :
Affiche tous les articles avec des boutons pour les voir, les éditer ou les supprimer.
Permet de créer un nouvel article via un bouton dédié.

			Page de détails d'un article :
Affiche le titre et le contenu de l'article.
Affiche les commentaires associés avec la possibilité de les éditer ou les supprimer.
Un formulaire permet d'ajouter de nouveaux commentaires à l'article.

			Page de création d'un article :
Un formulaire permet de saisir un titre et un contenu pour créer un nouvel article.

			Page de modification d'un article :
Permet de modifier un article existant avec les informations pré-remplies.

			Page de suppression d'un article :
Affiche un message de confirmation avant la suppression d'un article.

			Pages de gestion des commentaires :
Permet de créer, éditer et supprimer des commentaires associés aux articles de blog.


									Utilisation du projet 

	Créer un superutilisateur :
python manage.py createsuperuser


	Démarrer le serveur de développement :
python manage.py runserver


									Conclusion
Cette application est une base simple mais fonctionnelle pour un blog, avec des fonctionnalités
(Créer, Lire, Mettre à jour, Supprimer) pour les articles et les commentaires. 