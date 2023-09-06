### How to modify the doc

1.Clone the git project:
```
eval $(ssh-agent)
ssh-add $HOME/.ssh/id_ligo
ssh-add -l
cd $HOME/virgo/doc
git clone git@github.com:lethuill/mbta-offline-doc.git
cd mbta-offline-doc
git remote -v
```

2.Manage the project at readthedocs:
https://readthedocs.org/projects/mbta-offline-doc/

3.Look at the results:
https://mbta-offline-doc.readthedocs.io/en/latest/

4.Read the tutorial here:
https://docs.readthedocs.io/en/stable/tutorial/
