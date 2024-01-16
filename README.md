# ischmidls.github.io
a tip of an iceberg
[ischmidls.github.io](https://ischmidls.github.io)

# slogans aside

i want to store the node.js data in a separate repository and the generated static site solely in this github pages repo.

but, the git is too much of a headache right now.

i also might just shift to a static site again.

the generation is so bloated it takes more than a minute for each build.

# dangerous note

i always forget the command line tools.

here is a reminder

### git command aliases
   - `pacp` means                 `!f() { git pull && git add -A && git commit -m "$@" && git push; }; f`

### eleventy package stuff
  - browsersync is usual broken, so use `ws` package instead of `npm run serve` if it fails
  - otherwise `npm run build` and (idk `npm run serve`) and `npm run watch`
