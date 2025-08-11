from django.shortcuts import render

def presentation_du_CODEBA(request):
    contenu = {
        'nom': 'Presentation du CODEBA',
        'description': """
            ASIEL est un produit de ALEN SARL qui est une entreprise dynamique évoluant globalement dans les domaines de la gestion, de la négociation et du commerce.
            Soucieuse de s’adapter aux exigences du monde contemporain ; elle a initié un projet ambitieux qu’est ASIEL’. Ce service a pour vocation de mettre en lumière les commerces et surtout les trésors du Cameroun. A travers sa plateforme, l’entreprise entend valoriser les entreprises et commerces de notre environnement en mettant en évidence toute entreprise commerciale dont les valeurs ont été vérifiées. Ces valeurs devront cadrer avec une vision communautaire, une aspiration à se déployer valablement sur le marché national voire international ainsi qu’une responsabilité sociale effective.
                    """,
    }
    return render(request, 'CODEBA/presentation_du_CODEBA.html', {'contenu': contenu})

def activite_du_CODEBA(request):
    contenu = {
        'nom': 'Activite de CODEBA',
        'description': """
            C’est ainsi que ASIEL sera pensé et conçu par nous pour offrir à notre environnement une expérience de e-market et de livraisons purement professionnels et flexibles. Il se déploie alors dans les différents services que sont :

            ASIEL e-market ayant pour but de répondre aux divers besoins des consommateurs tout en faisant la promotion des producteurs et des entrepreneurs locaux. L’application permettra aux clients de procéder à leurs achats en toute sérénité avec la sélection et la constitution faciles de leurs paniers, l’enregistrement et le suivi en toute transparence de leurs commandes.
            ASIEL delivery (Livraison standard) qui est indépendant du e-market et vous permet d’acheminer vos commandes et colis constitués sur le e-market ou pas, jusqu’à vous. Ici nous offrons un service de livraison standard (à partir de 4 heures après la commande)
            SUPER ASIEL (Livraison Express) qui lui non plus n’est pas conditionné par l’achat sur l’application. Ce service vous donne droit à une livraison qui répond parfaitement à vos besoins urgents avec des délais beaucoup plus courts que ceux du service classique
                    """,
    }
    return render(request, 'CODEBA/activite_du_CODEBA.html', {'contenu': contenu})

