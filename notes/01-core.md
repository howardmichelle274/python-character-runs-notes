# Encode consecutive character runs: implementation

## What the example does

groupby groups adjacent equal values, not all matching values. Run-length encoding helps repeated sequences but can be larger for ordinary text.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"aaabbcaaa"
```

Expected result:

```json
[
  {
    "character": "a",
    "count": 3
  },
  {
    "character": "b",
    "count": 2
  },
  {
    "character": "c",
    "count": 1
  },
  {
    "character": "a",
    "count": 3
  }
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
