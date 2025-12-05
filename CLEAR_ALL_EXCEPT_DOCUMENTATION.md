# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes. This method provides a convenient way to clear all objects from the scene while keeping only specified objects.

## Location

- **File 1:** `manimlib/scene/scene.py` (Base Scene class)
- **File 2:** `manimlib/scene/interactive_scene.py` (InteractiveScene class)

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene
    
    Returns:
        self: Returns the scene object for method chaining
    """
```

## How It Works

The method performs two simple operations:
1. **Clear:** Removes all mobjects from the scene using `self.clear()`
2. **Add Back:** Adds back only the specified mobjects using `self.add(*mobjects_to_keep)`

## Usage Examples

### Example 1: Basic Usage in Scene

```python
from manimlib import *

class ClearAllExceptExample(Scene):
    def construct(self):
        # Create multiple objects
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only the circle
        self.clear_all_except(circle)
        self.wait(1)
```

### Example 2: Keeping Multiple Objects

```python
from manimlib import *

class KeepMultipleExample(Scene):
    def construct(self):
        # Create objects
        title = Text("Title").to_edge(UP)
        circle = Circle()
        square = Square()
        triangle = Triangle()
        footer = Text("Footer").to_edge(DOWN)
        
        # Add all
        self.add(title, circle, square, triangle, footer)
        self.wait(1)
        
        # Keep only title and footer
        self.clear_all_except(title, footer)
        self.wait(1)
```

### Example 3: Clear Everything

```python
from manimlib import *

class ClearEverythingExample(Scene):
    def construct(self):
        # Add objects
        self.add(Circle(), Square(), Triangle())
        self.wait(1)
        
        # Clear everything (no arguments)
        self.clear_all_except()
        self.wait(1)
```

### Example 4: Method Chaining

```python
from manimlib import *

class MethodChainingExample(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        
        # Add initial objects
        self.add(circle, square, triangle)
        self.wait(0.5)
        
        # Chain methods: clear all except circle, then add new object
        new_square = Square(color=YELLOW).shift(RIGHT * 2)
        self.clear_all_except(circle).add(new_square)
        self.wait(1)
```

### Example 5: InteractiveScene Usage

```python
from manimlib import *

class InteractiveClearExample(InteractiveScene):
    def construct(self):
        # Create objects
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        
        # Add objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only circle and square
        # Note: Selection features remain intact after clear_all_except
        self.clear_all_except(circle, square)
        self.wait(1)
```

## Important Notes

### Scene Class
- The `Scene` class maintains a camera frame in the mobjects list by default
- Calling `clear_all_except()` with no arguments will remove everything, including the camera frame
- This is consistent with the behavior of the `clear()` method

### InteractiveScene Class
- The `InteractiveScene` has additional UI elements (selection highlights, etc.)
- `clear_all_except()` removes ALL mobjects when called with no arguments, including UI elements
- After calling `clear_all_except()`, the `selection_search_set` is automatically regenerated
- This ensures that selection features continue to work correctly with the remaining objects

### Method Chaining
Both implementations return `self`, allowing for method chaining:
```python
self.clear_all_except(obj1, obj2).add(obj3)
```

### Duplicate Objects
If you pass the same object multiple times to `clear_all_except()`, it will be added multiple times (consistent with the behavior of `add()`):
```python
# This will add circle three times to the scene
self.clear_all_except(circle, circle, circle)
```

### Non-existent Objects
If you pass objects that weren't in the scene to `clear_all_except()`, they will be added to the scene:
```python
scene.add(circle)
# square wasn't in the scene, but it gets added
scene.clear_all_except(circle, square)
```

## Implementation Details

### Scene Implementation (scene.py)
```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene
    
    Returns:
        self: Returns the scene object for method chaining
    """
    self.clear()
    self.add(*mobjects_to_keep)
    return self
```

### InteractiveScene Implementation (interactive_scene.py)
```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from the scene and adds back only the ones
    specified in the argument list. Also regenerates the selection
    search set for interactive features.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene
    
    Returns:
        self: Returns the scene object for method chaining
    """
    super().clear_all_except(*mobjects_to_keep)
    self.regenerate_selection_search_set()
    return self
```

The key difference is that `InteractiveScene` calls `regenerate_selection_search_set()` to ensure that interactive selection features continue to work properly after clearing.

## Testing

Comprehensive tests are provided in `test_clear_all_except_unit.py`. To run the tests:

```bash
xvfb-run -a python test_clear_all_except_unit.py
```

The tests verify:
- Basic functionality in both Scene and InteractiveScene
- Keeping specific objects
- Clearing everything
- Keeping multiple objects
- Method chaining
- Edge cases (empty scenes, duplicates, non-existent objects)
- Selection search set regeneration in InteractiveScene

## Performance

The method is decorated with `@affects_mobject_list` which ensures that:
1. The render groups are reassembled after the operation
2. The operation is atomic and maintains scene consistency

This means the method is efficient and safe to use even with large numbers of objects.
