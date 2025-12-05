#!/usr/bin/env python
"""
Practical example demonstrating the clear_all_except method
This simulates a presentation where you want to keep certain elements
while transitioning between different content sections.
"""
from manimlib import *

class PresentationExample(Scene):
    """
    Simulates a mathematical presentation where we keep the title
    and navigation elements while changing the content.
    """
    
    def construct(self):
        # Create persistent elements (these will stay throughout)
        title = Text("Mathematical Concepts", font_size=48)
        title.to_edge(UP)
        
        # Create navigation dots
        nav_dots = VGroup(*[
            Dot(radius=0.08, color=GREY)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.3)
        nav_dots.to_corner(DR, buff=0.5)
        
        # Add persistent elements
        self.add(title, nav_dots)
        self.wait(0.5)
        
        # Section 1: Circles
        nav_dots[0].set_color(BLUE)
        section1_title = Text("Section 1: Circles", font_size=36, color=BLUE)
        section1_title.next_to(title, DOWN, buff=0.8)
        
        circles = VGroup(*[
            Circle(radius=0.5 + i * 0.2, color=BLUE)
            for i in range(3)
        ])
        
        formula1 = Tex(r"A = \pi r^2", font_size=48)
        formula1.next_to(circles, DOWN, buff=0.5)
        
        self.play(
            FadeIn(section1_title),
            FadeIn(circles),
            FadeIn(formula1)
        )
        self.wait(1.5)
        
        # Transition to Section 2: Keep only persistent elements
        nav_dots[0].set_color(GREY)
        nav_dots[1].set_color(RED)
        
        # This is where clear_all_except shines!
        # Instead of removing each element individually, we just keep what we want
        self.clear_all_except(title, nav_dots)
        
        # Section 2: Squares
        section2_title = Text("Section 2: Squares", font_size=36, color=RED)
        section2_title.next_to(title, DOWN, buff=0.8)
        
        squares = VGroup(*[
            Square(side_length=0.8 + i * 0.3, color=RED)
            for i in range(3)
        ]).arrange(RIGHT, buff=0.5)
        
        formula2 = Tex(r"A = s^2", font_size=48)
        formula2.next_to(squares, DOWN, buff=0.5)
        
        self.play(
            FadeIn(section2_title),
            FadeIn(squares),
            FadeIn(formula2)
        )
        self.wait(1.5)
        
        # Transition to Section 3
        nav_dots[1].set_color(GREY)
        nav_dots[2].set_color(GREEN)
        
        # Again, keep only persistent elements
        self.clear_all_except(title, nav_dots)
        
        # Section 3: Triangles
        section3_title = Text("Section 3: Triangles", font_size=36, color=GREEN)
        section3_title.next_to(title, DOWN, buff=0.8)
        
        triangles = VGroup(*[
            Triangle(color=GREEN).scale(0.5 + i * 0.2)
            for i in range(3)
        ]).arrange(RIGHT, buff=0.5)
        
        formula3 = Tex(r"A = \frac{1}{2}bh", font_size=48)
        formula3.next_to(triangles, DOWN, buff=0.5)
        
        self.play(
            FadeIn(section3_title),
            FadeIn(triangles),
            FadeIn(formula3)
        )
        self.wait(1.5)
        
        # Final transition - clear everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # End message
        end_text = Text("clear_all_except() makes transitions easy!", font_size=36)
        self.play(FadeIn(end_text))
        self.wait(2)


class ComparisonExample(Scene):
    """
    Shows the difference between manually removing objects vs using clear_all_except
    """
    
    def construct(self):
        # Title
        title = Text("Without vs With clear_all_except()", font_size=40)
        title.to_edge(UP)
        self.add(title)
        
        # Part 1: The hard way (manually removing objects)
        subtitle1 = Text("The Hard Way: Manual Removal", font_size=32, color=RED)
        subtitle1.next_to(title, DOWN, buff=0.5)
        
        code1 = Text(
            "# Create objects\n"
            "obj1, obj2, obj3 = ...\n"
            "header, footer = ...\n"
            "self.add(obj1, obj2, obj3, header, footer)\n\n"
            "# Remove everything except header and footer\n"
            "self.remove(obj1)\n"
            "self.remove(obj2)\n"
            "self.remove(obj3)\n"
            "# Easy to forget objects or make mistakes!",
            font_size=18,
            font="Monospace",
            color=GREY_A,
            line_spacing=0.8
        )
        code1.next_to(subtitle1, DOWN, buff=0.5)
        code1.to_edge(LEFT, buff=0.5)
        
        self.play(FadeIn(subtitle1), FadeIn(code1))
        self.wait(2)
        
        # Part 2: The easy way (using clear_all_except)
        self.clear_all_except(title)
        
        subtitle2 = Text("The Easy Way: clear_all_except()", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN, buff=0.5)
        
        code2 = Text(
            "# Create objects\n"
            "obj1, obj2, obj3 = ...\n"
            "header, footer = ...\n"
            "self.add(obj1, obj2, obj3, header, footer)\n\n"
            "# Keep only header and footer\n"
            "self.clear_all_except(header, footer)\n"
            "# Simple, clear, and impossible to forget objects!",
            font_size=18,
            font="Monospace",
            color=GREY_A,
            line_spacing=0.8
        )
        code2.next_to(subtitle2, DOWN, buff=0.5)
        code2.to_edge(LEFT, buff=0.5)
        
        self.play(FadeIn(subtitle2), FadeIn(code2))
        self.wait(3)
        
        # Summary
        self.clear_all_except(title)
        
        summary = VGroup(
            Text("Benefits:", font_size=32, color=YELLOW),
            Text("✓ More concise code", font_size=24),
            Text("✓ Less error-prone", font_size=24),
            Text("✓ Clearer intent", font_size=24),
            Text("✓ Easier to maintain", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=1)
        
        for item in summary:
            self.play(FadeIn(item))
            self.wait(0.5)
        
        self.wait(2)


class InteractiveDemo(InteractiveScene):
    """
    Demonstrates clear_all_except in an interactive scene
    """
    
    def construct(self):
        title = Text("Interactive Scene Demo", font_size=48)
        title.to_edge(UP)
        self.add(title)
        
        # Create a grid of shapes
        shapes = VGroup(*[
            VGroup(
                Circle(radius=0.3, color=color),
                Text(name, font_size=18).next_to(ORIGIN, DOWN, buff=0.5)
            ).shift(pos)
            for color, name, pos in [
                (RED, "Red", LEFT * 3 + UP),
                (BLUE, "Blue", LEFT * 1 + UP),
                (GREEN, "Green", RIGHT * 1 + UP),
                (YELLOW, "Yellow", RIGHT * 3 + UP),
                (PURPLE, "Purple", LEFT * 2 + DOWN),
                (ORANGE, "Orange", RIGHT * 2 + DOWN),
            ]
        ])
        
        self.play(FadeIn(shapes))
        self.wait(1)
        
        # Keep only red and blue circles
        to_keep = [title, shapes[0], shapes[1]]
        
        instruction = Text(
            "Keeping only Red and Blue circles",
            font_size=28,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(FadeIn(instruction))
        self.wait(1)
        
        self.clear_all_except(*to_keep)
        self.wait(2)
        
        # Notice that selection features still work!
        note = Text(
            "Selection features still work!\n(Try selecting with Ctrl)",
            font_size=24,
            color=GREEN
        ).move_to(instruction)
        
        self.play(FadeTransform(instruction, note))
        self.wait(3)


if __name__ == "__main__":
    print("Running clear_all_except examples...")
    
    # Example 1: Presentation with persistent elements
    print("\n1. Running PresentationExample...")
    scene1 = PresentationExample()
    scene1.run()
    
    # Example 2: Comparison of methods
    print("\n2. Running ComparisonExample...")
    scene2 = ComparisonExample()
    scene2.run()
    
    # Example 3: Interactive scene
    print("\n3. Running InteractiveDemo...")
    scene3 = InteractiveDemo()
    scene3.run()
    
    print("\nAll examples completed!")
