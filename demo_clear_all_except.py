#!/usr/bin/env python3
"""
Demo script showing the usage of clear_all_except method.
This can be rendered with: manimgl demo_clear_all_except.py DemoClearAllExcept -w
"""

from manimlib import *


class DemoClearAllExcept(Scene):
    def construct(self):
        # Create several shapes
        circle = Circle(color=BLUE).shift(LEFT * 2)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Add text labels
        circle_label = Text("Circle", font_size=24).next_to(circle, DOWN)
        square_label = Text("Square", font_size=24).next_to(square, DOWN)
        triangle_label = Text("Triangle", font_size=24).next_to(triangle, DOWN)
        
        # Show all shapes
        title = Text("All Shapes", font_size=36).to_edge(UP)
        self.play(
            FadeIn(title),
            FadeIn(circle),
            FadeIn(square),
            FadeIn(triangle),
            FadeIn(circle_label),
            FadeIn(square_label),
            FadeIn(triangle_label),
        )
        self.wait()
        
        # Clear all except circle
        new_title = Text("Keep Only Circle", font_size=36).to_edge(UP)
        self.play(FadeOut(title))
        self.play(FadeIn(new_title))
        self.wait(0.5)
        
        # Use clear_all_except to keep only circle and its label
        self.clear_all_except(circle, circle_label)
        self.wait(2)
        
        # Add new shapes
        star = Star(color=YELLOW).shift(RIGHT * 2)
        star_label = Text("Star", font_size=24).next_to(star, DOWN)
        
        new_title2 = Text("Add New Shapes", font_size=36).to_edge(UP)
        self.play(
            Transform(new_title, new_title2),
            FadeIn(star),
            FadeIn(star_label),
        )
        self.wait()
        
        # Now keep only the star
        new_title3 = Text("Keep Only Star", font_size=36).to_edge(UP)
        self.play(Transform(new_title, new_title3))
        self.wait(0.5)
        
        self.clear_all_except(star, star_label)
        self.wait(2)
        
        # Final message
        final_text = Text("clear_all_except() Demo Complete!", font_size=30)
        self.play(
            FadeOut(star),
            FadeOut(star_label),
            FadeIn(final_text)
        )
        self.wait(2)


class DemoInteractiveClearAllExcept(InteractiveScene):
    """
    Demo for InteractiveScene with clear_all_except.
    This preserves the interactive features like selection_highlight.
    """
    def construct(self):
        # Create several shapes
        shapes = VGroup(
            Circle(color=BLUE).shift(LEFT * 3),
            Square(color=RED).shift(LEFT),
            Triangle(color=GREEN).shift(RIGHT),
            Star(color=YELLOW).shift(RIGHT * 3),
        )
        
        labels = VGroup(*[
            Text(type(shape).__name__, font_size=24).next_to(shape, DOWN)
            for shape in shapes
        ])
        
        title = Text("Interactive Scene Demo", font_size=36).to_edge(UP)
        
        # Show all shapes
        self.play(
            FadeIn(title),
            LaggedStart(*[FadeIn(shape) for shape in shapes], lag_ratio=0.2),
            LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=0.2),
        )
        self.wait()
        
        # Clear all except first two shapes
        instruction = Text("Keeping only first two shapes...", font_size=24).to_edge(DOWN)
        self.play(FadeIn(instruction))
        self.wait(0.5)
        
        # Keep only first circle and square with their labels
        self.clear_all_except(shapes[0], shapes[1], labels[0], labels[1])
        self.wait(2)
        
        # Note: The selection_highlight is automatically preserved
        instruction2 = Text("Selection features still work!", font_size=24).to_edge(DOWN)
        self.play(Transform(instruction, instruction2))
        self.wait(2)
        
        final_text = Text("Demo Complete!", font_size=30)
        self.play(
            FadeOut(shapes),
            FadeOut(labels),
            FadeOut(instruction),
            FadeIn(final_text)
        )
        self.wait(2)


if __name__ == "__main__":
    # Run the demo
    from manimlib.config import parse_cli
    from manimlib.scene.scene import Scene as BaseScene
    
    print("Demo scenes for clear_all_except method:")
    print("1. DemoClearAllExcept - Basic scene demo")
    print("2. DemoInteractiveClearAllExcept - Interactive scene demo")
    print()
    print("Run with: xvfb-run -a manimgl demo_clear_all_except.py DemoClearAllExcept -w")
    print("Or:       xvfb-run -a manimgl demo_clear_all_except.py DemoInteractiveClearAllExcept -w")
