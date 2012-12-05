==================================
Maintaining Pyramid tutorial files
==================================

This document is oriented to anyone contributing documentation
or code enhancements to the `Pyramid` web application framework.

From time to time, some aspect of the `Pyramid` API might
change or the `Pyramid` scaffold upon which the tutorial is
based may be modified.
If the changes affect the
tutorials somehow, the following information will help the
contributor to keep the
tutorials up to date.

A few tool scripts are also included to assist in the
process, which may eventually be automated.

Organization
============

The tutorial user will normally access the narrative
HTML documentation that explains the steps to follow, which
is organized in chapters.  Behind the scenes, we have
a set of `reST` documentation files, one \*.rst file
per chapter, from which the HTML
files are obtained, plus a set of source files that
are the tutorial application being developed.  There
is a snapshot of the source files as expected to be at
the end of each chapter where modifications are made.

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

In the top level there are the \*.rst documentation files and
`src/` contains the source code files, organized in subfolders that
correspond to the chapters as follows:

+-----------------+----------------------------+---------------------------------------------------------------------------------------------+
+  Folder         |  Chapter                   | Source files                                                                                |
|                 |                            +----------+-------------+----------+----------+----------+----------+-------------+----------+
|                 |                            | setup.py | __init__.py | models.py| views.py | edit.pt  | login.pt | security.py | tests.py |
|                 |                            |          |             |          |          | view.pt  |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+
| basiclayout/    | Basic Layout               |            These files are freshly rendered             |          |             |          |
|                 |                            |            from a `Pyramid` scaffold                    |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+
| models/         | Defining the Domain Model  | Modified |             | Modified |          |          |          |             |          |
|                 |                            |          |             |          |          |          |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+
| views/          | Defining Views             | Modified |             |          | Modified | New      |          |             |          |
|                 |                            |          |             |          |          |          |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+
| authorization/  | Adding Authorization       |          | Modified    |          | Modified | Modified | New      | New         |          |
|                 |                            |          |             |          |          |          |          |             |          |
|                 |                            |          |             |          |          |          |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+
| tests/          | Adding Tests               | Modified |             |          |          |          |          |             | Modified |
|                 |                            |          |             |          |          |          |          |             |          |
+-----------------+----------------------------+----------+-------------+----------+----------+----------+----------+-------------+----------+

The following files come from the scaffold but are not modified in the tutorial:
`CHANGES.txt, development.ini, MANIFEST.in, production.ini, README.txt, setup.cfg`.

A \*.rst documentation file may list the content of one or more
source files by using a `literalinclude` Sphinx directive.
That directive may include a `lines` option to select specific
lines to display.

The `literalinclude` directive may also include a  `emphasize-lines`
option to highlight some of the displayed lines.  This is used to
show the user what lines are added or edited.

To explain the user what some lines in the source do, the text after
a source listing may contain references to specific lines in
that listing.  For example: "line 2 imports the docutils module"
or "lines 13-15 define a function".

If a  tutorial source code file needs to be modified, the
tutorial narrative documentation might need to be updated
accordingly.  For example, if one or more lines are added or
deleted in a source code file, a corresponding update might be
needed in the `lines` and/or `emphasize-lines` options of
a `literalinclude` Sphinx directive.  The line references after
the listing might also need modifications.  Depending on the
case, these modifications may need to be propagated to the
source file in the snapshot for the next chapters.  The
following section explains this process.

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

Conventions
===========

- Use line numbers in code lisings with the `linenos` option,
  except when listing a single line.

- For a file that the user needs to edit:

  - Before the listing, ask the user to modify a file: *Open
    tutorial/tutorial/models.py file and edit it to look like
    the following:*

  - Use higlighting on the lines that are new or modified.

  - After the listing, include this legend: *(The highlighted
    lines are the ones that need to be changed.)*


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
