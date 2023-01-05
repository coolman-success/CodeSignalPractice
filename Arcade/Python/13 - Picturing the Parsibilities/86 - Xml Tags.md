# Xml Tags

You want to create your local database containing information about the things you find the coolest. You used to store this information in `xml` documents, so now you need to come up with an algorithm that will convert the existing format into the new one. First you decided to choose a structure for your scheme, and to do it you want to represent `xml` document as a tree, i.e. gather all the tags and print them out as follows:

```
tag1()
 --tag1.1(attribute1, attribute2, ...)
 ----tag1.1.1(attribute1, attribute2, ...)
 ----tag1.1.2(attribute1, attribute2, ...)
 --tag1.2(attribute1, attribute2, ...)
 ----tag1.2.1(attribute1, attribute2, ...)
...
```

where attributes of each tag are sorted *lexicographically*.

You are a careful person, so the structure of the `xml` is neatly organized is such a way that:

- there is a single tag at the root level;
- each tag has a single parent tag (i.e. if there are several occurrences of tag `a`, and in one occurrence it's a child of tag `b` and in the other one it's a child of tag `c`, then `b = c`);
- each appearance of the same tag belongs to the same level.

Given an `xml` file, return its structure as shown above. The tags of the same level should be sorted in the order they appear in `xml`, and the attributes should be sorted *lexicographically*.

Note: you are given xml represantation in one line.

## Example

For

```
xml =
"<data>
    <animal name="cat">
    	<genus>Felis</genus>
        <family name="Felidae" subfamily="Felinae"/>
        <similar name="tiger" size="bigger"/>
    </animal>
    <animal name="dog">
        <family name="Canidae" member="canid"/>
        <order>Carnivora</order>
        <similar name="fox" size="similar"/>
    </animal>
</data>"
```

the output should be

```
solution(xml) =
["data()",
 "--animal(name)",
 "----genus()",
 "----family(member, name, subfamily)",
 "----similar(name, size)",
 "----order()"]
```

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string xml**

	`xml` file as a string.

	*Guaranteed constraints:*

	`7 ≤ xml.length ≤ 1000`.

- **[output] array.string**

	A list representing the structure of the `xml` file as described above.
