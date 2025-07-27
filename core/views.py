from django.shortcuts import render

def accueil(request):
    images_slider = [
        {'src': 'images/danse_traditionnelle.jpg', 'alt': 'Danse traditionnelle'},
        {'src': 'images/chute_baba.jpg', 'alt': 'Chute Baba'},
        {'src': 'images/case_bangoulap.jpg', 'alt': 'case_Bangoulap'},
        {'src': 'images/patrimoine1.jpg', 'alt': 'traditionnelle'},
        {'src': 'images/patrimoine2.jpg', 'alt': 'traditionnelle'},
    ]

    village = {
        'geographie': 'Bangoulap est un village d’altitude (1 480 m) situé à 7 km au sud de Bangangté, le long de la route départementale D68. Il est entouré de reliefs culminant entre 1 299 m et 1 511 m, dont le Tchuifet (ou Meneu), Ntagni et Nanfam.',
        'origine': 'À l’origine, le territoire de Bangoulap était occupé par plusieurs familles autochtones. Vers 1550, Nzouami, venu de Baloumgoum, s’installa avec sa délégation dans ce village riche en gibier. Grâce à son charisme et ses talents de chasseur, il prit la tête de la communauté et fonda la dynastie Nzouami, qui comptera 24 rois. Après avoir affirmé sa domination, Nzouami déclara « Beuk Goum Lah » (« nous avons maîtrisé le village »), expression à l’origine du nom Bangoulap. Sous son règne, la communauté mena des guerres pour défendre et étendre son territoire.',
        'population': 'Le groupement de Bangoulap s’étend sur environ 86 km² et compte 2 475 habitants selon le recensement de 2013, ainsi qu’une diaspora estimée à 15 000 personnes. L’économie locale repose principalement sur l’agriculture, l’élevage et le petit commerce.',
        'chefferie': 'Bangoulap est l’une des six chefferies traditionnelles de 2ᵉ degré de l’arrondissement de Bangangté. Elle comprend 28 quartiers, dont certains subdivisés. Sa structure sociale suit le modèle bamiléké, avec un roi, neuf notables, des chefs de quartiers et la population. L’élite et la diaspora sont réunies au sein d’un comité de développement local.',
        'village': 'Bangoulap est l’un des sept groupements de la commune de Bangangté, composé de sept villages : Sagna, Madoum, Bonkeu, Badjuidgong, Nounfam, Kopda et Lafeng.',
        'culture': 'Bangoulap se caractérise par une grande diversité culturelle visible dans les éloges familiaux et les danses traditionnelles comme le Mangambeu, le Kesou, le Lah et le Ngou. La Fondation Gacha valorise ce patrimoine à travers des actions de développement et la reconstitution d’architectures traditionnelles.',
        'tourisme': 'Bangoulap offre de nombreuses attractions touristiques dispersées sur son territoire, telles que le palais royal, les lieux sacrés de Ntagni et de la chefferie, les chutes de Baba, les grottes de Madoua et les reliques de la forge de Lafeng. Ce village est réputé pour son accueil chaleureux et l’harmonie de sa population. La culture locale se manifeste notamment par des éloges familiaux (ndap) spécifiques à chaque quartier et des danses traditionnelles variées, dont le kessou, la danse fétiche des Bangoulap. Le plateau sacré de Ntagny est aussi un lieu emblématique, connu pour la veillée d’armes de la panthère du Nde avant la finale de la coupe du Cameroun en 1988.',
        'personnalite': 'Bangoulap est renommé pour ses nombreux artistes célèbres comme Marole Tchamba (la reine du Ben Skin), Pierre Didier Tchakounte, Foly Dirane, et Koutchouam Mbada (Reine mère du Ben Skin), ainsi que pour ses figures politiques et institutionnelles majeures, incluant ministres, députés, officiers de police et de l’armée, et anciens hauts responsables locaux.',
        'roi': {
            'message': "Chères filles et chers fils Bangoulap, Chers visiteurs, Bienvenue sur notre plate-forme. Je saisi cette occasion grâce aux nouvelles techniques d’informations et de communications, pour vous présenter notre groupement Bangoulap dans sa diversité. En visitant notre site web, vous aurez l’occasion de découvrir ce qui suit.",
        }
    }

    return render(request, 'core/accueil.html', {
        'images_slider': images_slider,
        'village': village,
    })

