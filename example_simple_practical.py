#!/usr/bin/env python
"""
Simple practical example without LaTeX dependencies
Demonstrates real-world use cases for clear_all_except
"""

from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Rectangle, Line, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import *


class AnimationStoryboard(Scene):
    """
    Example: Creating a storyboard where we keep a title
    but transition through different scenes
    """
    
    def construct(self):
        # Persistent title
        title = Text("Animation Storyboard", font_size=42)
        title.to_edge(UP)
        self.add(title)
        self.wait(0.3)
        
        # Scene 1: Introduction
        scene1_label = Text("Scene 1: Introduction", font_size=30)
        scene1_label.next_to(title, DOWN, buff=0.5)
        
        circle = Circle(radius=1, color=BLUE)
        circle.shift(DOWN * 0.5)
        
        self.add(scene1_label, circle)
        print("✓ Scene 1: Introduction with circle")
        self.wait(1)
        
        # Clear everything except title, add scene 2
        self.clear_all_except(title)
        
        scene2_label = Text("Scene 2: Transformation", font_size=30)
        scene2_label.next_to(title, DOWN, buff=0.5)
        
        square = Square(side_length=1.5, color=RED)
        square.shift(DOWN * 0.5)
        
        self.add(scene2_label, square)
        print("✓ Scene 2: Transformation to square")
        self.wait(1)
        
        # Clear everything except title, add scene 3
        self.clear_all_except(title)
        
        scene3_label = Text("Scene 3: Multiple Objects", font_size=30)
        scene3_label.next_to(title, DOWN, buff=0.5)
        
        shapes = [
            Triangle(color=GREEN).shift(LEFT * 2 + DOWN * 0.5),
            Circle(radius=0.5, color=YELLOW).shift(DOWN * 0.5),
            Square(side_length=0.8, color=PURPLE).shift(RIGHT * 2 + DOWN * 0.5)
        ]
        
        self.add(scene3_label, *shapes)
        print("✓ Scene 3: Multiple objects")
        self.wait(1)
        
        # Final: Keep only title
        self.clear_all_except(title)
        
        end_text = Text("End", font_size=48, color=GREEN)
        end_text.next_to(title, DOWN, buff=2)
        self.add(end_text)
        print("✓ Storyboard complete")
        self.wait(1)


class ProgressiveReveal(Scene):
    """
    Example: Progressively revealing information while
    keeping a reference diagram visible
    """
    
    def construct(self):
        # Create a reference diagram that stays visible
        reference = Rectangle(width=3, height=2, color=GREY)
        reference.to_edge(LEFT)
        
        ref_label = Text("Reference", font_size=24)
        ref_label.next_to(reference, UP, buff=0.2)
        
        self.add(reference, ref_label)
        print("✓ Reference diagram added")
        self.wait(0.5)
        
        # Step 1
        step1 = Text("Step 1: Setup", font_size=32)
        step1.to_edge(RIGHT).shift(UP * 2)
        
        shapes1 = [
            Circle(radius=0.3, color=RED).shift(RIGHT * 2 + UP),
            Circle(radius=0.3, color=BLUE).shift(RIGHT * 3 + UP)
        ]
        
        self.add(step1, *shapes1)
        print("✓ Step 1 displayed")
        self.wait(1)
        
        # Keep reference, show step 2
        self.clear_all_except(reference, ref_label)
        
        step2 = Text("Step 2: Connect", font_size=32)
        step2.to_edge(RIGHT).shift(UP * 2)
        
        line = Line(
            reference.get_right(),
            reference.get_right() + RIGHT * 2,
            color=YELLOW
        )
        
        self.add(step2, line)
        print("✓ Step 2 displayed")
        self.wait(1)
        
        # Keep reference, show step 3
        self.clear_all_except(reference, ref_label)
        
        step3 = Text("Step 3: Result", font_size=32)
        step3.to_edge(RIGHT).shift(UP * 2)
        
        result = Square(side_length=1, color=GREEN)
        result.shift(RIGHT * 3)
        
        self.add(step3, result)
        print("✓ Step 3 displayed")
        self.wait(1)
        
        # Final summary with reference
        self.clear_all_except(reference, ref_label, result)
        
        summary = Text("Complete!", font_size=36, color=GREEN)
        summary.shift(UP * 2.5)
        
        self.add(summary)
        print("✓ Progressive reveal complete")
        self.wait(1)


class SelectiveCleanup(Scene):
    """
    Example: Cleaning up construction lines while keeping
    the final result
    """
    
    def construct(self):
        # Title
        title = Text("Selective Cleanup Demo", font_size=40)
        title.to_edge(UP)
        self.add(title)
        
        # Step 1: Draw construction elements
        label = Text("Drawing with construction lines", font_size=28)
        label.next_to(title, DOWN, buff=0.5)
        self.add(label)
        self.wait(0.3)
        
        # Construction lines (temporary)
        h_line = Line(LEFT * 3, RIGHT * 3, color=GREY, stroke_width=1)
        v_line = Line(UP * 2, DOWN * 2, color=GREY, stroke_width=1)
        
        # Main objects (to keep)
        main_square = Square(side_length=2, color=BLUE)
        
        self.add(h_line, v_line, main_square)
        print("✓ Construction lines and main object added")
        self.wait(1)
        
        # Clean up: remove construction lines, keep main object
        self.remove(label)
        label = Text("Removing construction lines", font_size=28)
        label.next_to(title, DOWN, buff=0.5)
        self.add(label)
        self.wait(0.3)
        
        self.clear_all_except(title, label, main_square)
        print("✓ Construction lines removed")
        self.wait(1)
        
        # Add detail to the final object
        self.remove(label)
        label = Text("Adding final details", font_size=28)
        label.next_to(title, DOWN, buff=0.5)
        self.add(label)
        
        inner_circle = Circle(radius=0.5, color=RED)
        self.add(inner_circle)
        print("✓ Final details added")
        self.wait(1)
        
        # Show final result only
        self.clear_all_except(title, main_square, inner_circle)
        
        final_label = Text("Final Result", font_size=32, color=GREEN)
        final_label.to_edge(DOWN)
        self.add(final_label)
        print("✓ Cleanup complete")
        self.wait(1)


if __name__ == "__main__":
    import sys
    
    examples = [
        ("Animation Storyboard", AnimationStoryboard),
        ("Progressive Reveal", ProgressiveReveal),
        ("Selective Cleanup", SelectiveCleanup)
    ]
    
    for name, scene_class in examples:
        print("\n" + "=" * 70)
        print(f"Running: {name}")
        print("=" * 70)
        
        scene = scene_class(
            skip_animations=True,
            show_animation_progress=False
        )
        
        try:
            scene.run()
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    
    print("\n" + "=" * 70)
    print("🎉 All practical examples completed successfully!")
    print("=" * 70)
    print("\nKey Benefits Demonstrated:")
    print("  ✓ Maintaining persistent UI elements (titles, references)")
    print("  ✓ Clean scene transitions between different states")
    print("  ✓ Removing temporary construction elements")
    print("  ✓ Progressive information reveal with context")
    print("  ✓ Simplified scene management code")
