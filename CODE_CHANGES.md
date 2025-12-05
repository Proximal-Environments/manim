# Code Changes for clear_all_except() Method

## File 1: manimlib/scene/scene.py

### Location: After line 396 (after the `clear()` method)

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

**Lines added:** 398-411 (14 lines)

---

## File 2: manimlib/scene/interactive_scene.py

### Location: After line 339 (after the `clear_selection()` method)

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

**Lines added:** 341-358 (18 lines)

---

## Summary of Changes

- **Total files modified:** 2
- **Total lines added:** 32
- **Breaking changes:** None
- **Backward compatibility:** 100%

Both methods follow the existing code style and conventions used in ManimGL.
