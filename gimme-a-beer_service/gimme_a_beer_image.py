def gimme_a_beer_image(index):
    ''' INPUT: an int between 1 and 16 (inclusive) - for 
        returns of tuple of length 2 in the format: ('beer_name', 'url_for_externally_hosted_beer_image')
        e.g.: 
        ('old_ale', '<img src="https://i.ibb.co/zsz1bMS/english-style-old-ale.jpg" alt="english-style-old-ale" border="0" />')
        '''
        
    
    
    amber_ale = [
        'https://ibb.co/x5BKMDh',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/6sTc4mY/amber-ale.jpg" alt="amber-ale" border="0" /></a>'
    ]
    
    amber_lager = [
        'https://ibb.co/2jbj1vR',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/vJtJ63f/american-amber-lager.jpg" alt="american-amber-lager" border="0" /></a>'
    ]
    
    barley_wine = [
        'https://ibb.co/0KXGhBX',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/5k9RBY9/american-barley-wine.jpg" alt="american-barley-wine" border="0" /></a>'
    ]
    
    black_ale = [
        'https://ibb.co/ctxxn1v',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/pZnnFxP/american-black-ale.jpg" alt="american-black-ale" border="0" /></a>'
    ]
    
    brett = [
        'https://ibb.co/sbmknHV',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/17vh16m/american-brett.jpg" alt="american-brett" border="0" /></a>'
    ]
    
    brown_ale = [
        'https://ibb.co/CsZVbHN',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/jZ23yrB/american-brown-ale.jpg" alt="american-brown-ale" border="0" /></a>'
    ]
    
    cream_ale = [
        'https://ibb.co/Zm8pdWT',
        '<img src="https://i.ibb.co/TL8xcmh/american-cream-ale.jpg" alt="american-cream-ale" border="0" />'
    ]
    
    imperial_porter = [
        'https://ibb.co/ftbDRZv',
        '<img src="https://i.ibb.co/mtmNsd8/american-imperial-porter.jpg" alt="american-imperial-porter" border="0" />'
    ]
    
    baltic_style_porter = [
        'https://ibb.co/KbvNKb1',
        '<img src="https://i.ibb.co/LY7QNYG/baltic-style-porter.jpg" alt="baltic-style-porter" border="0" />'
    ]
    
    belgian_style_dubbel = [
        'https://ibb.co/p0bJ4wD',
        '<img src="https://i.ibb.co/HFBnG4v/belgian-style-dubbel.jpg" alt="belgian-style-dubbel" border="0" />'
    ]
    
    belgian_style_fruit_lambic = [
        'https://ibb.co/v1bcsh6',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/PxRrTMv/belgian-style-fruit-lambic.jpg" alt="belgian-style-fruit-lambic" border="0" /></a>'
    ]
    
    berliner_style_weisse = [
        'https://ibb.co/2nXxZ1L',
        '<img src="https://i.ibb.co/K0CdKpQ/berliner-style-weisse.jpg" alt="berliner-style-weisse" border="0" />'
    ]
    
    biere_de_garde = [
        'https://ibb.co/T48sGYD',
        '<img src="https://i.ibb.co/fkpsWqV/biere-de-garde.jpg" alt="biere-de-garde" border="0" />'
    ]
    
    bohemian_style_pilsener = [
        'https://ibb.co/2dhVFD7',
        '<img src="https://i.ibb.co/x6L92pS/bohemian-style-pilsener.jpg" alt="bohemian-style-pilsener" border="0" />'
    ]

    cream_ale = [
        'https://ibb.co/Zm8pdWT',
        '<img src="https://i.ibb.co/TL8xcmh/american-cream-ale.jpg" alt="american-cream-ale" border="0" />'
    ]
    
    english_style_old_ale = [
        'https://ibb.co/qBvz9SR',
        '<img src="https://i.ibb.co/zsz1bMS/english-style-old-ale.jpg" alt="english-style-old-ale" border="0" />'
    ]
    
    dunkelweizen = [
        'https://ibb.co/FgWzmV4',
        '<img src="https://i.ibb.co/bz3XQJ5/german-style-dunkelweizen.jpg" alt="german-style-dunkelweizen" border="0" />'
    ]
    
    marzen_oktoberfest = [
        'https://ibb.co/jb9rQm8',
        '<a href="https://imgbb.com/"><img src="https://i.ibb.co/2W0kCxF/german-style-marzen-oktoberfest.jpg" alt="german-style-marzen-oktoberfest" border="0" /></a>'
    ]

    beers = [
        amber_ale,
        amber_lager,
        barley_wine,
        black_ale,
        brett,
        brown_ale,
        cream_ale,
        imperial_porter,
        baltic_style_porter,
        belgian_style_dubbel,
        belgian_style_fruit_lambic,
        berliner_style_weisse,
        biere_de_garde,
        bohemian_style_pilsener,
        english_style_old_ale,
        dunkelweizen,
        marzen_oktoberfest
    ]
    
    beers_names = [
        "amber_ale",
        "amber_lager",
        "barley_wine",
        "black_ale",
        "brett",
        "brown_ale",
        "cream_ale",
        "imperial_porter",
        "baltic_style_porter",
        "belgian_style_dubbel",
        "belgian_style_fruit_lambic",
        "berliner_style_weisse",
        "biere_de_garde",
        "bohemian_style_pilsener",
        "english_style_old_ale",
        "dunkelweizen",
        "marzen_oktoberfest"
    ]
    
    random_number = index
    random_beer_name = beers_names[random_number]
    beer_image_URL = beers[random_number]
    
    return (random_beer_name, beer_image_URL[1])
    
if __name__ == "__main__":
    print(gimme_a_beer_image())