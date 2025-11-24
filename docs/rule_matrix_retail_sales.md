# Retail Sales Data Quality Rules (Retail Store Sales: Dirty for Data Cleaning)

| Rule ID | Column              | Rule description                                                                             | Action on fail                             | Severity                              |
| ------: | ------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------- | ------------------- | ------ |
|     R01 | Transaction ID      | Must be not null                                                                             | Quarantine row                             | High                                  |
|     R02 | Transaction ID      | Must be unique within batch                                                                  | Send to duplicate bucket                   | Medium                                |
|     R03 | Customer ID         | Must be not null                                                                             | Quarantine row                             | High                                  |
|     R04 | Category            | Must be not null                                                                             | Quarantine row                             | High                                  |
|     R05 | Item                | Must be not null                                                                             | Quarantine row                             | Medium                                |
|     R06 | Price Per Unit      | Must be numeric and > 0                                                                      | Quarantine row                             | High                                  |
|     R07 | Quantity            | Must be numeric and > 0                                                                      | Quarantine row                             | High                                  |
|     R08 | Total Spent         | Must be numeric and >= 0                                                                     | Quarantine row                             | High                                  |
|     R09 | Total vs Price\*Qty |                                                                                              | Total Spent - (Price Per Unit \* Quantity) | <= 0.01 _ (Price Per Unit _ Quantity) | Flag for review/API | Medium |
|     R10 | Payment Method      | Must be in allowed set {Cash, Credit Card, Digital Wallet}                                   | Quarantine row                             | Medium                                |
|     R11 | Location            | Must be in allowed set {Online, In-store}                                                    | Quarantine row                             | Medium                                |
|     R12 | Transaction Date    | Must be a valid date and not in the future                                                   | Quarantine row                             | High                                  |
|     R13 | Discount Applied    | Must be one of {True, False, null}; map variants (e.g. 'Yes'/'No') where present             | Map or quarantine if weird                 | Low                                   |
|     R14 | Schema              | Required columns present; no unexpected missing critical columns                             | Fail batch & alert                         | Critical                              |
|     R15 | Record-level        | If any High severity rule fails, entire row is treated as invalid and written to error store | N/A                                        | N/A                                   |
