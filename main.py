from mkdocs_macros.context import fix_url


def define_env(env):
    @env.macro
    def image(url: str, alt: str = "", class_name: str = "") -> str:
        url = fix_url(url)
        return f'<img src="{url}" alt="{alt}" class="{class_name}">'

    @env.macro
    def internal_link(url: str, text: str, class_name: str = "") -> str:
        url = env.conf["site_url"] + url + ".html"
        return f'<a href="{url}" class="{class_name}">{text}</a>'

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
        {"logo_url": "assets/images/logos/acua.png", "name": "ACUA"},
        {"logo_url": "assets/images/logos/asaps.jpg", "name": "ASAPS"},
        {
            "logo_url": "assets/images/logos/isf.jpg",
            "name": "Ingeniería Sin Fronteras",
        },
        {"logo_url": "assets/images/logos/aecid.jpg", "name": "AECID"},
        {
            "logo_url": "assets/images/logos/xunta.png",
            "name": "Cooperación Galega",
        },
    ]

    env.variables.contacts_data = [
        {
            "name": "ACUA",
            "email": "email@email.com",
            "phone": "+503 2314 0636",
            "location": "Barrio la Cruz, Avenida Monseñor Romero #31. </br> Zaragoza, La Libertad, El Salvador",
            "url": "https://www.acua.org.sv/",
            "logo_url": "assets/images/logos/acua.png",
        },
        {
            "name": "ASAPS",
            "email": "email@email.com",
            "phone": "+34 123 456 789",
            "location": "San Salvador, El Salvador",
            "url": "https://www.acua.org.sv/",
            "logo_url": "assets/images/logos/asaps.jpg",
        },
        {
            "name": "iCarto",
            "email": "info@icarto.es",
            "phone": "+34 881 927 808",
            "location": "C/ Rafael Alberti, 13 – 1ºD. </br>15008 A Coruña, España",
            "url": "https://icarto.es",
            "logo_url": "assets/images/logos/icarto.png",
        },
    ]
