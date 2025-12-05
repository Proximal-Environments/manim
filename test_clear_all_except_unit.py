#!/usr/bin/env python
"""
Unit tests for the clear_all_except method
"""
from manimlib import *

def test_scene_clear_all_except():
    """Test Scene.clear_all_except() method"""
    print("\n" + "=" * 60)
    print("Testing Scene.clear_all_except()")
    print("=" * 60)
    
    scene = Scene()
    
    # Test 1: Clear all except specific objects
    print("\nTest 1: Keep specific objects")
    circle = Circle()
    square = Square()
    triangle = Triangle()
    
    scene.add(circle, square, triangle)
    initial_count = len(scene.mobjects)
    print(f"  Added 3 objects, mobjects count: {initial_count}")
    assert initial_count == 3, f"Expected 3 mobjects, got {initial_count}"
    
    scene.clear_all_except(circle, triangle)
    after_clear = len(scene.mobjects)
    print(f"  After clear_all_except(circle, triangle): {after_clear}")
    assert after_clear == 2, f"Expected 2 mobjects, got {after_clear}"
    assert circle in scene.mobjects, "Circle should remain"
    assert triangle in scene.mobjects, "Triangle should remain"
    assert square not in scene.mobjects, "Square should be removed"
    print("  ✓ Test 1 passed")
    
    # Test 2: Clear all (no arguments)
    print("\nTest 2: Clear all with no arguments")
    scene.clear_all_except()
    after_clear_all = len(scene.mobjects)
    print(f"  After clear_all_except(): {after_clear_all}")
    assert after_clear_all == 0, f"Expected 0 mobjects, got {after_clear_all}"
    print("  ✓ Test 2 passed")
    
    # Test 3: Keep one object
    print("\nTest 3: Keep only one object")
    dot1 = Dot(color=RED)
    dot2 = Dot(color=BLUE)
    dot3 = Dot(color=GREEN)
    
    scene.add(dot1, dot2, dot3)
    print(f"  Added 3 dots, mobjects count: {len(scene.mobjects)}")
    
    scene.clear_all_except(dot2)
    print(f"  After clear_all_except(dot2): {len(scene.mobjects)}")
    assert len(scene.mobjects) == 1, f"Expected 1 mobject, got {len(scene.mobjects)}"
    assert dot2 in scene.mobjects, "Dot2 should remain"
    assert dot1 not in scene.mobjects, "Dot1 should be removed"
    assert dot3 not in scene.mobjects, "Dot3 should be removed"
    print("  ✓ Test 3 passed")
    
    # Test 4: Method chaining
    print("\nTest 4: Method chaining")
    scene.clear_all_except()
    line1 = Line()
    line2 = Line()
    result = scene.clear_all_except(line1, line2).add(Circle())
    assert result is scene, "Should return self for method chaining"
    assert len(scene.mobjects) == 3, f"Expected 3 mobjects after chaining, got {len(scene.mobjects)}"
    print("  ✓ Test 4 passed")
    
    print("\n" + "=" * 60)
    print("All Scene tests passed! ✓")
    print("=" * 60)


def test_interactive_scene_clear_all_except():
    """Test InteractiveScene.clear_all_except() method"""
    print("\n" + "=" * 60)
    print("Testing InteractiveScene.clear_all_except()")
    print("=" * 60)
    
    scene = InteractiveScene()
    scene.setup()  # Initialize interactive scene components
    
    # Store the initial unselectables count
    initial_unselectables = len(scene.unselectables)
    print(f"Initial unselectables count: {initial_unselectables}")
    
    # Test 1: Clear all except specific objects
    print("\nTest 1: Keep specific objects in InteractiveScene")
    circle = Circle(color=BLUE)
    square = Square(color=RED)
    triangle = Triangle(color=GREEN)
    
    scene.add(circle, square, triangle)
    # Count only user-added mobjects (not UI elements)
    user_mobs = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"  Added 3 objects, user mobjects count: {len(user_mobs)}")
    assert circle in scene.mobjects, "Circle should be in scene"
    assert square in scene.mobjects, "Square should be in scene"
    assert triangle in scene.mobjects, "Triangle should be in scene"
    
    scene.clear_all_except(circle, triangle)
    user_mobs_after = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"  After clear_all_except(circle, triangle): {len(user_mobs_after)}")
    assert circle in scene.mobjects, "Circle should remain"
    assert triangle in scene.mobjects, "Triangle should remain"
    assert square not in scene.mobjects, "Square should be removed"
    print("  ✓ Test 1 passed")
    
    # Test 2: Verify selection_search_set is regenerated
    print("\nTest 2: Verify selection_search_set is regenerated")
    assert hasattr(scene, 'selection_search_set'), "Should have selection_search_set"
    # The search set should only contain selectable objects
    search_set_has_circle = any(circle in mob.get_family() for mob in scene.selection_search_set)
    search_set_has_square = any(square in mob.get_family() for mob in scene.selection_search_set)
    assert search_set_has_circle, "Circle should be in search set"
    assert not search_set_has_square, "Square should not be in search set"
    print("  ✓ Test 2 passed")
    
    # Test 3: Clear all
    print("\nTest 3: Clear all in InteractiveScene")
    scene.clear_all_except()
    user_mobs_final = [m for m in scene.mobjects if m not in scene.unselectables]
    print(f"  After clear_all_except(): user mobjects count: {len(user_mobs_final)}")
    assert len(user_mobs_final) == 0, "All user mobjects should be removed"
    # UI elements should remain
    assert scene.selection_highlight in scene.mobjects or \
           len([m for m in scene.unselectables if m in scene.mobjects]) > 0, \
           "UI elements should remain"
    print("  ✓ Test 3 passed")
    
    # Test 4: Method chaining
    print("\nTest 4: Method chaining in InteractiveScene")
    dot = Dot(color=YELLOW)
    result = scene.clear_all_except(dot)
    assert result is scene, "Should return self for method chaining"
    assert dot in scene.mobjects, "Dot should be in scene after chaining"
    print("  ✓ Test 4 passed")
    
    print("\n" + "=" * 60)
    print("All InteractiveScene tests passed! ✓")
    print("=" * 60)


def test_edge_cases():
    """Test edge cases for clear_all_except"""
    print("\n" + "=" * 60)
    print("Testing Edge Cases")
    print("=" * 60)
    
    # Test with empty scene
    print("\nTest: Clear empty scene")
    scene = Scene()
    scene.clear_all_except()
    assert len(scene.mobjects) == 0, "Empty scene should remain empty"
    print("  ✓ Empty scene test passed")
    
    # Test with duplicate objects in keep list
    print("\nTest: Duplicate objects in keep list")
    scene = Scene()
    circle = Circle()
    scene.add(circle)
    scene.clear_all_except(circle, circle, circle)  # Same object multiple times
    assert len(scene.mobjects) == 1, "Should handle duplicates gracefully"
    assert circle in scene.mobjects, "Circle should remain"
    print("  ✓ Duplicate objects test passed")
    
    # Test with non-existent objects in keep list
    print("\nTest: Non-existent objects in keep list")
    scene = Scene()
    circle = Circle()
    square = Square()
    scene.add(circle)
    scene.clear_all_except(circle, square)  # square is not in scene
    assert circle in scene.mobjects, "Circle should remain"
    # square will be added by the add() call in clear_all_except
    assert square in scene.mobjects, "Square gets added by the add() call"
    print("  ✓ Non-existent objects test passed")
    
    print("\n" + "=" * 60)
    print("All edge case tests passed! ✓")
    print("=" * 60)


if __name__ == "__main__":
    test_scene_clear_all_except()
    test_interactive_scene_clear_all_except()
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED! ✓✓✓")
    print("=" * 60)
