## Data Structure
```dataview
Table pageorder AS "#", file.name
WHERE contains(tags, "ds")
SORT pageorder asc
```
## Algorithm
```dataview
Table pageorder AS "#", description AS "Desc"
WHERE contains(tags, "algorithm")
SORT pageorder asc
```