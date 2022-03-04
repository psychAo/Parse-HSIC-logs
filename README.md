# toolbox
some scripts making things easier

## parse_log.py
parse https://github.com/shangsw/HPDM-SPRN terminal log.
outputs like:
|      | model | dataset |  oa   | oa_std |  aa   | aa_std | kappa | kappa_std |
| :--: | :---: | :-----: | :---: | :----: | :---: | :----: | :---: | :-------: |
|  0   | anet  |   ip    | 83.69 |  1.32  | 78.54 |  2.25  | 81.38 |   1.49    |
|  1   | anet  |   pu    | 97.73 |  0.33  | 96.42 |  0.92  | 96.99 |   0.44    |
|  2   | anet  |   sa    | 94.68 |  0.63  | 96.54 |  0.60  | 94.08 |   0.70    |
|  3   | bnet  |   ip    | 2.69  | 11.32  | 78.54 | 21.25  | 81.38 |   1.49    |
|  4   | bnet  |   pu    | 70.73 | 11.33  | 96.42 |  0.92  | 96.00 |   0.01    |
|  5   | bnet  |   sa    | 94.68 |  0.00  | 96.54 | 20.60  | 14.08 |   0.70    |

