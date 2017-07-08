
\w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
\W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
\s - matches whitespace, so spaces, tabs, newlines, etc.
\S - matches everything that isn't whitespace.
\d - is how we match any number from 0 to 9
\D - matches anything that isn't a number.
\b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
\B - matches anything that isn't the edges of a word.
