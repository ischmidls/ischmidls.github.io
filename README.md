# ischmidls.github.io
a tip of an iceberg
[ischmidls.github.io](https://ischmidls.github.io)

# slogans aside
i did this:
      > i want to store the node.js data in a separate repository and the generated static site solely in this github pages repo.
      > but, the git is too much of a headache right now.
      > i also might just shift to a static site again.
      > the generation is so bloated it takes more than a minute for each build.

- cloned _eleventy subdirectory to private repository [here](https://github.com/ischmidls/ischmidls-eleventy)
- added _eleventy/ to .gitignore
   - removed chached _eleventy/ subdirectory files
- see [stack exchange](https://stackoverflow.com/a/28923005/20874815) for cached ignored files
-    "git rm --cached if you want them untracked/irrelevant to history but want to keep the files intact locally."
- the rest was basic init, add ., commit -m "", remote add orgin, push, etc

# dangerous note

i always forget the command line tools.

here is a reminder

### where to run cammand line

- in `\_eleventy` folder run `npm` stuff
- in `\ischmidls.github.io` folder run `git` stuff

### git command aliases
   - `pacp` means                 `!f() { git pull && git add -A && git commit -m "$@" && git push; }; f`

### eleventy package stuff
  - browsersync is usual broken, so use `ws` package instead of `npm run serve` if it fails
  - otherwise `npm run build` and (idk `npm run serve`) and `npm run watch`
