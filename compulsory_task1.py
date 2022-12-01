'''(A majority of the information has been sourced from the task's pdf)

1. What is normalisation?

Normalisation is a process for evaluating and correcting table structures to minimise data redundancies and therefore reduce the likelihood of data anomalies. In other words, normalisation is a method to remove anomalies and bring the database to a consistent state.


2. When is a table in 1NF?

● All of the key attributes are defined;
● There are no repeating groups in the table;
● All attributes are dependent on the primary key (Coronel & Morris, 2014).

3. When is a table in 2NF?

● It is in 1NF
● It includes no partial dependencies; that is, no attribute is dependent on only a portion of the primary key.

It is still possible for a table in 2NF to exhibit transitive dependency; that is, one or more attributes may be functionally dependent on non-key attributes (Coronel & Morris, 2014).


4. When is a table in 3NF?

● It is in 2NF
● It contains no transitive dependencies (Rob, Coronel, & Crockett, 2008).




5. Using the INVOICE table given below, draw its dependency diagram and
identify all dependencies (including transitive and partial dependencies).
You can assume that the table does not contain any repeating groups and
that an invoice number references more than one product. Hint: This table
uses a composite primary key.

Dependencies: INV_NUM -> PROD_NUM, SALE_DATE, PROD_LABEL,	VEND_CODE, VEND_NAME, QUANT_SOLD, PROD_PRICE

Partial Dependencies: INV_NUM -> SALE_DATE

Transitive Dependencies: INV_NUM -> SALE_DATE, PROD_NUM -> PROD_LABEL, VEND_CODE -> VEND_NAME, PROD_NUM -> PROD_PRICE

CHART: INV_NUM -> PROD_NUM, SALE_DATE, PROD_LABEL,	VEND_CODE, VEND_NAME, QUANT_SOLD, PROD_PRICE

6. Using the answer to the above question, remove all partial dependencies
and draw the new dependency diagrams. Identify the normal forms for
each table structure you created.

SALE
INV_NUM -> SALE_DATE

PRODUCT SOLD
PROD_NUM -> PROD_LABEL, VEND_CODE, VEND_NAME, 

PROFIT
INV_NUM -> PROD_NUM, QUANT_SOLD, PROD_PRICE

7. Using the answer to the above question, remove all transitive dependencies
and draw the new dependency diagrams. Identify the normal forms for
each table structure you created.

SALE
INV_NUM -> SALE_DATE

PRODUCT SOLD
PROD_NUM -> PROD_LABEL

VENDER
VEND_CODE -> VEND_NAME

PROFIT
INV_NUM -> PROD_NUM, QUANT_SOLD, PROD_PRICE



Drawings are submitted in the file via jpegs
'''