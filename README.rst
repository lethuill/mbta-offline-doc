Clone the git project:
eval $(ssh-agent)
ssh-add $HOME/.ssh/id_ligo
ssh-add -l
cd $HOME/virgo/doc
git clone git@github.com:lethuill/mbta-offline-doc.git
cd mbta-offline-doc
git remote -v

Manage the project at readthedocs:
https://readthedocs.org/projects/mbta-offline-doc/

Look at the results:
https://mbta-offline-doc.readthedocs.io/en/latest/

Read the tutorial here:
https://docs.readthedocs.io/en/stable/tutorial/
