from dataclasses import dataclass

from manim import *


class TimedAnimation:    
    def __init__(self, component: Text | ImageMobject, length: int):
        if isinstance(component, Text):
            self.animation = Write(component)
        elif isinstance(component, ImageMobject):
            self.animation = FadeIn(component)
        else:
            raise ValueError("Component must be a Text or ImageMobject")
        self.component = component
        self.length = length


@dataclass
class CardData:
    title: str
    length: int | float
    timed_animations: list[TimedAnimation]


def build_image(path: str, size: int | float = 5):
    image = ImageMobject(path)
    image.width = size
    image.height = size
    return image


textos = [
    CardData(
        "Socios clave",
        58,
        [
            TimedAnimation(Text("Proveedores de materia prima", font_size=46), length=12),
            TimedAnimation(build_image("assets/raw-materials.png", size=2.8), length=12),
            TimedAnimation(Text("Empresas de logística", font_size=46), length=12),
            TimedAnimation(build_image("assets/logistic.png", size=2.8), length=12),
            TimedAnimation(Text("Proveedores de software", font_size=46), length=12),
            TimedAnimation(build_image("assets/software.png", size=2.8), length=12),
            TimedAnimation(Text("Centros de I+D", font_size=46), length=12),
            TimedAnimation(build_image("assets/research-and-development.png", size=2.8), length=12)
        ],
    ),
    CardData(
        "Actividades",
        52,
        [
            TimedAnimation(Text("Sistemas de carrocería   ", font_size=50), length=10),
            TimedAnimation(Text("Depósitos", font_size=50), length=10),
            TimedAnimation(Text("Energías renovables", font_size=50), length=10),
            TimedAnimation(Text("I+D de nuevos materiales", font_size=50), length=10),
            TimedAnimation(build_image("assets/car.png", size=3.5), length=10),
        ],
    ),
    CardData(
        "Recursos",
        43,
        [
            TimedAnimation(Text("Fábricas por todo el mundo", font_size=45), length=8),
            TimedAnimation(Text("Equipos de diseño y desarrollo", font_size=45), length=8),
            TimedAnimation(Text("Empleados altamente cualificados", font_size=45), length=8),
            TimedAnimation(Text("Patentes y propiedad intelectual", font_size=45), length=8),
            TimedAnimation(build_image("assets/industry.png", size=3.5), length=8),
        ],
    ),
    CardData(
        "Propuesta de valor",
        53,
        [
            TimedAnimation(Text("Producción a gran escala", font_size=45), length=9),
            TimedAnimation(Text("Máxima calidad y fiabilidad", font_size=45), length=9),
            TimedAnimation(Text("Sistemas eficientes y reciclables", font_size=45), length=9),
            TimedAnimation(Text("Liderazgo en investigación", font_size=45), length=9),
            TimedAnimation(Text("Compromiso de sostenibilidad", font_size=45), length=9),
            TimedAnimation(build_image("assets/value.png"), length=9),
        ],
    ),
    CardData(
        "Relación con clientes",
        48,
        [
            TimedAnimation(Text("Colaboración estrecha", font_size=50), length=9),
            TimedAnimation(Text("Contratos a largo plazo", font_size=50), length=9),
            TimedAnimation(Text("Asistencia técnica", font_size=50), length=9),
            TimedAnimation(Text("Programas de fidelización", font_size=50), length=9),
            TimedAnimation(build_image("assets/partner.png", size=3.5), length=9),
        ],
    ),
    CardData(
        "Canales de venta",
        43,
        [
            TimedAnimation(Text("Venta directa a fabricantes", font_size=50), length=10),
            TimedAnimation(Text("Indirecta a distribuidores", font_size=50), length=10),
            TimedAnimation(Text("Venta online", font_size=50), length=10),
            TimedAnimation(build_image("assets/selling-channels.png", size=3.5), length=10),
        ],
    ),
    CardData(
        "Clientes",
        13,
        [
            TimedAnimation(Text("Grupos automovilísticos", font_size=46), length=2),
            TimedAnimation(build_image("assets/fast-car.png", size=3.5), length=2),
            TimedAnimation(Text("Empresas de logística", font_size=46), length=2),
            TimedAnimation(build_image("assets/car-fix.png", size=3.5), length=3),
            TimedAnimation(Text("Particulares", font_size=46), length=3),
            TimedAnimation(build_image("assets/clients.png", size=3.5), length=2),
        ],
    ),
    CardData(
        "Costes operativos",
        45,
        [
            TimedAnimation(Text("Materias primas", font_size=55), length=7),
            TimedAnimation(Text("Maquinaria", font_size=55), length=7),
            TimedAnimation(Text("Energéticos", font_size=55), length=7),
            TimedAnimation(Text("Personal (1700 en España)", font_size=55), length=7),
            TimedAnimation(Text("Logística", font_size=55), length=7),
            # TimedAnimation(build_image("assets/logistic.png"), length=7),
        ],
    ),
    CardData(
        "Fuentes de ingresos",
        35,
        [
            TimedAnimation(Text("Ventas de productos", font_size=55), length=7),
            TimedAnimation(Text("Recambios", font_size=55), length=7),
            TimedAnimation(Text("Sistemas de energía limpia", font_size=55), length=7),
            TimedAnimation(Text("Propiedad intelectual", font_size=55), length=7),
            # TimedAnimation(build_image("assets/value.png"), length=7),
        ],
    ),
]


class CardObject(Group):
    def __init__(self, card_data: CardData, width: int, height: int, background_color: ManimColor):
        Group.__init__(self)
        self.card_data = card_data
        self.width = width
        self.height = height
        self.background_color = background_color

        self.title = Text(card_data.title, font_size=75)
        self.title.set_z_index(2)

        self.card_background = Rectangle(width=width, height=height, color=background_color, fill_opacity=0)

        self.title.move_to(self.card_background.get_top(), UP)
        self.title.shift(DOWN * 0.5)

        underline_title = Underline(self.title)
        self.add(self.title, underline_title, self.card_background)

        self.content = Group()
        self.content.set_z_index(2)

    def show_background(self):
        return self.card_background.animate.set_opacity(0.3)

    def add_content(self):
        self.add(self.content)

    def add_component(self, component: Text | ImageMobject):
        self.content.add(component)
        self.content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        self.content.next_to(self.title, DOWN, buff=0.7)


class BusinessModelCanvas(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key_partners = CardObject(card_data=textos[0], width=10, height=20, background_color=BLUE)
        self.key_activities = CardObject(card_data=textos[1], width=10, height=10, background_color=BLUE)
        self.key_resources = CardObject(card_data=textos[2], width=10, height=10, background_color=BLUE)
        self.value_propositions = CardObject(card_data=textos[3], width=10, height=20, background_color=RED)
        self.customer_relationships = CardObject(card_data=textos[4], width=10, height=10, background_color=ORANGE)
        self.channels = CardObject(card_data=textos[5], width=10, height=10, background_color=ORANGE)
        self.customers = CardObject(card_data=textos[6], width=10, height=20, background_color=ORANGE)
        self.cost_structure = CardObject(card_data=textos[7], width=25, height=8, background_color=GREEN)
        self.revenue_streams = CardObject(card_data=textos[8], width=25, height=8, background_color=GREEN)

        self.cards = [
            self.key_partners,
            self.key_activities,
            self.key_resources,
            self.value_propositions,
            self.customer_relationships,
            self.channels,
            self.customers,
            self.cost_structure,
            self.revenue_streams,
        ]
        left_group = Group(self.key_activities, self.key_resources)
        left_group.arrange(DOWN, buff=0)

        right_group = Group(self.customer_relationships, self.channels)
        right_group.arrange(DOWN, buff=0)

        up_group = Group(self.key_partners, left_group, self.value_propositions, right_group, self.customers)
        up_group.arrange(RIGHT, buff=0)

        costs_group = Group(self.cost_structure, self.revenue_streams)
        costs_group.arrange(RIGHT, buff=0)

        self.canvas_group = Group(up_group, costs_group)
        self.canvas_group.arrange(DOWN, buff=0)

    def construct(self):
        self.add(self.canvas_group)
        self.play(self.camera.auto_zoom(self.canvas_group, animate=True).scale(1.1))
        self.remove(self.canvas_group)

        self.play(
            LaggedStart(*[FadeIn(card) for card in self.cards], lag_ratio=0.2, run_time=4),
            run_time=4,
        )

        for card in self.cards:
            self.play(self.camera.frame.animate.move_to(card), run_time=1)
            self.play(self.camera.auto_zoom(card, animate=True).scale(1.05), run_time=1)
            self.play(card.show_background(), run_time=1)

            card.add_content()
            for timed_animation in card.card_data.timed_animations:
                card.add_component(timed_animation.component)
                self.play(timed_animation.animation, run_time=1)
                self.wait(timed_animation.length)

        self.play(self.camera.auto_zoom(self.canvas_group, animate=True).scale(1.1), run_time=2)
        self.wait(0.5)

        logo = SVGMobject("assets/logo.svg", height=8, width=8)
        logo.set_z_index(2)
        self.play(Write(logo, run_time=1.2), run_time=1.2)
        self.wait(3)


if __name__ == "__main__":
    video = BusinessModelCanvas()
    video.render()
