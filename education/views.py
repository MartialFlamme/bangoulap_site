from django.shortcuts import render

def projets_educatifs(request):
    projets = [
        {'titre': 'Ateliers numériques pour les jeunes', 'description': 'Initiation à l’informatique et à Internet dans les écoles.'},
        {'titre': 'Éducation civique communautaire', 'description': 'Formations sur la citoyenneté et l’engagement local.'},
    ]
    return render(request, 'education/projets_educatifs.html', {'projets': projets})

def academie_hoteliere(request):
    contenu = {
        'nom': 'Académie Hôtelière de Bangoulap',
        'description': """
            Ce centre de formation vise à préparer les jeunes aux métiers de l’hôtellerie, de la restauration
            et du tourisme rural, en valorisant les produits et coutumes locales.
        """,
        'image': 'images/education/academie.jpg'
    }
    return render(request, 'education/academie_hoteliere.html', {'contenu': contenu})

