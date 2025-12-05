#!/usr/bin/env python3
"""
Example usage of clear_all_except() method
This script demonstrates practical use cases for the new method.
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle, Rectangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import *
from manimlib.animation.creation import ShowCreation
from manimlib.animation.fading import FadeIn, FadeOut


class ExampleClearAllExcept(Scene):
    """
    Example showing a practical use case: creating multiple "slides" 
    where you want to keep a title but change all other content.
    """
    
    def construct(self):
        # Create a persistent title
        title = Text("Geometry Shapes", font_size=48).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(0.5)
        
        # Slide 1: Show circles
        subtitle1 = Text("Circles", font_size=36).next_to(title, DOWN)
        circles = [
            Circle(radius=0.5, color=color).shift(pos)
            for color, pos in zip([RED, GREEN, BLUE], [2*LEFT, ORIGIN, 2*RIGHT])
        ]
        
        self.play(FadeIn(subtitle1))
        self.play(*[ShowCreation(c) for c in circles])
        self.wait(1)
        
        # Clear all except title, show squares
        self.clear_all_except(title)  # Everything except title is removed
        
        subtitle2 = Text("Squares", font_size=36).next_to(title, DOWN)
        squares = [
            Square(side_length=1, color=color).shift(pos)
            for color, pos in zip([YELLOW, PINK, TEAL], [2*LEFT, ORIGIN, 2*RIGHT])
        ]
        
        self.play(FadeIn(subtitle2))
        self.play(*[ShowCreation(s) for s in squares])
        self.wait(1)
        
        # Clear all except title, show triangles
        self.clear_all_except(title)
        
        subtitle3 = Text("Triangles", font_size=36).next_to(title, DOWN)
        triangles = [
            Triangle(color=color).shift(pos)
            for color, pos in zip([PURPLE, ORANGE, MAROON], [2*LEFT, ORIGIN, 2*RIGHT])
        ]
        
        self.play(FadeIn(subtitle3))
        self.play(*[Create(t) for t in triangles])
        self.wait(1)
        
        # Final slide: Mixed shapes, but keep title
        self.clear_all_except(title)
        
        subtitle4 = Text("Mixed Shapes", font_size=36).next_to(title, DOWN)
        mixed = [
            Circle(radius=0.5, color=RED).shift(2*LEFT + UP),
            Square(side_length=1, color=GREEN).shift(2*RIGHT + UP),
            Triangle(color=BLUE).shift(2*LEFT + DOWN),
            Rectangle(color=YELLOW, width=1.5, height=1).shift(2*RIGHT + DOWN),
        ]
        
        self.play(FadeIn(subtitle4))
        self.play(*[Create(m) for m in mixed])
        self.wait(1)
        
        # Final clear
        end_text = Text("The End!", font_size=48).move_to(ORIGIN)
        self.clear_all_except(title)
        self.play(FadeIn(end_text))
        self.wait(2)


class ExampleSelectiveUpdate(Scene):
    """
    Example showing how to update only specific objects while keeping others.
    Useful for animations where some elements remain constant.
    """
    
    def construct(self):
        # Create a coordinate system that stays constant
        axes_label = Text("Coordinate System", font_size=36).to_edge(UP)
        
        # Create simple axes
        x_axis = Line(3*LEFT, 3*RIGHT, stroke_width=2)
        y_axis = Line(2*DOWN, 2*UP, stroke_width=2)
        axes = [axes_label, x_axis, y_axis]
        
        self.add(*axes)
        self.wait(0.5)
        
        # Show different points on the coordinate system
        for i in range(3):
            # Clear everything except the axes
            self.clear_all_except(*axes)
            
            # Add new point and label
            point = Circle(radius=0.1, color=BLUE, fill_opacity=1).shift(
                [2*np.cos(i*2*PI/3), 1.5*np.sin(i*2*PI/3), 0]
            )
            label = Text(f"Point {i+1}", font_size=24).next_to(point, UP)
            
            self.play(FadeIn(point), FadeIn(label))
            self.wait(1)
        
        # Final message
        self.clear_all_except(*axes)
        message = Text("Axes remained constant!", font_size=30).to_edge(DOWN)
        self.play(FadeIn(message))
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    # Check if we should run with display
    run_with_display = len(sys.argv) > 1 and sys.argv[1] == "--show"
    
    if run_with_display:
        print("Running with display output...")
        print("\nExample 1: Clear All Except with Multiple Slides")
        scene1 = ExampleClearAllExcept()
        scene1.run()
        
        print("\nExample 2: Selective Update with Constant Elements")
        scene2 = ExampleSelectiveUpdate()
        scene2.run()
    else:
        print("Running in headless mode (skip animations)...")
        print("\nExample 1: Clear All Except with Multiple Slides")
        scene1 = ExampleClearAllExcept(skip_animations=True)
        scene1.run()
        print("✓ Example 1 completed")
        
        print("\nExample 2: Selective Update with Constant Elements")
        scene2 = ExampleSelectiveUpdate(skip_animations=True)
        scene2.run()
        print("✓ Example 2 completed")
        
        print("\n✅ All examples completed successfully!")
        print("\nRun with --show flag to see actual animations")
