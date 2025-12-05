#!/usr/bin/env python
"""Quick demonstration of the clear_all_except method"""

from manimlib import *

class QuickDemo(Scene):
    """Quick demonstration of clear_all_except"""
    
    def construct(self):
        # Create objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        text = Text("Keep Me!", font_size=24).to_edge(UP)
        
        # Add all
        self.add(circle, square, triangle, text)
        print("Added 4 objects: circle, square, triangle, text")
        
        # Clear all except text and square
        print("Calling clear_all_except(text, square)...")
        self.clear_all_except(text, square)
        
        # Verify
        assert text in self.mobjects, "Text should remain"
        assert square in self.mobjects, "Square should remain"
        assert circle not in self.mobjects, "Circle should be gone"
        assert triangle not in self.mobjects, "Triangle should be gone"
        
        print("✓ Verification passed: only text and square remain")
        print(f"  Current mobjects count: {len([m for m in self.mobjects if m != self.camera.frame])}")


class QuickDemoInteractive(InteractiveScene):
    """Quick interactive demo"""
    
    def construct(self):
        # Create objects
        circle = Circle(color=RED).shift(LEFT * 2)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT * 2)
        
        # Add all
        self.add(circle, square, triangle)
        print("Added 3 objects to InteractiveScene")
        
        # Clear all except square
        print("Calling clear_all_except(square)...")
        self.clear_all_except(square)
        
        # Verify
        regular_mobs = [m for m in self.mobjects 
                       if m not in [self.camera.frame, self.selection_highlight]]
        
        assert square in regular_mobs, "Square should remain"
        assert circle not in self.mobjects, "Circle should be gone"
        assert triangle not in self.mobjects, "Triangle should be gone"
        
        print("✓ Verification passed: only square remains in InteractiveScene")
        print(f"  Selection search set regenerated: {len(self.selection_search_set)} items")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Quick Demo: Scene.clear_all_except()")
    print("=" * 60)
    
    scene1 = QuickDemo()
    scene1.run()
    
    print("\n" + "=" * 60)
    print("Quick Demo: InteractiveScene.clear_all_except()")
    print("=" * 60)
    
    scene2 = QuickDemoInteractive()
    scene2.run()
    
    print("\n" + "=" * 60)
    print("ALL QUICK DEMOS COMPLETED!")
    print("=" * 60 + "\n")
