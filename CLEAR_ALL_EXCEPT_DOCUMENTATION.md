# clear_all_except() Method Documentation

## Overview

The `clear_all_except()` method has been added to both `Scene` and `InteractiveScene` classes in ManimGL. This method provides a convenient way to clear all mobjects from the scene while keeping only specified objects.

## Location

- **File 1**: `manimlib/scene/scene.py` (Scene class)
- **File 2**: `manimlib/scene/interactive_scene.py` (InteractiveScene class)

## Method Signature

```python
def clear_all_except(self, *mobjects_to_keep: Mobject) -> Scene:
    """
    Clears all mobjects from the scene and adds back only the specified ones.
    Duplicate mobjects in the argument list are handled gracefully (only added once).
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene after clearing
        
    Returns:
        self: Returns the scene instance for method chaining
    """
```

## Features

1. **Clears all mobjects**: Removes all objects from the scene
2. **Selective retention**: Adds back only the specified mobjects
3. **No duplicates**: Handles duplicate arguments gracefully
4. **Method chaining**: Returns `self` to allow chaining with other methods
5. **InteractiveScene support**: Automatically updates selection search sets

## Usage Examples

### Basic Usage

```python
from manimlib import *

class BasicExample(Scene):
    def construct(self):
        # Create objects
        circle = Circle(color=RED)
        square = Square(color=BLUE)
        triangle = Triangle(color=GREEN)
        
        # Add all to scene
        self.add(circle, square, triangle)
        self.wait()
        
        # Keep only the circle
        self.clear_all_except(circle)
        self.wait()
```

### Keeping Multiple Objects

```python
class KeepMultiple(Scene):
    def construct(self):
        title = Text("Title")
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        self.add(title, circle, square, triangle)
        self.wait()
        
        # Keep title and circle
        self.clear_all_except(title, circle)
        self.wait()
```

### Clearing Everything

```python
class ClearAll(Scene):
    def construct(self):
        # Add some objects
        self.add(Circle(), Square(), Triangle())
        self.wait()
        
        # Clear everything
        self.clear_all_except()
        self.wait()
```

### Method Chaining

```python
class ChainedExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Chain multiple operations
        self.add(circle, square, triangle) \
            .clear_all_except(circle) \
            .add(square)
```

### Practical Use Case: Multi-Stage Visualization

```python
class MultiStageVisualization(Scene):
    def construct(self):
        # Persistent title
        title = Text("My Visualization").to_edge(UP)
        self.add(title)
        
        # Stage 1
        stage1_label = Text("Stage 1").next_to(title, DOWN)
        self.add(stage1_label)
        
        graph1 = self.get_graph_1()
        self.add(graph1)
        self.wait()
        
        # Transition to Stage 2 - keep only title
        self.clear_all_except(title)
        
        stage2_label = Text("Stage 2").next_to(title, DOWN)
        self.add(stage2_label)
        
        graph2 = self.get_graph_2()
        self.add(graph2)
        self.wait()
```

### InteractiveScene Usage

```python
class InteractiveExample(InteractiveScene):
    def construct(self):
        # Create objects
        objects = [Circle(), Square(), Triangle()]
        self.add(*objects)
        
        # Selection search set is automatically maintained
        print(f"Search set size: {len(self.selection_search_set)}")
        
        # Clear and keep only first object
        self.clear_all_except(objects[0])
        
        # Search set is automatically updated
        print(f"Search set size: {len(self.selection_search_set)}")
```

## Implementation Details

### Scene Class Implementation

```python
@affects_mobject_list
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all mobjects from the scene and adds back only the specified ones.
    Duplicate mobjects in the argument list are handled gracefully (only added once).
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene after clearing
    """
    self.mobjects = []
    if mobjects_to_keep:
        # Remove duplicates while preserving order
        seen = set()
        unique_mobjects = []
        for mob in mobjects_to_keep:
            if id(mob) not in seen:
                seen.add(id(mob))
                unique_mobjects.append(mob)
        self.add(*unique_mobjects)
    return self
```

### InteractiveScene Class Implementation

```python
def clear_all_except(self, *mobjects_to_keep: Mobject):
    """
    Clears all mobjects from the scene and adds back only the specified ones.
    Also handles selection search set regeneration for interactive scene.
    
    Args:
        *mobjects_to_keep: Mobjects that should remain in the scene after clearing
    """
    super().clear_all_except(*mobjects_to_keep)
    self.regenerate_selection_search_set()
    return self
```

## Key Design Decisions

1. **Decorator**: Uses `@affects_mobject_list` in Scene class to ensure render groups are properly assembled
2. **Deduplication**: Removes duplicate objects from arguments to prevent adding the same object multiple times
3. **Order preservation**: Maintains the order of objects as specified in arguments
4. **Return value**: Returns `self` to enable method chaining
5. **InteractiveScene integration**: Automatically updates selection search set for interactive features

## Comparison with Existing Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| `clear()` | Removes all mobjects | When you want to completely clear the scene |
| `remove(*mobjects)` | Removes specific mobjects | When you know what to remove |
| `clear_all_except(*mobjects)` | Removes all except specified | When it's easier to specify what to keep |

## Edge Cases Handled

1. **No arguments**: Calling `clear_all_except()` clears everything (same as `clear()`)
2. **Non-existent objects**: Objects not in the scene are handled gracefully
3. **Duplicate arguments**: Same object specified multiple times only appears once
4. **Groups**: Works with grouped mobjects
5. **Camera frame**: The camera frame is handled correctly by the add/remove logic

## Testing

Comprehensive tests have been created in:
- `test_clear_all_except.py` - Basic functionality tests
- `test_clear_all_except_comprehensive.py` - Edge cases and advanced scenarios

Run tests with:
```bash
xvfb-run -a python test_clear_all_except.py
xvfb-run -a python test_clear_all_except_comprehensive.py
```

## Performance Considerations

- The method clears the entire mobjects list and re-adds objects, which triggers render group assembly
- For scenes with many objects, this is still efficient as it's a one-time operation
- The deduplication uses a set lookup which is O(n) where n is the number of arguments

## Common Patterns

### Pattern 1: Persistent UI Elements
```python
class PersistentUI(Scene):
    def construct(self):
        title = Text("Title").to_edge(UP)
        self.add(title)
        
        # Do stuff with many temporary objects
        self.show_stage_1()
        
        # Clear but keep title
        self.clear_all_except(title)
        
        # Show next stage
        self.show_stage_2()
```

### Pattern 2: Progressive Disclosure
```python
class ProgressiveDisclosure(Scene):
    def construct(self):
        # Show many objects
        all_objects = self.create_many_objects()
        self.add(*all_objects)
        self.wait()
        
        # Focus on important ones
        important = all_objects[:3]
        self.clear_all_except(*important)
        self.wait()
```

### Pattern 3: State Management
```python
class StateManagement(Scene):
    def construct(self):
        # State 1
        state1_objects = [Circle(), Square()]
        self.add(*state1_objects)
        self.wait()
        
        # Transition to State 2
        state2_objects = [Triangle(), Text("State 2")]
        self.clear_all_except()  # Clear all
        self.add(*state2_objects)
        self.wait()
```

## Troubleshooting

### Issue: Objects not appearing after clear_all_except
**Cause**: Object might not have been added to scene before clearing  
**Solution**: Ensure objects are added before calling clear_all_except

### Issue: Unexpected objects remain
**Cause**: Might be passing wrong objects or not all objects to keep  
**Solution**: Use print statements to debug which objects are in the scene

```python
# Debug helper
print(f"Objects in scene: {[type(m).__name__ for m in self.mobjects]}")
self.clear_all_except(obj1, obj2)
print(f"Objects after clear: {[type(m).__name__ for m in self.mobjects]}")
```

## Future Enhancements

Possible future enhancements could include:
1. Optional parameter to keep objects matching a predicate
2. Option to animate the removal
3. Support for keeping objects by type or property
4. Undo/redo integration

## Conclusion

The `clear_all_except()` method provides a clean and intuitive way to manage scene content, especially useful for multi-stage visualizations where you want to maintain certain UI elements while clearing the rest.
