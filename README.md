# PharmaceuticalInventoryManagementSystem
School Project on 'Pharmaceutical Inventory Management System' using Python (&amp; MySQL). 
List of tables:
    purchase


    sale

    item
        itemID              int primary key,                          /*  0   */
        itemName            varchar(50),                              /*  1   */
        itemCategory        varchar(1),                               /*  2   */
        company             varchar(50),                              /*  3   */
        composition         text,                                     /*  4   */
        stockist            decimal(8,2),                             /*  5   */
        retailPrice         decimal(8,2),                             /*  6   */
        mrp                 decimal(8,2),                             /*  7   */
        packing             varchar(10),                              /*  8   */
        batchNo             int,                                      /*  9   */
        expiryDate          date,                                     /* 10   */
        manufacturingDate   date                                      /* 11   */

    customer/supplier


    invoice

