==================================
Maintaining Pyramid tutorial files
==================================

How to maintain the `Pyramid` tutorial source code files and
their narrative documentation updated when one or more source
code files are modified.

This document is oriented to anyone contributing documentation
or code enhancements to `Pyramid`.  If the changes affect the
tutorials somehow, the following information will help the
contributor to include any necessary updates to keep the
tutorials up to date.

A few tool scripts are also included to assist in the
process, which may eventually be automated.

Organization
============

The files for the two wiki tutorials are located under
`docs/tutorials/wiki` and `docs/tutorials/wiki2` in the
`Pyramid` source directory.  The
structure is this::

 docs/tutorials/wiki/*.rst
                     src/
                         basiclayout/
                         models/
                         views/
                         authorization/
                         tests/

The \*.rst files are the narrative documentation for the
tutorial.

The subfolders under src/ contain the source code files that
make up the tutorial application.  These subfolders represent
the state of the source code files at the end of a given stage
of the tutorial.

Each source code file may or may not change from one stage to
the other.

A \*.rst documentation file may list the content of one or more
source files, by using a `literalinclude` Sphinx directive.
That directive may include `lines` and/or `emphasize-lines`
options.  The text after a source listing may contain references
to specific lines in that listing.  For example: "line 2 imports
the docutils module" or "lines 13-15 define a function".

Thus, the tutorial narrative documentation might need to be
updated when a tutorial source code file is modified.  If one or
more lines are added or deleted in a source code file,
a corresponding update might be needed in the `lines` and/or
`emphasize-lines` options of a `literalinclude` Sphinx
directive.

A source code file might need to be modified, either because
a `Pyramid` scaffold or the API is modified.

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
