from django.shortcuts import render

# Liste d’associations simulée (pas de BD)
associations_data = [
    {'id': 1, 'titre': 'ADB – Association pour le Développement de Bangoulap', 'description': 'L’ADB est l’organisation faîtière de toutes les initiatives de développement de la communauté Bangoulap, tant au village que dans la diaspora. Elle regroupe les fils et filles du village, autour d’objectifs communs : construction d’infrastructures (écoles, routes, centres de santé), actions sociales, soutien aux jeunes et préservation du patrimoine culturel. L’ADB organise des assemblées générales, journées culturelles et campagnes de solidarité. Elle fonctionne avec des comités locaux et des représentations à l’étranger (France, USA, Canada, etc.).'},
    {'id': 2, 'titre': 'ADB-France', 'description': 'Branche européenne de l’Association pour le Développement de Bangoulap. Elle regroupe les Bangoulapais vivant en France, engagés dans le développement de leur village d’origine. Elle mène des campagnes de levée de fonds, des actions culturelles (soirées, expositions, colloques) et collabore étroitement avec la chefferie et le comité central au Cameroun.'},
    {'id': 3, 'titre': 'ADB-Canada', 'description': 'Cette antenne regroupe la diaspora bangoulapaise vivant au Canada. Elle contribue activement aux projets du village, notamment dans les domaines de la santé, de l’éducation et de la culture. ADB-Canada participe à la coordination internationale des actions de l’ADB.'},
    {'id': 4, 'titre': 'ADB-USA', 'description': 'Représentation de la communauté Bangoulap basée aux États-Unis. En plus de soutenir les projets locaux, ADB-USA organise des événements culturels pour faire rayonner la culture bangoulapaise outre-Atlantique et renforcer les liens entre la diaspora et le village.'},
    {'id': 5, 'titre': 'Comité des Jeunes de Bangoulap (CJB)', 'description': 'Association dédiée à la mobilisation, à la formation et à la valorisation des jeunes du village. Le CJB s’implique dans l’organisation des tournois sportifs, les activités culturelles, la sensibilisation sociale, et la participation au développement communautaire. Il constitue une force dynamique pour préparer la relève.'},
    {'id': 6, 'titre': 'Association des Femmes Dynamiques de Bangoulap (AFDB)', 'description': 'Structure féminine engagée dans le développement local, la solidarité entre femmes, le soutien aux activités génératrices de revenus, et la participation active aux événements culturels et sociaux. L’AFDB promeut aussi la transmission des savoirs traditionnels et culinaires aux jeunes filles.'},
    {'id': 7, 'titre': 'Association des Élites Bangoulap (AEB)', 'description': 'Regroupe les cadres, universitaires, entrepreneurs et personnalités d’influence issus de Bangoulap. Leur mission est de mettre leur expertise, leurs réseaux et leurs moyens au service du développement du village. L’AEB joue souvent un rôle consultatif et stratégique dans les grands projets communautaires.'},
    {'id': 8, 'titre': 'Comité de Développement Local de Bangoulap (CDLB)', 'description': 'Instance de coordination sur le terrain, ce comité veille à l’exécution des projets votés par la communauté. Il agit en relais avec la chefferie, les partenaires techniques, les ONG et les bailleurs. Il supervise les chantiers, la maintenance des infrastructures, et les actions d’urgence.'},

]

def liste_associations(request):
    return render(request, 'associations/liste_associations.html', {'associations': associations_data})

def detail_association(request, id):
    association = next((a for a in associations_data if a['id'] == id), None)
    return render(request, 'associations/detail_association.html', {'association': association})
