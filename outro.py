from manim import *


class Outro(MovingCameraScene):
    def construct(self):
        title = Text("Fin", font_size=120)
        subtitle = Text("Vídeo animado con", font_size=50)
        logo = ManimBanner()
        logo.width = 2
        logo.height = 2

        start_group = Group(title, subtitle, logo).arrange(DOWN, buff=1)
        start_group.set_z_index(2)

        self.play(self.camera.auto_zoom(start_group).scale(1.1))

        self.wait(0.5)
        underline_title = Underline(title)
        self.play(
            LaggedStart(Write(title), Write(underline_title), Write(subtitle), Write(logo), lag_ratio=0.25, run_time=1)
        )
        self.wait(0.2)
        self.play(logo.expand(direction="center"))
        self.wait(1)
        self.play(FadeOut(start_group, underline_title, logo), run_time=1)
        self.wait(1)


# Run the animation
if __name__ == "__main__":
    video = Outro()
    video.render()
