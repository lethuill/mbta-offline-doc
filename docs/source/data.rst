Where's the data Lebowski
========================

.. _data:

gw_data_find
------------

The GWDataFind service allows users to query for the location of Gravitational-Wave data files. Scitokens authentification is required to access the datafind server.

https://gwdatafind.readthedocs.io/

https://computing.docs.ligo.org/guide/auth/scitokens/

.. code-block:: console

   source /cvmfs/software.igwn.org/conda/etc/profile.d/conda.sh
   conda activate igwn-py310 > /dev/null 2>&1
   htgettoken --vaultserver vault.ligo.org --issuer igwn --audience https://datafind.ligo.org --scope gwdatafind.read
   httokendecode -H
   python -m gwdatafind -r datafind.ligo.org -o H -t H1_HOFT_C00 --latest

``-y`` to find available type

.. code-block:: console

   python -m gwdatafind -r datafind.ligo.org  -o V -y | grep -i hoft
   python -m gwdatafind -r datafind.ligo.org  -o V -y | grep -i online
   python -m gwdatafind -r datafind.ligo.org  -o H -y | grep -i hoft


``-a`` to find time segments where a given type is available

.. code-block:: console

   python -m gwdatafind -r datafind.ligo.org  -o L -t L1_HOFT_C00_AR -a


``-f`` to find location(s) of a file

.. code-block:: console

   python -m gwdatafind -r datafind.ligo.org  -f L-L1_HOFT_C00_AR-1368974350-3058.gwf

.. warning::

   Vigro h(t) name changed from V1Online to HoftOnline on Jun 13

.. code-block:: console

   python -m gwdatafind -r datafind.ligo.org  -o V -t V1Online --latest
   python -m gwdatafind -r datafind.ligo.org  -o V -t HoftOnline --latest



O4 data
-------

Raw data
^^^^^^^^

.. code-block:: console

   at CIT, LHO, LLO:
      /archive/frames/O4/raw
      /ifocache/frames/O4/raw
      /ceph/mirror/frames/O4/raw

   at LHO: /archive/frames/O4/raw/H1

   at LLO: /archive/frames/O4/raw/L1


Low latency frames
^^^^^^^^^^^^^^^^^^

datasets: ``H1_llhoft``, ``L1_llhoft``, ``V1Online`` (before 2023-JUN-13) or ``HoftOnline`` (after 2023-JUN-13)

.. code-block:: console

   at CIT, LHO, LLO:
      /dev/shm/kafka/   (5 min buffer)
      /ifocache/llcache/kafka/  (1 month buffer)
   
   at Cascina:
      /data/dev/hrec/ H1KafkaOnline L1KafkaOnline V1Online (~1 week buffer)
      /data/prod/hrec/ H1Online L1Online V1Online (~2 months buffer)


Aggregated frames
^^^^^^^^^^^^^^^^^^

datasets: ``H1_HOFT_C00``, ``L1_HOFT_C00``, ``V1Online`` (before 2023-JUN-13) or ``HoftOnline`` (after 2023-JUN-13)

.. code-block:: console

   on cvmfs:
      /cvmfs/ligo.storage.igwn.org/igwn/ligo/frames/O4/hoft_C00
      /cvmfs/virgo.storage.igwn.org/igwn/virgo/frames/O4/V1Online (before Jun 13)
      /cvmfs/virgo.storage.igwn.org/igwn/virgo/frames/O4/HoftOnline (after Jun 13)

   at CIT: 
      /ifocache/frames/O4/hoft_C00
      /ceph/mirror/frames/O4/hoft_C00
      /archive/frames/O4/hoft_C00

   at LLO, LHO:
      /archive/frames/O4/hoft_C00

   at Cascina:
      /data/prod/hrec/ H1Online L1Online V1Online (~2 months buffer)     


Analysis ready frames
^^^^^^^^^^^^^^^^^^^^^

datasets: ``H1_HOFT_C00_AR``, ``L1_HOFT_C00_AR``, ``V1Online`` (before 2023-JUN-13) or ``HoftOnline`` (after 2023-JUN-13)

.. code-block:: console

   on cvmfs:
      /cvmfs/ligo.storage.igwn.org/igwn/ligo/frames/O4/hoft_C00_AR

   at CIT: 
      /ifocache/frames/O4/hoft_C00_AR
      /ceph/mirror/frames/O4/hoft_C00_AR
      /archive/frames/O4/hoft_C00_AR
   

O3 data
------------------

Raw data
^^^^^^^^

.. code-block:: console

   at LLO: /archive/frames/O3/raw/L1
   at LHO: /archive/frames/O3/raw/H1
   at Cascina: /data/archive/rawdata 
   at CC: /hpss/in2p3.fr/group/virgo/Run/O3/raw/

Low latency frames
^^^^^^^^^^^^^^^^^^

.. code-block:: console

   at CIT:
      /dev/shm/kafka/   (5 min buffer)
      /ifocache/llcache/kafka/  (1 month buffer)
   
   at Cascina: ~1 week buffer /data/dev/hrec  => H1KafkaOnline, L1KafkaOnline, V1Online
               ~2 months buffer /data/prod/hrec/H1Online L1Online V1Online


Aggregated frames
^^^^^^^^^^^^^^^^^

.. code-block:: console

   at LLO, LHO, CIT:
       /archive/frames   /O3 /ER15 /O4
       aggregated h(t) => /ifocache/frames/O4/hoft_C00/


Analysis ready frames
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   at CIT: 
      /ifocache/frames/O4/hoft_C00_AR
      /ceph/mirror/frames/O4/hoft_C00_AR
      /archive/frames/O4/hoft_C00_AR
      /cvmfs/ligo.storage.igwn.org/igwn/ligo/frames/O4/hoft_C00_AR
