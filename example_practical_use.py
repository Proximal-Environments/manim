#!/usr/bin/env python
"""
Practical example: Using clear_all_except() in a real animation scenario
This demonstrates a multi-slide presentation style animation
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle, Rectangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.animation.creation import ShowCreation, FadeIn, FadeOut
from manimlib.constants import UP, DOWN, LEFT, RIGHT, ORIGIN
from manimlib.constants import RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, WHITE


class PresentationScene(Scene):
    """
    Example: Creating a presentation-style animation where we keep
    a title/header and switch between different content slides
    """
    
    def construct(self):
        # Create persistent header
        header = Text("Mathematics Shapes", font_size=48)
        header.to_edge(UP)
        header.set_color(WHITE)
        
        # Create slide indicator
        slide_num = Text("Slide 1/3", font_size=24)
        slide_num.to_corner(UP + RIGHT)
        
        self.add(header, slide_num)
        self.wait(1)
        
        # SLIDE 1: Circles
        slide1_title = Text("1. Circles", font_size=36)
        slide1_title.next_to(header, DOWN, buff=0.5)
        
        circle1 = Circle(color=RED, radius=0.5).shift(LEFT * 2)
        circle2 = Circle(color=BLUE, radius=0.7)
        circle3 = Circle(color=GREEN, radius=0.6).shift(RIGHT * 2)
        
        desc1 = Text("Three circles of different sizes", font_size=24)
        desc1.to_edge(DOWN)
        
        self.play(FadeIn(slide1_title))
        self.play(ShowCreation(circle1))
        self.play(ShowCreation(circle2))
        self.play(ShowCreation(circle3))
        self.add(desc1)
        self.wait(2)
        
        # Transition to SLIDE 2: Keep only header and slide_num, clear rest
        slide_num.become(Text("Slide 2/3", font_size=24).to_corner(UP + RIGHT))
        self.clear_all_except(header, slide_num)
        
        slide2_title = Text("2. Squares", font_size=36)
        slide2_title.next_to(header, DOWN, buff=0.5)
        
        square1 = Square(color=YELLOW, side_length=1).shift(LEFT * 2.5 + DOWN * 0.5)
        square2 = Square(color=PURPLE, side_length=1.2).shift(ORIGIN + DOWN * 0.5)
        square3 = Square(color=ORANGE, side_length=0.8).shift(RIGHT * 2.5 + DOWN * 0.5)
        
        desc2 = Text("Squares with different colors", font_size=24)
        desc2.to_edge(DOWN)
        
        self.play(FadeIn(slide2_title))
        self.play(ShowCreation(square1))
        self.play(ShowCreation(square2))
        self.play(ShowCreation(square3))
        self.add(desc2)
        self.wait(2)
        
        # Transition to SLIDE 3: Mixed shapes
        slide_num.become(Text("Slide 3/3", font_size=24).to_corner(UP + RIGHT))
        self.clear_all_except(header, slide_num)
        
        slide3_title = Text("3. Mixed Shapes", font_size=36)
        slide3_title.next_to(header, DOWN, buff=0.5)
        
        mix1 = Circle(color=RED, radius=0.5).shift(LEFT * 3 + DOWN * 0.5)
        mix2 = Square(color=BLUE, side_length=1).shift(LEFT * 1 + DOWN * 0.5)
        mix3 = Triangle(color=GREEN).shift(RIGHT * 1 + DOWN * 0.5)
        mix4 = Rectangle(color=YELLOW, width=1.5, height=1).shift(RIGHT * 3 + DOWN * 0.5)
        
        desc3 = Text("Combining different geometric shapes", font_size=24)
        desc3.to_edge(DOWN)
        
        self.play(FadeIn(slide3_title))
        self.play(ShowCreation(mix1))
        self.play(ShowCreation(mix2))
        self.play(ShowCreation(mix3))
        self.play(ShowCreation(mix4))
        self.add(desc3)
        self.wait(2)
        
        # Final slide: Thank you
        self.clear_all_except(header)
        
        thanks = Text("Thank you!", font_size=60, color=GREEN)
        thanks.move_to(ORIGIN)
        
        subtext = Text("Demo of clear_all_except()", font_size=30)
        subtext.next_to(thanks, DOWN)
        
        self.play(FadeIn(thanks))
        self.play(FadeIn(subtext))
        self.wait(2)
        
        # Show how many times we used clear_all_except
        info = Text("Used clear_all_except() 4 times!", font_size=24, color=YELLOW)
        info.to_edge(DOWN)
        self.add(info)
        self.wait(2)


class WorkflowExample(Scene):
    """
    Example: Iterative development workflow where you keep some
    reference objects while experimenting with others
    """
    
    def construct(self):
        # Setup: Create reference grid and labels
        title = Text("Development Workflow", font_size=40).to_edge(UP)
        self.add(title)
        
        # Add reference axes (keep these throughout)
        ref_text = Text("Reference Objects (kept)", font_size=24, color=BLUE)
        ref_text.next_to(title, DOWN)
        self.add(ref_text)
        
        # Version 1: Testing circles
        info1 = Text("v1: Testing circles", font_size=30)
        info1.to_edge(DOWN)
        self.add(info1)
        
        circles = [
            Circle(color=RED, radius=0.3).shift(LEFT * 2),
            Circle(color=RED, radius=0.5),
            Circle(color=RED, radius=0.4).shift(RIGHT * 2),
        ]
        self.add(*circles)
        self.wait(1)
        
        # Keep only reference objects, try new design
        self.clear_all_except(title, ref_text)
        
        info2 = Text("v2: Testing squares", font_size=30)
        info2.to_edge(DOWN)
        self.add(info2)
        
        squares = [
            Square(color=BLUE, side_length=0.6).shift(LEFT * 2 + UP * 0.5),
            Square(color=BLUE, side_length=1).shift(UP * 0.5),
            Square(color=BLUE, side_length=0.8).shift(RIGHT * 2 + UP * 0.5),
        ]
        self.add(*squares)
        self.wait(1)
        
        # Keep reference, try another design
        self.clear_all_except(title, ref_text)
        
        info3 = Text("v3: Final design", font_size=30)
        info3.to_edge(DOWN)
        self.add(info3)
        
        final = [
            Circle(color=GREEN, radius=0.5).shift(LEFT * 2),
            Square(color=YELLOW, side_length=1),
            Triangle(color=PURPLE).shift(RIGHT * 2),
        ]
        self.add(*final)
        self.wait(2)
        
        # Show completion
        self.clear_all_except(title)
        complete = Text("Efficient workflow with\nclear_all_except()!", 
                       font_size=36, color=GREEN)
        complete.move_to(ORIGIN)
        self.add(complete)
        self.wait(2)


if __name__ == "__main__":
    import sys
    
    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLES OF clear_all_except()")
    print("=" * 70)
    
    try:
        print("\n1. Running PresentationScene (slide-based presentation)...")
        scene1 = PresentationScene(skip_animations=True)
        scene1.run()
        print("   ✓ PresentationScene completed")
        
        print("\n2. Running WorkflowExample (iterative development)...")
        scene2 = WorkflowExample(skip_animations=True)
        scene2.run()
        print("   ✓ WorkflowExample completed")
        
        print("\n" + "=" * 70)
        print("PRACTICAL EXAMPLES COMPLETED SUCCESSFULLY! ✓")
        print("=" * 70)
        print("\nThese examples demonstrate how clear_all_except() simplifies:")
        print("  • Multi-slide presentations")
        print("  • Iterative design workflows")
        print("  • Keeping persistent UI elements")
        print("  • Clean scene transitions")
        
    except Exception as e:
        print(f"\n✗ Example failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
