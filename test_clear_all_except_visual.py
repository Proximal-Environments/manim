#!/usr/bin/env python
"""
Visual demonstration of the clear_all_except method
This creates an animation showing how clear_all_except works
"""
from manimlib import *

class ClearAllExceptDemo(Scene):
    def construct(self):
        # Title
        title = Text("clear_all_except() Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(0.5)
        
        # Create multiple shapes
        circle = Circle(color=BLUE, radius=0.5)
        square = Square(color=RED, side_length=1).shift(LEFT * 2.5)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2.5)
        
        # Position them in a row
        circle.shift(DOWN * 0.5)
        square.shift(DOWN * 0.5)
        triangle.shift(DOWN * 0.5)
        
        # Add labels
        circle_label = Text("Circle", font_size=24, color=BLUE).next_to(circle, DOWN)
        square_label = Text("Square", font_size=24, color=RED).next_to(square, DOWN)
        triangle_label = Text("Triangle", font_size=24, color=GREEN).next_to(triangle, DOWN)
        
        # Show all objects
        self.play(
            FadeIn(circle),
            FadeIn(square),
            FadeIn(triangle),
            FadeIn(circle_label),
            FadeIn(square_label),
            FadeIn(triangle_label),
        )
        self.wait(1)
        
        # Instruction 1
        instruction1 = Text(
            "We have 3 shapes on screen",
            font_size=32,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(instruction1))
        self.wait(1)
        
        # Instruction 2
        instruction2 = Text(
            "Let's keep only the circle using:",
            font_size=32,
            color=YELLOW
        ).move_to(instruction1)
        code = Text(
            "self.clear_all_except(circle)",
            font_size=28,
            font="Monospace",
            color=GREEN
        ).next_to(instruction2, DOWN, buff=0.3)
        
        self.play(
            FadeTransform(instruction1, instruction2),
            FadeIn(code)
        )
        self.wait(1.5)
        
        # Perform clear_all_except
        self.play(
            FadeOut(instruction2),
            FadeOut(code)
        )
        self.wait(0.3)
        
        # Keep track of what we want to keep
        to_keep = [title, circle, circle_label]
        
        # Clear all except title, circle, and its label
        self.clear_all_except(*to_keep)
        self.wait(1.5)
        
        # Result message
        result = Text(
            "Only the circle remains!",
            font_size=36,
            color=GREEN
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(result))
        self.wait(1)
        
        # Demo 2: Keep multiple objects
        self.play(FadeOut(result))
        self.wait(0.3)
        
        # Add new shapes
        star = Star(color=YELLOW, n=5).shift(LEFT * 1.5 + DOWN * 0.5).scale(0.5)
        pentagon = RegularPolygon(n=5, color=PURPLE).shift(RIGHT * 1.5 + DOWN * 0.5).scale(0.5)
        
        star_label = Text("Star", font_size=24, color=YELLOW).next_to(star, DOWN)
        pentagon_label = Text("Pentagon", font_size=24, color=PURPLE).next_to(pentagon, DOWN)
        
        self.play(
            FadeIn(star),
            FadeIn(pentagon),
            FadeIn(star_label),
            FadeIn(pentagon_label),
        )
        self.wait(1)
        
        # Instruction 3
        instruction3 = Text(
            "Now keep circle and star:",
            font_size=32,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        code2 = Text(
            "self.clear_all_except(circle, star)",
            font_size=28,
            font="Monospace",
            color=GREEN
        ).next_to(instruction3, DOWN, buff=0.3)
        
        self.play(
            FadeIn(instruction3),
            FadeIn(code2)
        )
        self.wait(1.5)
        
        self.play(
            FadeOut(instruction3),
            FadeOut(code2)
        )
        self.wait(0.3)
        
        # Clear all except title, circle, circle_label, star, and star_label
        self.clear_all_except(title, circle, circle_label, star, star_label)
        self.wait(1.5)
        
        # Final message
        final = Text(
            "Circle and Star remain!",
            font_size=36,
            color=GREEN
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(final))
        self.wait(2)
        
        # Clean up everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ClearAllExceptInteractiveDemo(InteractiveScene):
    def construct(self):
        # Title
        title = Text("InteractiveScene Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(0.5)
        
        # Create shapes
        shapes = VGroup(
            Circle(color=RED),
            Square(color=BLUE),
            Triangle(color=GREEN),
            Star(color=YELLOW, n=5),
        ).arrange(RIGHT, buff=1).scale(0.7)
        
        self.play(FadeIn(shapes))
        self.wait(1)
        
        # Instruction
        instruction = Text(
            "clear_all_except() also works in InteractiveScene!",
            font_size=32,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(instruction))
        self.wait(1)
        
        # Keep only first and last shapes
        to_keep = [title, instruction, shapes[0], shapes[3]]
        self.clear_all_except(*to_keep)
        self.wait(2)
        
        result = Text(
            "Selection features still work!",
            font_size=32,
            color=GREEN
        ).move_to(instruction)
        self.play(FadeTransform(instruction, result))
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    print("Running visual demonstration...")
    print("(This will create animation files)")
    
    # Run the basic scene demo
    scene = ClearAllExceptDemo()
    scene.run()
    
    # Run the interactive scene demo
    scene2 = ClearAllExceptInteractiveDemo()
    scene2.run()
    
    print("Demonstrations complete!")
