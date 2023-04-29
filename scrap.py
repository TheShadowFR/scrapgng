# ensure you have Python (3  or latest)
# ensure you have pip installer
from Studyrama import Studyrama
from Scrapper import Scrapper


instance = Studyrama(
    'https://www.studyrama.com',
    "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page=",
    "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page=",
    1
    )

scrapyCoco = Scrapper(instance, 'links.csv', 'contacts.csv','errors.csv')

scrapyCoco.exec()

print("Done")


# TODO
# Laison Api Chat GPT : 
# Tu es un prospecteur en tant que professeur d'informatique, tu propose tes services a une ecole pour la formation intitulée "LA COMMUNICATION IMPRIMÉE ET DES BIOMATÉRIAUX” : dans un mail personnalisé en fonction de la description suivante : "Grenoble INP - Pagora dispense sur 3 années une formation scientifique et technique spécialisée et de haut niveau, sanctionnée par un diplôme d’Ingénieur, avec 2 spécialisations au choix : Ingénierie de la Fibre et des Biomatériaux ou Ingénierie de la Communication Imprimée. Ces 3 années comportent de nombreux projets offrant aux élèves ingénieurs la possibilité d’utiliser des outils industriels de pointe. La formation d’ingénieur de Grenoble INP - Pagora, réalisable en cursus étudiant ou apprentissage, permet également aux élèves de développer des compétences en sciences économiques, en management de l’entreprise, sur les aspects de la responsabilité sociétale et du développement durable." , peux-tu imaginer le corp du mail que tu envoies 

# "Bonjour [nom du destinataire],

# Je suis [votre nom] et je souhaiterais proposer mes services en tant que professeur d'informatique pour la formation "LA COMMUNICATION IMPRIMÉE ET DES BIOMATÉRIAUX" dispensée à Grenoble INP - Pagora.

# J'ai [X années] d'expérience dans le domaine de l'informatique et je suis convaincu que ma formation et mon expérience peuvent être bénéfiques pour les élèves ingénieurs inscrits dans ce programme. J'ai déjà enseigné à des étudiants dans des programmes similaires et j'ai pu constater leur passion et leur détermination pour acquérir des connaissances en informatique.

# Je suis particulièrement intéressé par les nombreux projets proposés tout au long des 3 années de cette formation, qui offrent aux étudiants la possibilité d'utiliser des outils industriels de pointe. Je suis persuadé que mon expérience en tant qu'enseignant et mon expertise dans les technologies de pointe peuvent contribuer à enrichir les projets des élèves ingénieurs et à les aider à développer des compétences clés en informatique.

# Je suis également convaincu de l'importance des compétences en sciences économiques, en management de l'entreprise et en développement durable, et je suis prêt à travailler en collaboration avec d'autres enseignants pour aider les élèves à développer ces compétences.

# Je serais ravi de discuter plus en détail de ma proposition avec vous et de répondre à toutes vos questions. Si vous êtes intéressé, n'hésitez pas à me contacter pour convenir d'un rendez-vous.

# Je vous remercie pour votre temps et votre considération.

# Cordialement,

# [votre nom]"




# Tu es un prospecteur en tant que professeur d'informatique, tu propose tes services a une ecole pour la formation intitulée “BACHELOR DÉVELOPPEUR WEB” : dans un mail personnalisé en fonction de la description suivante : Le Bachelor développeur web a pour objectif d’acquérir les compétences en développement web & mobile : optimisation des ressources client-serveur, gestion des données, compatibilité multi-device, travail avec les équipes créatives. , peux-tu imaginer le corp du mail que tu envoies 




# Bonjour [nom du destinataire],

# Je suis [votre nom] et je souhaiterais proposer mes services en tant que professeur d'informatique pour la formation "BACHELOR DÉVELOPPEUR WEB" que vous proposez.

# Avec [X années] d'expérience en développement web et mobile, je suis convaincu que je peux apporter une contribution significative à votre programme. Je suis passionné par l'enseignement et j'ai déjà eu l'occasion de travailler avec des étudiants de tous niveaux.

# Je suis particulièrement intéressé par l'objectif de votre programme, qui est d'acquérir des compétences en développement web et mobile. En tant que professionnel du développement web, je suis convaincu de l'importance d'optimiser les ressources client-serveur, de gérer efficacement les données, de garantir la compatibilité multi-device et de travailler en collaboration avec les équipes créatives pour produire des résultats de qualité.

# Je suis persuadé que ma formation et mon expérience dans le domaine de l'informatique peuvent être bénéfiques pour les étudiants inscrits dans votre programme. Mon approche pédagogique se base sur une combinaison de théorie et de pratique, en utilisant des exemples concrets pour aider les élèves à comprendre les concepts clés. Je suis également en mesure d'utiliser les outils les plus récents pour garantir que mes étudiants sont prêts pour les défis futurs dans le domaine de la technologie.

# Je serais ravi de discuter plus en détail de ma proposition avec vous et de répondre à toutes vos questions. Si vous êtes intéressé, n'hésitez pas à me contacter pour convenir d'un rendez-vous.

# Je vous remercie pour votre temps et votre considération.

# Cordialement,

# [votre nom]