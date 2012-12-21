=============================
Maintaining Pyramid tutorials
=============================

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

The tutorial user documentation in HTML, PDF, epub format is produced
from two sets of files:

  - Source files. They constitute the wiki web application
    being developed.  Most files start from a `Pyramid`
    scaffold created in the *Installation* chapter.
    Five of those files are modified in subsequent tutorial
    chapters.
    Three files are created in the *Defining views*
    and *Adding authorization* chapters.

  - Documentation files.  They list the content of some of the
    source files, highlighting the added or modified lines and
    in some cases refering to specific line numbers in the
    listing to explain them.  For example: "line 2 imports
    the docutils module" or "lines 13-15 define a function".
    They are in `reST` format and there is one ``.rst`` file
    per chapter.

These files are located under
``docs/tutorials/wiki`` and ``docs/tutorials/wiki2`` in the
`Pyramid` source directory.  The documentation files are
in the top level, the source files are duplicated in folders
under a ``src/`` main folder::

 docs/tutorials/wiki/*.rst
                     src/
                         basiclayout/
                         models/
                         views/
                         authorization/
                         tests/

Each folder contains modifications that are made to some of the
source files in a chapter.

The scaffold is produced by a ``pcreate -s zodb tutorial`` or
``pcreate -s alchemy tutorial`` command.
The files ``CHANGES.txt, development.ini,
MANIFEST.in, production.ini, README.txt`` and ``setup.cfg`` that
result from the scaffold are not modified in the tutorial.
The following table shows the folder - chapter correspondence
and the source files that are modified on each chapter:

+--------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
+    Folder          |  Chapter                   |     Source files                                                                                                            |
|                    |                            +--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
|                    |                            | ``setup.py`` | ``__init__.py`` | ``models.py`` | ``views.py`` | ``edit.pt`` | ``login.pt`` | ``security.py`` | ``tests.py`` |
|                    |                            |              |                 |               |              | ``view.pt`` |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
| ``basiclayout/``   | Basic Layout               |   New        |   New           |   New         |   New        |             |              |                 |   New        |
|                    |                            |              |                 |               |              |             |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
| ``models/``        | Defining the Domain Model  |   Modified   |                 |   Modified    |              |             |              |                 |              |
|                    |                            |              |                 |               |              |             |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
| ``views/``         | Defining Views             |   Modified   |                 |               |   Modified   |   New       |              |                 |              |
|                    |                            |              |                 |               |              |             |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
| ``authorization/`` | Adding Authorization       |              |   Modified      |               |   Modified   |   Modified  |   New        |   New           |              |
|                    |                            |              |                 |               |              |             |              |                 |              |
|                    |                            |              |                 |               |              |             |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+
| ``tests/``         | Adding Tests               |   Modified   |                 |               |              |             |              |                 |   Modified   |
|                    |                            |              |                 |               |              |             |              |                 |              |
+--------------------+----------------------------+--------------+-----------------+---------------+--------------+-------------+--------------+-----------------+--------------+


If an external change is merged to a source file in one of
the folders, in most cases the change needs to merged to that
file in the folders for subsequent chapters.

If the external change consists of one or more lines being added
or deleted in a source file, some
line number references to that file in the documentation might
need to be updated.

References
==========

Listing the content of a source file is done with the
`literalinclude` Sphinx directive, along these options:

- `lines` to select specific lines to display.

- `emphasize-lines` to highlight the added or edited lines.

The following example is from ``docs/tutorials/wiki2/definingviews.rst``::

    It's time for a major change.  Open ``tutorial/tutorial/views.py`` and edit it to look like the following:

    .. literalinclude:: src/views/tutorial/views.py
    :linenos:
    :language: python
    :emphasize-lines: 1-7,12,15-70

    (The highlighted lines are the ones that need to be added or edited.)

If an external change adds a new line at the current line 8, the line
number references 12 and 15-70 in the ``:emphasize-lines:`` option
need to be added 1 like this::

    :emphasize-lines: 1-7,13,16-71

This other example is from ``docs/tutorials/wiki2/authorization.rst``::

    Our ``tutorial/tutorial/__init__.py`` will look something like this
    when we're done:

    .. literalinclude:: src/authorization/tutorial/__init__.py
    :linenos:
    :emphasize-lines: 2-3,7,21-23,25-27,30-31
    :language: python

    (Only the highlighted lines need to be added.)

If the external change adds a new line at the current lines 7 and 26,
the line number references 7, 21-23 and 25- in the ``:emphasize-lines:``
option need to be added 1, while the line number references -27 and
30-31 need to be added 2 like this::

    :emphasize-lines: 2-3,8,22-24,26-29,32-33

If the new line 7 is not blank and is part of what the user needs
to add, then that line needs to be included in the line number
reference 7 by converting it to 7-8::

    :emphasize-lines: 2-3,7-8,22-24,26-29,32-33

The ``:emphasize-lines:`` option refers to the lines that are displayed
and in some cases they do not need to be changed.
This example is from ``docs/tutorials/wiki2/authorization.rst``::

    Open ``tutorial/tutorial/__init__.py`` and add a ``root_factory``
    parameter to our :term:`Configurator` constructor, that points to
    the class we created above:

    .. literalinclude:: src/authorization/tutorial/__init__.py
    :lines: 24-25
    :linenos:
    :emphasize-lines: 2
    :language: python

    (Only the highlighted line needs to be added.)

Only two lines are displayed, and both are also highlighted.  If
an external change removes a line at the current line 10, then
only the line number reference 24-25 in the ``:lines:`` option
needs to be substracted 1 to be like this::

    :lines: 23-24

the line number reference 2 in the ``:emphasize-lines:`` option
remains unaffected.


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
against the corresponding file in the ``basiclayout`` folder
of the SQL tutorial, and then opens
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
