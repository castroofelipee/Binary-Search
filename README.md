```markdown
# Binary Search

Binary Search is an efficient search algorithm used to find an element in a **sorted list**.

## What is Binary Search?

Binary Search works by repeatedly dividing the search interval in half.

Instead of checking every element one by one (like linear search), it:

1. Looks at the middle element.
2. Compares it with the target value.
3. Discards half of the list based on the comparison.
4. Repeats the process until the element is found or the interval is empty.

## Requirements

- The list **must be sorted**.
- Works best with large datasets.

## How It Works 

Given this list:

```

[1, 2, 3, 4, 5, 6, 7]

```

If we search for `4`:

- Start with the full range.
- Check the middle element → `4`
- Target found in 1 attempt.

If we search for `7`:

- Check middle → `4`
- 7 is greater → discard left half
- Check new middle → `6`
- 7 is greater → discard left half
- Check new middle → `7`
- Found.

## Time Complexity

Binary Search runs in:

```

O(log n)

```
