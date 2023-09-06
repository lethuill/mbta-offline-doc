Where's the data Lebowski
========================

.. _data:

gwdatafind
----------

The GWDataFind service allows users to query for the location of Gravitational-Wave data files containing data associated with gravitational-wave detectors.

https://gwdatafind.readthedocs.io/

.. code-block:: console

   htgettoken --audience https://datafind.ligo.org --scope gwdatafind.read
   gw_data_find -r datafind.ligo.org -o H -t H1_HOFT_C00 --latest

``-y`` to find available type

.. code-block:: console

   gw_data_find -o V -y | grep -i hoft
   gw_data_find -o V -y | grep -i online


``-a`` to find time segments where a given type is available

.. code-block:: console

   gw_data_find -o L -t L1_HOFT_C00_AR -a


``-f`` to find location(s) of a file

.. code-block:: console

   gw_data_find -f L-L1_HOFT_C00_AR-1368974350-3058.gwf

.. note::

   Vigro h(t) name changed on Jun 13

.. code-block:: console

   gw_data_find -o V -t V1Online --latest
   gw_data_find -o V -t HoftOnline --latest



O4 data
------------------

RAW DATA:
at LLO: /archive/frames/O3/raw/L1
at LHO: /archive/frames/O3/raw/H1
at Cascina: /data/archive/rawdata 
at CC: /hpss/in2p3.fr/group/virgo/Run/O3/raw/
at Cascina ER15: /data/dev/hrec/V1Online


ONLINE LOW LATENCY FRAMES:
datasets: H1_llhoft, L1_llhoft, V1_llhoft
at CIT:
   /dev/shm/kafka/   (5 min buffer)
   /ifocache/llcache/kafka/  (1 month buffer)

at Cascina: ~1 week buffer /data/dev/hrec  => H1KafkaOnline, L1KafkaOnline, V1Online
                    ~2 months buffer /data/prod/hrec/H1Online L1Online V1Online


Aggregated frames:
datasets: H1_HOFT_C00, L1_HOFT_C00, V1???
at LLO, LHO, CIT:
    /archive/frames   /O3 /ER15 /O4
    aggregated h(t) => /ifocache/frames/O4/hoft_C00/


AR Frames:
Datatsets: H1_HOFT_C00_AR, L1_HOFT_C00_AR
at CIT: 
   /ifocache/frames/O4/hoft_C00_AR
   /ceph/mirror/frames/O4/hoft_C00_AR
   /archive/frames/O4/hoft_C00_AR
   /cvmfs/ligo.storage.igwn.org/igwn/ligo/frames/O4/hoft_C00_AR

