# `clear_all_except` Method Documentation

## Overview

The `clear_all_except` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all objects from the screen while preserving specific objects that you want to keep.

## Location

- **File 1**: `manimlib/scene/scene.py`
- **File 2**: `manimlib/scene/interactive_scene.py`

## Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all objects from screen and adds back the ones given in the argument list.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain on screen after clearing
        
    Returns:
        self: Returns the scene object for method chaining
    """
```

## Usage

### Basic Usage

```python
from manimlib import Scene, Square, Circle, Triangle
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT, UP

class MyScene(Scene):
    def construct(self):
        # Create some objects
        square = Square(color=RED).shift(LEFT)
        circle = Circle(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        
        # Add all objects
        self.add(square, circle, triangle)
        self.wait(1)
        
        # Clear everything except the circle
        self.clear_all_except(circle)
        self.wait(1)
```

### Keeping Multiple Objects

```python
# Keep multiple objects
self.clear_all_except(square, circle)
```

### Clearing Everything

```python
# Clear all objects (equivalent to self.clear())
self.clear_all_except()
```

### Method Chaining

Since the method returns `self`, you can chain it with other methods:

```python
self.clear_all_except(circle).add(new_square).wait(1)
```

## Behavior

### In `Scene` Class

1. Stores the mobjects to keep
2. Clears all mobjects from the scene using `self.clear()`
3. Adds back only the specified mobjects
4. Returns `self` for method chaining

### In `InteractiveScene` Class

The `InteractiveScene` implementation extends the base `Scene` behavior with:

1. Preserves the `selection_highlight` object which is part of the interactive interface
2. Updates the `selection_search_set` after clearing
3. Maintains the proper rendering groups

This ensures that interactive features continue to work correctly after using `clear_all_except`.

## Examples

### Example 1: Scene Transition

```python
class SceneTransition(Scene):
    def construct(self):
        # Scene 1
        obj1 = Circle(color=RED)
        obj2 = Square(color=BLUE)
        self.add(obj1, obj2)
        self.wait(1)
        
        # Transition - keep only obj1
        self.clear_all_except(obj1)
        
        # Scene 2
        obj3 = Triangle(color=GREEN)
        self.add(obj3)
        self.wait(1)
```

### Example 2: Progressive Revelation

```python
class ProgressiveReveal(Scene):
    def construct(self):
        # Title that stays throughout
        title = Text("My Animation").to_edge(UP)
        self.add(title)
        
        # Step 1
        step1_objs = [Circle(), Square()]
        self.add(*step1_objs)
        self.wait(1)
        
        # Clear step 1, keep title
        self.clear_all_except(title)
        
        # Step 2
        step2_objs = [Triangle(), Pentagon()]
        self.add(*step2_objs)
        self.wait(1)
```

### Example 3: Interactive Scene

```python
class InteractiveExample(InteractiveScene):
    def construct(self):
        obj1 = Circle(color=RED)
        obj2 = Square(color=BLUE)
        obj3 = Triangle(color=GREEN)
        
        self.add(obj1, obj2, obj3)
        self.wait(1)
        
        # Clear all except obj2
        # The selection_highlight is automatically preserved
        self.clear_all_except(obj2)
        self.wait(1)
```

## Edge Cases

### Non-existent Objects

Passing objects that aren't in the scene doesn't cause errors - they're simply added:

```python
obj1 = Circle()
obj2 = Square()  # Not added to scene yet

self.add(obj1)
self.clear_all_except(obj1, obj2)  # Works fine, obj2 is added
```

### Empty Scene

Calling `clear_all_except` on an empty scene is safe:

```python
scene = Scene()
scene.clear_all_except()  # No error
```

### Camera Frame

In the base `Scene` class, the camera frame is technically a mobject. When using `clear_all_except`, if you want to keep the camera frame behavior intact, you don't need to explicitly include it - the scene handles this automatically.

## Implementation Details

### Scene Implementation

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from screen and adds back the ones given in the argument list.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain on screen after clearing
    """
    # Store the mobjects to keep
    to_keep = list(mobjects_to_keep)
    # Clear everything
    self.clear()
    # Add back the mobjects to keep
    if to_keep:
        self.add(*to_keep)
    return self
```

### InteractiveScene Implementation

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all objects from screen and adds back the ones given in the argument list.
    This override ensures that the selection highlight is properly maintained.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain on screen after clearing
    """
    # Store the mobjects to keep
    to_keep = list(mobjects_to_keep)
    
    # Preserve the selection highlight if it exists
    has_highlight = self.selection_highlight in self.mobjects
    
    # Clear everything using parent method
    super().clear_all_except(*to_keep)
    
    # Re-add selection highlight if it was there before
    if has_highlight and self.selection_highlight not in self.mobjects:
        self.mobjects.insert(0, self.selection_highlight)
        self.assemble_render_groups()
    
    # Regenerate selection search set
    self.regenerate_selection_search_set()
    
    return self
```

## Comparison with Other Methods

### `clear()` vs `clear_all_except()`

```python
# clear() - removes everything
self.clear()

# clear_all_except() - removes everything except specified objects
self.clear_all_except(obj1, obj2)

# clear_all_except() with no args is equivalent to clear()
self.clear_all_except()  # Same as self.clear()
```

### `remove()` vs `clear_all_except()`

```python
# remove() - removes specific objects
self.remove(obj1, obj2)  # Removes obj1 and obj2, keeps everything else

# clear_all_except() - inverse logic
self.clear_all_except(obj3, obj4)  # Removes everything except obj3 and obj4
```

## Testing

Comprehensive unit tests have been created in `test_clear_all_except_unit.py`. Run tests with:

```bash
xvfb-run -a python test_clear_all_except_unit.py
```

Demo scripts are also available:
- `test_clear_all_except.py` - Basic functionality tests
- `test_interactive_clear_all_except.py` - Interactive scene tests
- `demo_clear_all_except.py` - Visual demonstrations

## Performance Considerations

The method is efficient as it:
1. Uses the existing `clear()` method which is already optimized
2. Uses the existing `add()` method to restore objects
3. The `@affects_mobject_list` decorator ensures render groups are properly assembled

## Troubleshooting

### Issue: Objects disappear unexpectedly

Make sure you're passing the correct object references:

```python
# Correct
obj = Circle()
self.add(obj)
self.clear_all_except(obj)  # obj reference is kept

# Incorrect
self.add(Circle())
self.clear_all_except(Circle())  # This creates a NEW Circle, not the one added
```

### Issue: Interactive features stop working

In `InteractiveScene`, the `selection_highlight` should be automatically preserved. If you experience issues, make sure you're using the `InteractiveScene` class, not the base `Scene` class.

## Future Enhancements

Possible future improvements:
- Add a `clear_all_except_types()` method to keep objects by type
- Add a `clear_all_except_matching()` method with a filter function
- Add animation support for smoother transitions

## Contributing

If you find bugs or have suggestions for improvements, please submit an issue or pull request to the ManimGL repository.
