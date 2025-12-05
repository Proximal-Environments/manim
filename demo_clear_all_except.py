#!/usr/bin/env python
"""Demo script showing clear_all_except in action"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle, Star, RegularPolygon
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, UP, DOWN, LEFT, RIGHT


class DemoClearAllExcept(Scene):
    """Visual demonstration of clear_all_except method"""
    
    def construct(self):
        # Create title
        title = Text("Demo: clear_all_except", font_size=48)
        title.to_edge(UP)
        self.add(title)
        self.wait(1)
        
        # Create multiple shapes
        circle = Circle(color=RED, radius=0.5).shift(2 * LEFT + UP)
        square = Square(color=BLUE, side_length=1).shift(UP)
        triangle = Triangle(color=GREEN).shift(2 * RIGHT + UP)
        star = Star(color=YELLOW, n=5, outer_radius=0.5).shift(2 * LEFT + DOWN)
        pentagon = RegularPolygon(n=5, color=PURPLE).shift(DOWN)
        hexagon = RegularPolygon(n=6, color=ORANGE).shift(2 * RIGHT + DOWN)
        
        # Add all shapes
        label1 = Text("Adding 6 shapes", font_size=36)
        label1.next_to(title, DOWN, buff=0.5)
        self.add(label1)
        self.wait(0.5)
        
        self.add(circle, square, triangle, star, pentagon, hexagon)
        self.wait(2)
        
        # Clear label
        self.remove(label1)
        
        # Keep only blue square and green triangle
        label2 = Text("Keep only BLUE square and GREEN triangle", font_size=30)
        label2.next_to(title, DOWN, buff=0.5)
        self.add(label2)
        self.wait(1)
        
        self.clear_all_except(title, label2, square, triangle)
        self.wait(2)
        
        # Remove label
        self.remove(label2)
        
        # Add back some shapes
        label3 = Text("Add back YELLOW star and PURPLE pentagon", font_size=30)
        label3.next_to(title, DOWN, buff=0.5)
        self.add(label3)
        self.wait(1)
        
        self.add(star, pentagon)
        self.wait(2)
        
        # Remove label
        self.remove(label3)
        
        # Keep only the title
        label4 = Text("Keep only the title", font_size=36)
        label4.next_to(title, DOWN, buff=0.5)
        self.add(label4)
        self.wait(1)
        
        self.clear_all_except(title)
        self.wait(2)
        
        # Final message
        final = Text("Demo Complete!", font_size=48, color=GREEN)
        final.next_to(title, DOWN, buff=1)
        self.add(final)
        self.wait(2)


if __name__ == "__main__":
    import sys
    from manimlib.config import manim_config
    
    # Run the demo
    scene = DemoClearAllExcept(
        skip_animations=False,  # Show animations for the demo
        show_animation_progress=False
    )
    
    try:
        scene.run()
        print("\n✅ Demo completed successfully!")
    except Exception as e:
        print(f"❌ Error in demo: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
