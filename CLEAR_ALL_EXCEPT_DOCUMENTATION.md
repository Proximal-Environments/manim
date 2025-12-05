# clear_all_except Method Documentation

## Overview

The `clear_all_except` method has been added to both `Scene` and `InteractiveScene` classes to provide a convenient way to remove all mobjects from the scene except for specified ones.

## Location

- **File 1:** `manimlib/scene/scene.py` (Base Scene class)
- **File 2:** `manimlib/scene/interactive_scene.py` (InteractiveScene class)

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all objects from the scene and adds back the ones given 
    in the argument list of objects to keep.
    
    Only mobjects that were already in the scene will be kept.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene
        
    Returns:
        self (for method chaining)
    """
```

## Behavior

### In Scene class:
1. Filters the provided mobjects to only include those currently in the scene
2. Clears all mobjects from the scene
3. Adds back only the filtered mobjects
4. Triggers `affects_mobject_list` decorator to reassemble render groups

### In InteractiveScene class (additional behavior):
1. Clears the current selection (if any)
2. Calls the parent `Scene.clear_all_except` method
3. Regenerates the selection search set

## Usage Examples

### Basic Usage

```python
from manimlib import Scene
from manimlib.mobject.geometry import Circle, Square, Triangle
from manimlib.constants import RED, BLUE, GREEN, LEFT, RIGHT

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        
        # Add all objects
        self.add(circle, square, triangle)
        self.wait(1)
        
        # Keep only the square
        self.clear_all_except(square)
        self.wait(1)
```

### Keeping Multiple Objects

```python
# Keep multiple objects
self.clear_all_except(square, circle)
```

### Clearing Everything

```python
# Clear everything (equivalent to self.clear())
self.clear_all_except()
```

### With Groups

```python
from manimlib.mobject.mobject import Group

# Create a group
group = Group(circle, square)
self.add(group, triangle)

# Keep only the group (the group itself, not its members)
self.clear_all_except(group)
```

### In InteractiveScene

```python
from manimlib import InteractiveScene

class MyInteractiveScene(InteractiveScene):
    def construct(self):
        circle = Circle(color=RED).shift(LEFT)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT)
        
        self.add(circle, square, triangle)
        
        # Add some objects to selection
        self.add_to_selection(circle, triangle)
        
        # Clear all except square (also clears selection)
        self.clear_all_except(square)
        
        # Selection is now empty
        assert len(self.selection) == 0
```

## Edge Cases

### Objects Not in Scene

If you pass objects that aren't currently in the scene, they will be ignored:

```python
circle = Circle()
square = Square()

self.add(circle)
# square is not in the scene
self.clear_all_except(square)
# Result: both circle and square are removed (scene is empty)
```

### Duplicate Arguments

Duplicate objects in the arguments are handled gracefully:

```python
self.clear_all_except(circle, circle, circle)
# Same as: self.clear_all_except(circle)
```

### Empty Scene

Works correctly on an empty scene:

```python
self.clear_all_except()  # No effect on empty scene
```

## Comparison with Other Methods

| Method | Description |
|--------|-------------|
| `clear()` | Removes all mobjects from the scene |
| `remove(*mobjects)` | Removes specific mobjects (supports family removal) |
| `clear_all_except(*mobjects)` | Removes all mobjects except specified ones |

## Implementation Details

### Decorator

The method uses the `@affects_mobject_list` decorator, which:
- Ensures render groups are reassembled after the operation
- Returns `self` for method chaining

### Scene Class Implementation

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    # Filter to only keep mobjects that are currently in the scene
    to_keep = [mob for mob in mobjects_to_keep if mob in self.mobjects]
    # Clear all mobjects
    self.mobjects = []
    # Add back the mobjects we want to keep
    if to_keep:
        self.add(*to_keep)
    return self
```

### InteractiveScene Class Implementation

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    # Clear the selection first
    self.clear_selection()
    # Call parent's clear_all_except
    super().clear_all_except(*mobjects_to_keep)
    # Regenerate selection search set
    self.regenerate_selection_search_set()
    return self
```

## Testing

Comprehensive tests have been created:

1. **test_clear_all_except.py**: Basic functionality tests
2. **test_edge_cases.py**: Edge case and boundary condition tests
3. **demo_clear_all_except.py**: Visual demonstration

Run tests with:
```bash
xvfb-run -a python test_clear_all_except.py
xvfb-run -a python test_edge_cases.py
```

## Benefits

1. **Convenience**: Single method call instead of multiple remove operations
2. **Performance**: More efficient than removing objects one by one
3. **Clarity**: Intent is clear from the method name
4. **Consistency**: Works the same way in both Scene and InteractiveScene
5. **Safety**: Handles edge cases gracefully

## Notes

- The method returns `self` to support method chaining
- Only mobjects that were in the scene before the call will be kept
- In InteractiveScene, the selection is always cleared
- The method respects the z-index ordering when re-adding objects
