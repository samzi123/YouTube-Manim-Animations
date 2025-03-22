from manim import *

class Intro(Scene):
    def construct(self):
        title_text = "Boid Simulation"
        title = Text(title_text, font_size=38)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(16)
        
        # Transform to show "Bird-oid Object"
        final_text = "Bird-oid Object"
        final_title = Text(final_text, font_size=38)
        final_title.to_edge(UP, buff=0.2)

        self.play(Transform(title, final_title))
        self.wait(5)

class Separation6(Scene):
    def construct(self):
        initial_title = Text("The Three Rules", font_size=38)
        initial_title.to_edge(UP, buff=0.2)
        self.play(Write(initial_title))
        
        self.wait(20)
        
        # Transform to show Separation title
        title = Text("Rule #1: Separation", font_size=38)
        title.to_edge(UP, buff=0.2)
        self.play(ReplacementTransform(initial_title, title))
        
        self.wait(9)
        
        # Pseudocode using Code class which preserves indentation
        code_str = '''function calculate_separation(b):
    steer = Vector(0, 0)
    total = 0
    
    for each boid n:
        if b == n:
            continue
        if distance(b, n) < protected_radius:
            diff = (b.position - n.position).normalize()
            diff /= distance(b, n) // scale by inverse of distance
            steer += diff
            total += 1

    if total > 0:
        steer /= total
    return steer * separation_weight'''
        
        code = Code(
            code_string=code_str,
            tab_width=4,
            language="python",
            background_config={"fill_color": "#282c34"},
            paragraph_config={"font_size": 20},
        )
        
        # Position the code on the bottom right of screen
        code.height = 6
        code.width = 6
        code.to_edge(DOWN, buff=0.2)
        code.to_edge(RIGHT, buff=0.2)
        
        self.play(Create(code))
        
        # Only show the pseudo-code for 5 secs
        self.wait(5)
        self.play(FadeOut(code))

        self.wait(30)

class Alignment(Scene):
    def construct(self):
        title = Text("Rule #2: Alignment", font_size=38)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(3)
        
        code_str = '''function calculate_alignment(b):
    alignment = Vector(0, 0)
    total = 0
    for each boid n:
        if b == n:
            continue
        if distance(b, n) < visual_radius:
            alignment += n.velocity
            total += 1

    if total > 0:
        alignment /= total
        alignment = alignment.normalize() * MAX_SPEED - b.velocity
        alignment *= alignment_weight
    return alignment'''
        
        code = Code(
            code_string=code_str,
            tab_width=4,
            language="python",
            background_config={"fill_color": "#282c34"},
            paragraph_config={"font_size": 20},
        )
        
        # Position the code on the bottom right of screen
        code.height = 6
        code.width = 6
        code.to_edge(DOWN, buff=0.2)
        code.to_edge(RIGHT, buff=0.2)
        
        self.play(Create(code))
        self.wait(3)

        # remove code
        self.play(FadeOut(code))
        self.wait(10)


class Cohesion(Scene):
    def construct(self):
        title = Text("Rule #3: Cohesion", font_size=38)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(4)
        
        code_str = '''function calculate_cohesion(b):
    cohesion = Vector(0, 0)
    total = 0
    for each boid n:
        if b == n:
            continue
        if distance(b, n) < visual_radius:
            cohesion += n.position
            total += 1

    if total > 0:
        cohesion /= total
        cohesion = (cohesion - b.position).normalize() * MAX_SPEED - b.velocity
        cohesion *= cohesion_weight
    return cohesion'''
        
        code = Code(
            code_string=code_str,
            tab_width=4,
            language="python",
            background_config={"fill_color": "#282c34"},
            paragraph_config={"font_size": 20},
        )
        
        # Position the code on the bottom right of screen
        code.height = 6
        code.width = 6
        code.to_edge(DOWN, buff=0.2)
        code.to_edge(RIGHT, buff=0.2)
        
        self.play(Create(code))
        self.wait(3)

        # remove code
        self.play(FadeOut(code))
        self.wait(15)
