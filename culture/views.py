from django.shortcuts import render

def danses(request):
    danses = [
        {'nom': 'Tso (ou Tsotscho) – La Danse des Braves', 'description': 'Cette danse guerrière est réservée aux notables, chefs et guerriers. Elle symbolise la force, le courage et la dignité. Accompagnée de tambours puissants, elle impressionne par son rythme intense et les tenues majestueuses portées par les danseurs. Elle est souvent présentée lors des grandes cérémonies royales.'},
        {'nom': 'Ben Skin – La Danse Populaire Moderne', 'description': 'Très connue dans l’Ouest Cameroun, le Ben Skin est aujourd’hui une véritable identité musicale et dansante pour Bangoulap, grâce à des artistes locaux comme Marole Tchamba et Koutchouam Mbada. Cette danse énergique et festive, souvent accompagnée de paroles satiriques ou engagées, est très prisée des jeunes et anime les fêtes du village.'},
        {'nom': 'Méngou – La Danse des Femmes', 'description': 'Le Méngou est une danse rituelle principalement exécutée par les femmes. Elle célèbre la fertilité, la royauté et les traditions familiales. Les femmes dansent en groupe, avec des gestes élégants et rythmés, lors des cérémonies de mariage, d’hommage ou d’intronisation.'},
        {'nom': 'Nkù – La Danse des Initiés', 'description': 'Le Nkù est lié aux rites de passage et à l’initiation. Son nom vient des tambours traditionnels utilisés pour rythmer la danse. Elle est souvent pratiquée lors de funérailles ou de célébrations rituelles importantes et porte une grande charge spirituelle.'},
        {'nom': 'Danses Masquées et Secrètes', 'description': 'Certaines danses à Bangoulap sont strictement réservées aux membres des sociétés secrètes (comme le Kwifo). Elles sont liées aux cultes ancestraux, à la justice traditionnelle et à la protection spirituelle du village. Ces danses se font souvent avec des masques sacrés, et leur contenu reste mystérieux pour les non-initiés.'},
    ]
    return render(request, 'culture/danses.html', {'danses': danses})

def festivals(request):
    festivals = [
        {'nom': 'La Fête du Roi (Fo Bangoulap)', 'date': 'Décembre ou Janvier (fin d’année ou début d’année)', 'description': 'Organisée généralement une fois par an, cette grande célébration est dédiée au chef traditionnel (Fo) de Bangoulap. Elle marque son intronisation, son anniversaire ou une commémoration symbolique. C’est un moment fort où les notables, les chefs de quartiers, les dignitaires et la population se rassemblent autour du trône pour renouveler leur fidélité au roi. Danses rituelles, offrandes, discours coutumiers et démonstrations guerrières sont au programme.'},
        {'nom': 'La Fête des Ancêtres (Rituels de mémoire)', 'date': 'Entre Juin et Août (en saison sèche intermédiaire)', 'description': 'C’est une période consacrée au culte des ancêtres. Chaque famille ou lignage organise une cérémonie de commémoration pour ses morts. Des rituels de purification, des prières collectives et des danses symboliques comme le Tsotscho sont organisés pour honorer les esprits et renforcer les liens entre vivants et ancêtres.'},
        {'nom': 'Festival du Patrimoine et des Arts de Bangoulap', 'date': 'Août ou pendant les vacances scolaires (Juillet-Août)', 'description': 'Ce festival met en lumière les richesses culturelles de Bangoulap : danses, chants, artisanat, gastronomie, contes… C’est une vitrine pour les talents locaux et un lieu de transmission culturelle pour les jeunes. Il est souvent organisé en lien avec les associations de la diaspora ou les jeunes du village.'},
        {'nom': 'Funérailles Traditionnelles (Rites de passage)', 'date': 'Toute l’année, surtout de Décembre à Mars (saison sèche)', 'description': 'À Bangoulap, les funérailles ne sont pas que des moments de deuil, ce sont aussi des rituels culturels codifiés. Elles comprennent des veillées de chants, des danses traditionnelles, des offrandes, et parfois des démonstrations de sociétés secrètes. Elles permettent d’accompagner le défunt vers le monde des ancêtres avec honneur.'},
        {'nom': 'Journées de Réflexion et de Développement (JRD Bangoulap)', 'date': 'Fin Juillet ou Août (pendant les vacances en été)', 'description': 'Ces journées, souvent organisées par les élites et associations de développement, permettent d’échanger sur les défis et projets du village (éducation, santé, patrimoine…). Elles sont généralement accompagnées de animations culturelles, expositions et concerts.'},
        {'nom': 'La Fête des Ancêtres (Rituels de mémoire)', 'date': 'Octobre', 'description': 'Événement littéraire communautaire.'},
        {'nom': 'Rites d’Initiation & Cérémonies Secrètes', 'date': 'Variable – souvent entre Janvier et Mai', 'description': 'Ces rites sont réservés aux initiés (hommes ou femmes), selon des calendriers internes propres aux sociétés traditionnelles (comme le Kwifo). Ces événements ont un caractère sacré et discret, et marquent des passages de vie importants (passage à l’âge adulte, accession au rang de notable…).'},
    ]
    return render(request, 'culture/festivals.html', {'festivals': festivals})

def structure(request):
    structure = {
        'roi': 'Sa Majeste YONKEU KUIKA JEAN, Roi de BANGOULAP',
        'organismes': ['Organismes Locaux de Développement', 'Organismes Traditionnels', 'Organismes Socio-éducatifs', 'Organismes Publics ou Institutionnels'],
    }
    return render(request, 'culture/structure.html', {'structure': structure})
