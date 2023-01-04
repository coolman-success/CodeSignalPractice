# User Attribute

At CodeSignal information about the users is stored in the database. Anny is working on the class representation of this information, and needs to come up with a class that creates objects with the following attributes: `username`, `_id`, `xp` and `name`. She has already come up with a test object:

```
username: "annymaster"
_id: "1234567"
xp: "1500"
name: "anny"
```

The problem is, she doesn't know if this will be enough. It is possible that the server will require information about additional attributes that are not yet present in Anny's representation.

Given the `attribute` the server requested, return its value if it is defined, and the <code><i>&lt;attribute&gt;</i> attribute is not defined</code> string otherwise.

## Example

- For `attribute = "_id"`, the output should be

`solution(attribute) = "1234567"`;

- For `attribute = "age"`, the output should be

`solution(attribute) = "age attribute is not defined"`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string attribute**

	An attribute the server requested.

	*Guaranteed constraints:*

	`1 ≤ attribute.length ≤ 10`.

- **[output] string**

	The value of the attribute if it's defined, <code><i>&lt;attribute&gt;</i> attribute is not defined</code> otherwise.
