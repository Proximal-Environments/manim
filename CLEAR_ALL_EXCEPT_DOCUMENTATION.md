# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all mobjects from the scene while preserving specific objects that you want to keep.

## Location

- **File 1**: `manimlib/scene/scene.py` (Scene class)
- **File 2**: `manimlib/scene/interactive_scene.py` (InteractiveScene class)

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject)
```

### Parameters

- `*mobjects_to_keep`: Variable number of Mobject arguments representing the objects to keep on screen. All other mobjects will be removed from the scene.

### Returns

- `self`: Returns the scene instance for method chaining.

## Features

### Scene.clear_all_except()

- Removes all mobjects from the scene except those specified in the arguments
- Preserves the camera frame automatically
- Marked with `@affects_mobject_list` decorator to ensure render groups are properly reassembled
- Can be called with no arguments to clear everything (equivalent to `clear()`)

### InteractiveScene.clear_all_except()

- Extends the base Scene functionality
- Properly handles the selection system:
  - Clears selection if selected objects are being removed
  - Regenerates the selection search set after clearing
  - Maintains compatibility with interactive features
- Preserves interactive UI elements (selection highlight, etc.)

## Usage Examples

### Example 1: Basic Usage

```python
class MyScene(Scene):
    def construct(self):
        # Create several objects
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        # Add all to scene
        self.add(circle, square, triangle)
        
        # Remove all except the square
        self.clear_all_except(square)
        # Now only square remains on screen
```

### Example 2: Keeping Multiple Objects

```python
class MyScene(Scene):
    def construct(self):
        # Create objects
        title = Text("My Title").to_edge(UP)
        circle = Circle()
        square = Square()
        label = Text("Label").to_edge(DOWN)
        
        self.add(title, circle, square, label)
        
        # Keep title and label, remove shapes
        self.clear_all_except(title, label)
```

### Example 3: Working with Groups

```python
class MyScene(Scene):
    def construct(self):
        # Create groups
        group1 = VGroup(Circle(), Square())
        group2 = VGroup(Triangle(), Dot())
        background = Rectangle()
        
        self.add(background, group1, group2)
        
        # Keep only group2
        self.clear_all_except(group2)
        # Only group2 and its children remain
```

### Example 4: Clear Everything

```python
class MyScene(Scene):
    def construct(self):
        # Add many objects
        self.add(Circle(), Square(), Triangle())
        
        # Clear all mobjects
        self.clear_all_except()
        
        # Scene is now empty (except camera frame)
        # Can add new objects
        self.add(Text("Fresh start!"))
```

### Example 5: Interactive Scene

```python
class MyScene(InteractiveScene):
    def construct(self):
        # Create objects
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        self.add(circle, square, triangle)
        
        # Selection system is automatically handled
        self.clear_all_except(square)
        
        # Selection search set is regenerated
        # Interactive features still work properly
```

### Example 6: Animation Workflow

```python
class MyScene(Scene):
    def construct(self):
        # Scene 1
        title1 = Text("Scene 1")
        objects1 = VGroup(Circle(), Square())
        self.add(title1, objects1)
        self.play(FadeIn(objects1))
        self.wait()
        
        # Transition - keep title, remove objects
        self.clear_all_except(title1)
        
        # Scene 2
        title1.become(Text("Scene 2"))
        objects2 = VGroup(Triangle(), Dot())
        self.play(FadeIn(objects2))
        self.wait()
```

## Implementation Details

### Scene Implementation

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all mobjects from the scene except those specified in the argument list.
    The specified mobjects are kept on screen.
    """
    # Store the mobjects we want to keep
    to_keep = list(mobjects_to_keep)
    # Clear all mobjects
    self.mobjects = []
    # Add back the ones we want to keep
    if to_keep:
        self.mobjects = to_keep
    return self
```

### InteractiveScene Implementation

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all mobjects from the scene except those specified in the argument list.
    The specified mobjects are kept on screen. This method also handles the selection
    properly for InteractiveScene.
    """
    # Use parent class method but handle selection properly
    kept_mobs = set(mobjects_to_keep)
    # Clear selection if any selected mobject is being removed
    for mob in list(self.selection):
        if mob not in kept_mobs and mob not in [m for km in kept_mobs for m in km.get_family()]:
            self.clear_selection()
            break
    # Call parent method
    result = super().clear_all_except(*mobjects_to_keep)
    # Regenerate selection search set
    self.regenerate_selection_search_set()
    return result
```

## Comparison with Other Methods

| Method | Purpose | When to Use |
|--------|---------|-------------|
| `clear()` | Removes all mobjects | When you want a completely empty scene |
| `clear_all_except(obj1, obj2, ...)` | Removes all except specified | When you want to keep some specific objects |
| `remove(obj1, obj2, ...)` | Removes specific mobjects | When you know exactly what to remove |
| `add(obj)` | Adds mobjects | When adding new objects |

## Benefits

1. **Convenience**: Single method call instead of removing objects one by one
2. **Clarity**: Code intention is clear - "keep these, remove everything else"
3. **Safety**: Automatically handles scene state and render groups
4. **Interactive Support**: Works seamlessly with InteractiveScene's selection system
5. **Flexible**: Can keep any number of objects, including zero (clear all)

## Testing

Comprehensive tests have been written and pass successfully:

```bash
# Run tests with xvfb-run to handle display issues
xvfb-run -a python test_clear_all_except.py
```

Test coverage includes:
- Basic functionality with Scene
- Basic functionality with InteractiveScene
- Keeping multiple objects
- Clearing everything (no arguments)
- Working with groups
- Selection system handling in InteractiveScene

## Notes

- The camera frame is automatically preserved (it's part of the scene structure)
- In InteractiveScene, internal UI elements (selection highlight, etc.) are handled automatically
- The method returns `self` for method chaining
- The `@affects_mobject_list` decorator ensures render groups are properly updated

## Version

Added in: Current development version

## See Also

- `Scene.clear()` - Clear all mobjects
- `Scene.add()` - Add mobjects to scene
- `Scene.remove()` - Remove specific mobjects
- `InteractiveScene.clear_selection()` - Clear selected objects in interactive mode
