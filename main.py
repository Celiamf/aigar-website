def define_env(env):
    env.variables.stats_items = [
        {"icon": "download", "value": "1000", "label": "Descargas"},
        {"icon": "communities", "value": "10", "label": "Comunidades"},
        {"icon": "people", "value": "1000", "label": "Usuarios/as"},
    ]

    env.variables.testimonials_data = [
        {
            "img_url": "https://xsgames.co/randomusers/avatar.php?g=female",
            "name": "Ana García",
            "title": "ACUA",
            "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officia ad accusantium eos quo optio eaque repellendus provident placeat.",
        },
        {
            "img_url": "https://xsgames.co/randomusers/avatar.php?g=male",
            "name": "Carlos Rodríguez",
            "title": "ASAPS",
            "content": "Quidem, numquam quae neque repellendus eum perspiciatis molestias qui consectetur voluptatibus labore.",
        },
    ]

    env.variables.funders_data = [
        {"logo_url": "assets/images/funders_logos/acua.png", "name": "ACUA"},
        {"logo_url": "assets/images/funders_logos/asaps.jpg", "name": "ASAPS"},
        {
            "logo_url": "assets/images/funders_logos/isf.jpg",
            "name": "Ingeniería Sin Fronteras",
        },
        {"logo_url": "assets/images/funders_logos/aecid.jpg", "name": "AECID"},
        {
            "logo_url": "assets/images/funders_logos/xunta.png",
            "name": "Cooperación Galega",
        },
    ]
