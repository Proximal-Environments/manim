#!/usr/bin/env python3
"""
Final verification script for clear_all_except implementation
"""

import sys

def test_scene_implementation():
    """Test Scene class implementation"""
    print("Testing Scene.clear_all_except...")
    from manimlib import Scene, Circle, Square, Triangle
    from manimlib.constants import RED, BLUE, GREEN
    
    scene = Scene()
    
    # Test 1: Basic functionality
    c1, c2, c3 = Circle(color=RED), Square(color=BLUE), Triangle(color=GREEN)
    scene.add(c1, c2, c3)
    scene.clear_all_except(c2)
    
    assert c2 in scene.mobjects, "c2 should be in mobjects"
    assert c1 not in scene.mobjects, "c1 should not be in mobjects"
    assert c3 not in scene.mobjects, "c3 should not be in mobjects"
    print("  ✓ Basic functionality works")
    
    # Test 2: Multiple objects
    scene.clear()
    c1, c2, c3 = Circle(color=RED), Square(color=BLUE), Triangle(color=GREEN)
    scene.add(c1, c2, c3)
    scene.clear_all_except(c1, c3)
    
    assert c1 in scene.mobjects, "c1 should be in mobjects"
    assert c3 in scene.mobjects, "c3 should be in mobjects"
    assert c2 not in scene.mobjects, "c2 should not be in mobjects"
    print("  ✓ Multiple objects works")
    
    # Test 3: No arguments (clear all)
    scene.clear_all_except()
    assert len([m for m in scene.mobjects if m in [c1, c2, c3]]) == 0, "All should be cleared"
    print("  ✓ No arguments (clear all) works")
    
    # Test 4: Method chaining
    c1 = Circle(color=RED)
    result = scene.clear_all_except(c1)
    assert result is scene, "Should return self"
    print("  ✓ Method chaining works")
    
    print("✅ Scene.clear_all_except: All tests passed!\n")
    return True

def test_interactive_scene_implementation():
    """Test InteractiveScene class implementation"""
    print("Testing InteractiveScene.clear_all_except...")
    from manimlib import InteractiveScene, Circle, Square, Triangle
    from manimlib.constants import RED, BLUE, GREEN
    
    scene = InteractiveScene()
    scene.setup()
    
    # Test 1: Basic functionality with selection_highlight preservation
    c1, c2, c3 = Circle(color=RED), Square(color=BLUE), Triangle(color=GREEN)
    scene.add(c1, c2, c3)
    
    assert scene.selection_highlight in scene.mobjects, "selection_highlight should be in mobjects"
    
    scene.clear_all_except(c2)
    
    assert c2 in scene.mobjects, "c2 should be in mobjects"
    assert c1 not in scene.mobjects, "c1 should not be in mobjects"
    assert c3 not in scene.mobjects, "c3 should not be in mobjects"
    assert scene.selection_highlight in scene.mobjects, "selection_highlight should still be in mobjects"
    print("  ✓ Basic functionality with selection_highlight preservation works")
    
    # Test 2: Method chaining
    result = scene.clear_all_except(c2)
    assert result is scene, "Should return self"
    print("  ✓ Method chaining works")
    
    print("✅ InteractiveScene.clear_all_except: All tests passed!\n")
    return True

def test_method_exists():
    """Test that the method exists in both classes"""
    print("Checking method existence...")
    from manimlib import Scene, InteractiveScene
    
    assert hasattr(Scene, 'clear_all_except'), "Scene should have clear_all_except method"
    assert callable(getattr(Scene, 'clear_all_except')), "Scene.clear_all_except should be callable"
    print("  ✓ Scene.clear_all_except exists")
    
    assert hasattr(InteractiveScene, 'clear_all_except'), "InteractiveScene should have clear_all_except method"
    assert callable(getattr(InteractiveScene, 'clear_all_except')), "InteractiveScene.clear_all_except should be callable"
    print("  ✓ InteractiveScene.clear_all_except exists")
    
    print("✅ Method existence: All checks passed!\n")
    return True

def main():
    """Run all verification tests"""
    print("=" * 60)
    print("FINAL VERIFICATION: clear_all_except Implementation")
    print("=" * 60)
    print()
    
    tests = [
        ("Method Existence", test_method_exists),
        ("Scene Implementation", test_scene_implementation),
        ("InteractiveScene Implementation", test_interactive_scene_implementation),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result, None))
        except Exception as e:
            results.append((name, False, str(e)))
            print(f"❌ {name}: FAILED")
            print(f"   Error: {e}\n")
    
    print("=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, passed, error in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {name}")
        if error:
            print(f"  Error: {error}")
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("✅ ALL VERIFICATIONS PASSED!")
        print("=" * 60)
        print()
        print("The clear_all_except method has been successfully implemented!")
        print("You can now use it in your ManimGL scenes.")
        print()
        print("Quick example:")
        print("  scene.clear_all_except(obj1, obj2)")
        return 0
    else:
        print("❌ SOME VERIFICATIONS FAILED!")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
