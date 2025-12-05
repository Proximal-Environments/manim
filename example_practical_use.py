#!/usr/bin/env python
"""
Practical example: Using clear_all_except for a math explanation scene
Demonstrates a real-world use case where we want to keep certain elements
while transitioning between different parts of an explanation.
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Line
from manimlib.mobject.svg.tex_mobject import Tex
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import *


class MathExplanationScene(Scene):
    """
    A practical example showing how clear_all_except helps in creating
    clean scene transitions while keeping important reference elements.
    """
    
    def construct(self):
        # Create a persistent title that stays throughout
        title = Text("Pythagorean Theorem", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Part 1: Introduction
        intro_text = Text("Let's explore a right triangle", font_size=36)
        intro_text.next_to(title, DOWN, buff=0.5)
        self.add(intro_text)
        self.wait(1)
        
        # Draw a right triangle
        point_a = 2 * LEFT + 1 * DOWN
        point_b = 2 * RIGHT + 1 * DOWN
        point_c = 2 * LEFT + 2 * UP
        
        side_a = Line(point_a, point_b, color=BLUE)
        side_b = Line(point_b, point_c, color=GREEN)
        side_c = Line(point_c, point_a, color=RED)
        
        label_a = Tex("a", color=BLUE).next_to(side_a, DOWN)
        label_b = Tex("b", color=GREEN).next_to(side_b, RIGHT)
        label_c = Tex("c", color=RED).next_to(side_c, LEFT)
        
        triangle_group = [side_a, side_b, side_c, label_a, label_b, label_c]
        
        self.add(*triangle_group)
        self.wait(2)
        
        # Transition: Keep only title and triangle, remove intro text
        print("Transition 1: Removing intro text, keeping title and triangle")
        self.clear_all_except(title, *triangle_group)
        self.wait(0.5)
        
        # Part 2: Show the formula
        formula = Tex("a^2 + b^2 = c^2", font_size=48)
        formula.next_to(title, DOWN, buff=0.5)
        
        explanation = Text("The sum of squares of the two sides", font_size=24)
        explanation.next_to(formula, DOWN, buff=0.3)
        
        explanation2 = Text("equals the square of the hypotenuse", font_size=24)
        explanation2.next_to(explanation, DOWN, buff=0.1)
        
        self.add(formula, explanation, explanation2)
        self.wait(2)
        
        # Transition: Keep title and formula, show specific side calculations
        print("Transition 2: Keeping title and formula, showing calculations")
        self.clear_all_except(title, formula)
        self.wait(0.5)
        
        # Part 3: Numerical example
        example_text = Text("Example: If a=3 and b=4", font_size=36)
        example_text.next_to(formula, DOWN, buff=1)
        self.add(example_text)
        self.wait(1)
        
        calc_1 = Tex("3^2 + 4^2 = c^2")
        calc_1.next_to(example_text, DOWN, buff=0.5)
        self.add(calc_1)
        self.wait(1)
        
        calc_2 = Tex("9 + 16 = c^2")
        calc_2.next_to(calc_1, DOWN, buff=0.3)
        self.add(calc_2)
        self.wait(1)
        
        calc_3 = Tex("25 = c^2")
        calc_3.next_to(calc_2, DOWN, buff=0.3)
        self.add(calc_3)
        self.wait(1)
        
        calc_4 = Tex("c = 5", color=YELLOW)
        calc_4.next_to(calc_3, DOWN, buff=0.3)
        self.add(calc_4)
        self.wait(2)
        
        # Final transition: Keep only title and result
        print("Transition 3: Showing final result")
        self.clear_all_except(title, calc_4)
        
        # Center the result
        calc_4.move_to(ORIGIN)
        self.wait(1)
        
        # Add conclusion
        conclusion = Text("Therefore, the hypotenuse is 5 units!", font_size=36, color=GREEN)
        conclusion.next_to(calc_4, DOWN, buff=1)
        self.add(conclusion)
        self.wait(2)
        
        # Clean ending
        print("Final: Keeping title and conclusion")
        self.clear_all_except(title, conclusion)
        conclusion.move_to(ORIGIN)
        self.wait(1)
        
        print("\n✅ Scene completed successfully!")


class InteractiveDemo(Scene):
    """
    Another practical example showing progressive building and clearing
    """
    
    def construct(self):
        # Header that stays throughout
        header = Text("Building Blocks Demo", font_size=42)
        header.to_edge(UP)
        self.add(header)
        
        # Phase 1: Add shapes
        phase_label = Text("Phase 1: Adding shapes", font_size=30)
        phase_label.next_to(header, DOWN)
        self.add(phase_label)
        self.wait(0.5)
        
        shapes = []
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        positions = [2*LEFT, LEFT, ORIGIN, RIGHT, 2*RIGHT]
        
        for i, (pos, color) in enumerate(zip(positions, colors)):
            if i % 2 == 0:
                shape = Circle(radius=0.4, color=color)
            else:
                shape = Square(side_length=0.8, color=color)
            shape.shift(pos)
            shapes.append(shape)
            self.add(shape)
            self.wait(0.2)
        
        self.wait(1)
        
        # Phase 2: Keep only every other shape
        self.remove(phase_label)
        phase_label = Text("Phase 2: Keep every other shape", font_size=30)
        phase_label.next_to(header, DOWN)
        self.add(phase_label)
        self.wait(0.5)
        
        keep_shapes = [shapes[i] for i in range(0, len(shapes), 2)]
        self.clear_all_except(header, phase_label, *keep_shapes)
        self.wait(1)
        
        # Phase 3: Keep only the first and last
        self.remove(phase_label)
        phase_label = Text("Phase 3: Keep first and last", font_size=30)
        phase_label.next_to(header, DOWN)
        self.add(phase_label)
        self.wait(0.5)
        
        self.clear_all_except(header, phase_label, keep_shapes[0], keep_shapes[-1])
        self.wait(1)
        
        # Phase 4: Final cleanup
        self.remove(phase_label)
        phase_label = Text("Complete!", font_size=36, color=GREEN)
        phase_label.next_to(header, DOWN)
        self.add(phase_label)
        self.wait(0.5)
        
        self.clear_all_except(header, phase_label)
        self.wait(1)
        
        print("\n✅ Interactive demo completed!")


if __name__ == "__main__":
    import sys
    
    print("=" * 70)
    print("Running Practical Example 1: Math Explanation")
    print("=" * 70)
    
    scene1 = MathExplanationScene(
        skip_animations=True,
        show_animation_progress=False
    )
    
    try:
        scene1.run()
    except Exception as e:
        print(f"❌ Error in example 1: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("Running Practical Example 2: Interactive Demo")
    print("=" * 70)
    
    scene2 = InteractiveDemo(
        skip_animations=True,
        show_animation_progress=False
    )
    
    try:
        scene2.run()
    except Exception as e:
        print(f"❌ Error in example 2: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("🎉 All practical examples completed successfully!")
    print("=" * 70)
    print("\nThese examples demonstrate how clear_all_except() helps in:")
    print("  • Keeping persistent UI elements (titles, headers)")
    print("  • Creating clean scene transitions")
    print("  • Managing complex scenes with multiple phases")
    print("  • Maintaining context while removing clutter")
