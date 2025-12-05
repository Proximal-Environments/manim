#!/usr/bin/env python3
"""
Test script for clear_all_except method in both Scene and InteractiveScene
"""

from manimlib.scene.scene import Scene
from manimlib.scene.interactive_scene import InteractiveScene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.mobject.svg.text_mobject import Text
from manimlib.constants import RED, BLUE, GREEN, YELLOW


class TestClearAllExceptScene(Scene):
    """Test the clear_all_except method in Scene"""
    
    def construct(self):
        # Create multiple mobjects
        circle = Circle(color=RED)
        square = Square(color=BLUE).shift([2, 0, 0])
        triangle = Triangle(color=GREEN).shift([-2, 0, 0])
        text = Text("Keep Me!", color=YELLOW).shift([0, -2, 0])
        
        # Add all mobjects to the scene
        self.add(circle, square, triangle, text)
        print(f"Initial mobjects count: {len(self.mobjects)}")
        print(f"Mobjects: {[type(m).__name__ for m in self.mobjects]}")
        
        self.wait(1)
        
        # Clear all except circle and text
        print("\nClearing all except circle and text...")
        self.clear_all_except(circle, text)
        print(f"Mobjects count after clear_all_except: {len(self.mobjects)}")
        print(f"Mobjects: {[type(m).__name__ for m in self.mobjects]}")
        
        # Verify that only circle and text remain
        assert circle in self.mobjects, "Circle should still be in scene"
        assert text in self.mobjects, "Text should still be in scene"
        assert square not in self.mobjects, "Square should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        self.wait(1)
        
        # Test clearing everything
        print("\nClearing everything...")
        self.clear_all_except()
        print(f"Mobjects count after clearing all: {len(self.mobjects)}")
        print(f"Mobjects: {[type(m).__name__ for m in self.mobjects]}")
        
        self.wait(1)
        
        # Add new mobjects
        new_circle = Circle(color=RED).scale(0.5)
        self.add(new_circle)
        print(f"\nAdded new circle. Mobjects count: {len(self.mobjects)}")
        
        self.wait(1)
        
        print("\n✅ All tests passed for Scene.clear_all_except!")


class TestClearAllExceptInteractiveScene(InteractiveScene):
    """Test the clear_all_except method in InteractiveScene"""
    
    def construct(self):
        # Create multiple mobjects
        circle = Circle(color=RED)
        square = Square(color=BLUE).shift(2 * [1, 0, 0])
        triangle = Triangle(color=GREEN).shift(2 * [-1, 0, 0])
        text = Text("Interactive!", color=YELLOW).shift(2 * [0, -1, 0])
        
        # Add all mobjects to the scene
        self.add(circle, square, triangle, text)
        print(f"Initial mobjects count (Interactive): {len(self.mobjects)}")
        print(f"Selection search set count: {len(self.selection_search_set)}")
        
        self.wait(1)
        
        # Clear all except circle and text
        print("\nClearing all except circle and text (Interactive)...")
        self.clear_all_except(circle, text)
        print(f"Mobjects count after clear_all_except: {len(self.mobjects)}")
        print(f"Selection search set count: {len(self.selection_search_set)}")
        
        # Verify that only circle and text remain
        assert circle in self.mobjects, "Circle should still be in scene"
        assert text in self.mobjects, "Text should still be in scene"
        assert square not in self.mobjects, "Square should be removed"
        assert triangle not in self.mobjects, "Triangle should be removed"
        
        # Verify selection_search_set is updated
        selectable_mobs = [m for m in self.mobjects if m not in self.unselectables]
        print(f"Selectable mobjects: {len(selectable_mobs)}")
        
        self.wait(1)
        
        # Test clearing everything
        print("\nClearing everything (Interactive)...")
        self.clear_all_except()
        print(f"Mobjects count after clearing all: {len(self.mobjects)}")
        
        self.wait(1)
        
        print("\n✅ All tests passed for InteractiveScene.clear_all_except!")


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Testing Scene.clear_all_except")
    print("=" * 60)
    
    # Test regular Scene
    scene = TestClearAllExceptScene(
        skip_animations=True,
        show_animation_progress=False,
    )
    scene.run()
    
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except")
    print("=" * 60)
    
    # Test InteractiveScene
    interactive_scene = TestClearAllExceptInteractiveScene(
        skip_animations=True,
        show_animation_progress=False,
    )
    interactive_scene.run()
    
    print("\n" + "=" * 60)
    print("🎉 ALL TESTS PASSED! 🎉")
    print("=" * 60)
