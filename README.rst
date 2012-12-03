==================================
Maintaining Pyramid tutorial files
==================================

How to maintain the `Pyramid` tutorial files and their
documentation synchronized when the corresponding scaffolds are
modified.

Operation
=========

#. Update one or more files in the alchemy or
   zodb scaffolds.

#. For each updated file of a scaffold:

   #. Merge changes into the `basiclayout` stage of
      the tutorial that uses that scaffold.

   #. For each of the `models`, `views`, `authorization`
      and `tests` stages:

      #. Merge changes in the file from the previous section
         into that stage on the given tutorial.
  
      #. If one ore more lines added or deleted, ajust the
         displayed and emphasized lines that are affected.

Tools
=====

The following script opens vim with one tab for each file that
changed, in the SQL and then the ZODB tutorial::

 update-scaffolds

Each tab shows the color diff of the file in the
scaffold vs the corresponding file in the tutorial.

The following script will open vim with four tabs.
Each tab shows the color diff of a given file from
a stage to the next one::

 update-file-by-stage '' <file-path>

 update-file-by-stage 2 <file-path>

The following Python 3 script lists the
`literalinclude` references by file on each stage::

 src2rst.py
