# Blithedale Regex

1. Search for `&, <, and >`. There are none.
2. Find `\n{3}`, Replace: `\n\n`
3. Find: `\n\n`, Replace: `</p>\n\n<p>`
Not stumped anymore
4. Find: `(<p>)([IVX]+\..+)(</p>)`, Replace: `<title>\2</title>`
5. Find: `<title>`, Replace: `</chapter>\n<chapter><title>`
6. Find: `(")(.+?)(")`, Replace: `<quote>\2</quote>`