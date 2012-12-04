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

The subfolders under `src/` contain the source code files that
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
directive.  The line references after the listing might also
need modifications.

A tutorial source code file might need to be modified because
the `Pyramid` API or the corresponding scaffold file is
modified.

Operation
=========

If one or more files in the `alchemy` or `zodb` scaffolds are
modified, those changes need to be applied into the tutorial
initial files:

#. Render that scaffold into a temporary area, using `tutorial`
   as the project name.

#. Compare the rendered scaffold folder  against the `basiclayout`
   folder of the corresponding tutorial path.

#. For each updated file of the scaffold:

   #. Merge the changes into the corresponding file in the
      `basiclayout` folder.

   #. If one ore more lines added or deleted, determine
      if any displayed lines, emphasized lines, or line
      references are affected, and adjust them in the
      `basiclayout.rst` documentation file.

   #. Compare with the corresponding file in the `models`
      folder of the tutorial.

   #. Merge the changes into the file in the `models`
      folder.

   #. If one ore more lines added or deleted, determine
      if any displayed lines, emphasized lines, or line
      references are affected, and adjust them in the
      `definingmodels.rst` documentation file.

   #. Repeat the last three steps for the corresponding file
      in the `views`, `authorization` and `tests` folders,
      updating the `definingviews.rst`, `authorization.rst`
      and `tests.rst` files if needed.

Tools
=====

Some of the steps described above can assisted by the following
scripts.

Merge changes in the scaffold
-----------------------------

The following script renders the `alchemy` scaffold into
a temporary path, it compares each file in the rendered scaffold
against the corresponding file in the SQL tutorial, and then opens
vim with one tab for each file that has differences between the
rendered scaffold  and the SQL tutorial::

 update-scaffolds

Each tab shows the color diff of the file in the
scaffold vs the corresponding file in the tutorial.

Function keys are defined to move from one change to another
`F5` and `F6`, to apply a change, `F8`, and to navigate the tabs,
`F9` and `F12`.

When vim is quit, the same process is repeated for the `zodb`
scaffold.

Merge changes across tutorial stages
------------------------------------

The following script will open vim with four tabs.
Each tab shows the color diff of a given file from
a stage to the next one.  To display a file in the
ZODB tutorial::

 update-file-by-stage '' <file-path>

To display a file in the SQL tutorial::

 update-file-by-stage 2 <file-path>

Function keys are defined to move from one change to another
`F5` and `F6`, to apply a change, `F8`, and to navigate the tabs,
`F9` and `F12`.

Find references to source files
-------------------------------

The following Python 3 script lists the
`literalinclude` references by file on each stage.  To
do this for the ZODB tutorial::

 src2rst.py

To work on the SQL tutorial::

 src2rst.py 2
