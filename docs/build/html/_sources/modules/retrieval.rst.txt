This is retrieval
==========

Sub section
----------
    
This is an ordinary paragraph, introducing a block quote.
    "It is my business to know things. That is my trade."
        -- Sherlock Holmes

retrieval
------------
* item 1
* item 2
* item 3
    #. item 3.1
    #. item 3.2

3. item 1
4. item 2
5. item 3
#. item 4
#. item 5

term 1
    this is term 1.
term 2: term2
    this is term 2.


Field List

:Date: 2001-08-16
:Version: 1
:Authors: 
   - Me
   - Myself
   - I
:Indentation: 
Since the field marker may be quite long, the second
and subsequent lines of the field body do not have to line up
with the first line, but they must be indented relative to the
field name marker, and they must line up with each other.

:Parameter i: integer

+-------------------------+-------------------------+---------------+----------+
|| Header row, column 1   || Header 2               || Header 3     || Header 4|
|| (header rows optional) ||                        ||              ||         |
+=========================+=========================+===============+==========+
| body row 1, column 1    | column 2                | column 3      | column 4 |
+-------------------------+-------------------------+---------------+----------+
| body row 2              | Cells may span columns. |               |          |
+-------------------------+-------------------------+---------------+----------+
| body row 3              | Cells may               | - Table cells |          |
+-------------------------+-------------------------+---------------+----------+
| body row 4              | - body elements.        |               |          |
+-------------------------+-------------------------+---------------+----------+

===== ===== ======
   Inputs    Output
----------- ------
  A     B   A or B
===== ===== ======
False False False
True  False True
False True  True
True  True  True
===== ===== ======


.. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"

.. list-table:: Frozen Delights!
    :widths: 15 10 30
    :header-rows: 1
    
   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
    crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. note:: This is note.

.. warning:: This is warning.

