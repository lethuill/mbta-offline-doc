slurm + cvmfs +scitokens = ?
===========================

.. _slurm:

slurm
-----

Local farm at ccin2p3

https://gwdatafind.readthedocs.io/

https://computing.docs.ligo.org/guide/auth/scitokens/


cvmfs
-----

LVK data are distributed over cvmfs

.. code-block:: console

   source /cvmfs/software.igwn.org/conda/etc/profile.d/conda.sh
   conda activate igwn-py310 > /dev/null 2>&1
   htgettoken --vaultserver vault.ligo.org --issuer igwn --audience https://datafind.ligo.org --scope gwdatafind.read
   httokendecode -H
   python -m gwdatafind -r datafind.ligo.org -o H -t H1_HOFT_C00 --latest


scitokens
---------
authentification 
vault
bearer


accessing slurm from a slurm job
--------------------------------
myscripts



