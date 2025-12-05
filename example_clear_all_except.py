#!/usr/bin/env python3
"""
Simple example demonstrating the clear_all_except method.
Run with: xvfb-run -a manimgl example_clear_all_except.py SimpleClearExample -w
"""

from manimlib import *


class SimpleClearExample(Scene):
    """Basic example showing clear_all_except usage"""
    
    def construct(self):
        # Step 1: Create and show multiple objects
        title = Text("clear_all_except() Demo", font_size=48)
        title.to_edge(UP)
        
        circle = Circle(color=BLUE, radius=1).shift(LEFT * 2)
        square = Square(color=RED, side_length=2)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        self.play(FadeIn(title))
        self.play(
            FadeIn(circle),
            FadeIn(square),
            FadeIn(triangle),
        )
        self.wait()
        
        # Step 2: Show what we have
        count_text = Text(f"Objects in scene: {len(self.get_mobjects())}", font_size=24)
        count_text.to_edge(DOWN)
        self.play(FadeIn(count_text))
        self.wait()
        
        # Step 3: Use clear_all_except to keep only the circle
        instruction = Text("Keeping only the circle...", font_size=30)
        instruction.move_to(count_text)
        self.play(Transform(count_text, instruction))
        self.wait()
        
        # This is the key line - clear all except circle
        self.clear_all_except(circle)
        
        # Step 4: Show result
        new_count_text = Text(f"Objects remaining: {len(self.get_mobjects())}", font_size=24)
        new_count_text.to_edge(DOWN)
        self.add(new_count_text)
        self.wait(2)
        
        # Step 5: Add new objects
        self.play(FadeOut(new_count_text))
        star = Star(color=YELLOW).shift(RIGHT * 2)
        pentagon = RegularPolygon(n=5, color=PURPLE).shift(LEFT * 2)
        
        self.play(
            FadeIn(star),
            FadeIn(pentagon),
        )
        self.wait()
        
        # Step 6: Keep multiple objects
        keep_text = Text("Now keeping circle and star...", font_size=24)
        keep_text.to_edge(DOWN)
        self.play(FadeIn(keep_text))
        self.wait()
        
        self.clear_all_except(circle, star)
        self.wait(2)
        
        # Final message
        final = Text("Demo Complete!", font_size=36)
        self.play(
            FadeOut(circle),
            FadeOut(star),
            FadeIn(final),
        )
        self.wait(2)


class ComparisonExample(Scene):
    """Comparing clear_all_except with traditional methods"""
    
    def construct(self):
        # Create shapes
        shapes = VGroup(
            Circle(color=BLUE),
            Square(color=RED),
            Triangle(color=GREEN),
            Star(color=YELLOW),
        ).arrange(RIGHT, buff=0.5)
        
        title = Text("Method Comparison", font_size=36).to_edge(UP)
        self.play(FadeIn(title), FadeIn(shapes))
        self.wait()
        
        # Traditional way - remove specific objects
        traditional = Text("Traditional: self.remove(square, triangle, star)", font_size=20)
        traditional.to_edge(DOWN)
        self.play(FadeIn(traditional))
        self.wait()
        
        # Do it the traditional way
        self.play(
            FadeOut(shapes[1]),
            FadeOut(shapes[2]),
            FadeOut(shapes[3]),
        )
        self.wait()
        
        # Reset
        self.play(FadeOut(traditional))
        self.play(FadeIn(shapes[1]), FadeIn(shapes[2]), FadeIn(shapes[3]))
        self.wait()
        
        # New way - clear_all_except
        new_way = Text("New way: self.clear_all_except(circle)", font_size=20)
        new_way.to_edge(DOWN)
        self.play(FadeIn(new_way))
        self.wait()
        
        # Use clear_all_except
        self.clear_all_except(shapes[0])
        self.wait(2)
        
        # Show benefit
        benefit = Text("✓ More concise and intuitive!", font_size=30, color=GREEN)
        self.play(
            FadeOut(new_way),
            FadeIn(benefit),
        )
        self.wait(2)


class PracticalExample(Scene):
    """A practical use case: building up and cleaning a construction"""
    
    def construct(self):
        # Title
        title = Text("Practical Use Case", font_size=36).to_edge(UP)
        self.play(FadeIn(title))
        
        # Step 1: Draw construction lines
        subtitle = Text("Drawing construction...", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        
        horizontal_line = Line(LEFT * 3, RIGHT * 3, color=GREY)
        vertical_line = Line(DOWN * 2, UP * 2, color=GREY)
        construction_lines = VGroup(horizontal_line, vertical_line)
        
        self.play(Create(construction_lines))
        self.wait()
        
        # Step 2: Draw the actual shape using the construction
        self.play(FadeOut(subtitle))
        subtitle = Text("Creating main shape...", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        
        main_shape = Square(color=BLUE, side_length=2)
        self.play(DrawBorderThenFill(main_shape))
        self.wait()
        
        # Step 3: Add decorations
        self.play(FadeOut(subtitle))
        subtitle = Text("Adding details...", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        
        dot1 = Dot(color=RED).move_to(main_shape.get_corner(UL))
        dot2 = Dot(color=RED).move_to(main_shape.get_corner(UR))
        dot3 = Dot(color=RED).move_to(main_shape.get_corner(DL))
        dot4 = Dot(color=RED).move_to(main_shape.get_corner(DR))
        temp_dots = VGroup(dot1, dot2, dot3, dot4)
        
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in temp_dots], lag_ratio=0.1))
        self.wait()
        
        # Step 4: Clean up - keep only the main shape
        self.play(FadeOut(subtitle))
        subtitle = Text("Cleaning up construction...", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait()
        
        # This is where clear_all_except shines!
        self.clear_all_except(main_shape)
        self.wait()
        
        # Final message
        final = Text("Final Result: Clean and Simple!", font_size=30, color=GREEN)
        final.next_to(title, DOWN)
        self.add(final)
        self.wait(2)


if __name__ == "__main__":
    print("\nAvailable examples:")
    print("1. SimpleClearExample - Basic usage demonstration")
    print("2. ComparisonExample - Comparing with traditional methods")
    print("3. PracticalExample - Real-world use case")
    print("\nRun with: xvfb-run -a manimgl example_clear_all_except.py <ExampleName> -w")
    print("Example: xvfb-run -a manimgl example_clear_all_except.py SimpleClearExample -w\n")
