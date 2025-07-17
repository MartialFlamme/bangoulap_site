from django.shortcuts import render

def origines(request):
    contexte = {
        'texte': """
    Le village Bangoulap, situé dans la région de l’Ouest Cameroun, plus précisément dans le département des Hauts-Plateaux, est une chefferie traditionnelle bamiléké qui remonte à plusieurs siècles. Ce village fait partie des anciennes communautés royales de la région, connues pour leur organisation sociale rigoureuse, leur attachement aux rites coutumiers et leur patrimoine culturel exceptionnel.

Selon les traditions orales transmises de génération en génération, Bangoulap aurait été fondé entre le XVIIe et le XVIIIe siècle par un prince issu d’une grande chefferie voisine — probablement Baleng, Bahouan ou Bamendjou — à la suite d’un conflit de succession, d’une quête d’indépendance ou d’un mandat spirituel. Accompagné de ses partisans, il se serait installé dans une zone fertile, entourée de collines verdoyantes et de rivières, pour y établir une nouvelle communauté, désormais autonome. Il y érigea une chefferie, cœur du pouvoir et de l'identité de Bangoulap.

Le nom "Bangoulap" aurait des origines linguistiques dans la langue bamiléké, où le préfixe "Ba-" signifie "les gens de". Le mot "Ngoulap" pourrait désigner un lieu sacré, un ancêtre fondateur ou une entité protectrice. Ainsi, Bangoulap peut être interprété comme "le peuple de Ngoulap" ou "ceux du territoire protégé". Le sens exact varie selon les clans et les gardiens de la tradition.

Depuis sa fondation, Bangoulap a connu une succession de rois (appelés Fo), qui incarnent à la fois l’autorité politique, la sagesse spirituelle et la continuité culturelle. Le Fo de Bangoulap est le garant de l’ordre social, du respect des ancêtres et des rites. Il est entouré de notables, de chefs de quartiers et de dignitaires traditionnels qui l’assistent dans la gestion des affaires du village. Cette monarchie coutumière forme la base de l’organisation politique du village jusqu’à aujourd’hui.

Le village est divisé en quartiers ou secteurs, chacun administré par un chef de quartier. Ces quartiers ont souvent des histoires ou des spécialisations propres (artisanat, rites, lignages). De plus, Bangoulap abrite plusieurs sociétés secrètes traditionnelles, telles que le Kwifo (justice mystique), le Kom (initiation masculine), et le Mélim (organisation rituelle féminine). Ces sociétés jouent un rôle fondamental dans la transmission des valeurs, la préservation des lois coutumières et la protection spirituelle du village.

Au fil des siècles, Bangoulap a su résister à la colonisation, préserver son identité face aux mutations modernes, et valoriser son patrimoine à travers des danses, des rituels, des funérailles traditionnelles et des festivals. Aujourd’hui encore, le village organise chaque année des fêtes royales, des journées culturelles et des rencontres de la diaspora, notamment sous l’égide de l’Association pour le Développement de Bangoulap (ADB) et ses antennes en France, au Canada, aux États-Unis et ailleurs.

Bangoulap est ainsi un village où l’histoire, la royauté, les croyances ancestrales et la modernité cohabitent en harmonie. Il continue de jouer un rôle important dans la région comme centre de mémoire vivante, de culture et de cohésion sociale pour tous ceux qui s’identifient à son nom.
        """
    }
    return render(request, 'histoire/origines.html', contexte)

def sites_touristiques(request):
    sites = [
        {'nom': 'Le Palais Royal de Bangoulap', 'description': 'Centre spirituel et politique du village, la chefferie traditionnelle abrite la case du Fo (roi), les sanctuaires ancestraux, et la cour où se tiennent les cérémonies et danses rituelles.'},
        {'nom': 'Le Bois Sacré', 'description': 'Plusieurs placettes du village accueillent les danses rituelles telles que le Tso (danse des guerriers), le Méngou (danse féminine), et le Ben Skin, danse festive populaire.'},
        {'nom': 'Les Sites de Danses Traditionnelles', 'description': 'Plusieurs placettes du village accueillent les danses rituelles telles que le Tso (danse des guerriers), le Méngou (danse féminine), et le Ben Skin, danse festive populaire.'},
        {'nom': 'Sources d’Eau Sacrées et Cascades', 'description': 'Certaines sources naturelles sont considérées comme sacrées et curatives, liées à des légendes locales. Elles sont accessibles avec un guide et offrent un cadre naturel paisible.'},
        {'nom': 'Rochers et Collines de Mémoire', 'description': 'Ces lieux symboliques ont servi de refuges historiques ou d’espaces sacrés et offrent de magnifiques panoramas sur la région environnante.'},
        {'nom': 'Habitat Traditionnel Bamiléké', 'description': 'Maisons en banco aux toits bas, témoignages de l’architecture précoloniale, encore préservées par certaines familles qui acceptent les visites.'},
        {'nom': 'Ateliers d’Artisanat Local', 'description': 'Sculpture, tissage, fabrication d’instruments de musique : plusieurs artisans ouvrent leurs ateliers pour découvrir le savoir-faire traditionnel.'},
        {'nom': 'Anciennes Missions Religieuses et Églises Historiques', 'description': 'Édifices catholiques et protestants construits dans les années 1950–1960, témoignant de l’histoire religieuse et de la cohabitation culturelle du village.'},
    ]
    return render(request, 'histoire/sites_touristiques.html', {'sites': sites})
