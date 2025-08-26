## Overlap check:
Overlap iff the later start ≤ earlier end.

- Two intervals A=[a1,a2], B=[b1,b2] overlap 
    - iff max(a1, b1) ≤ min(a2, b2) IS TRUE
        - equal to `a1 ≤ b2 and b1 ≤ a2`
    - the intersection is [max(a1,b1), min(a2,b2)].

Question:
- 986