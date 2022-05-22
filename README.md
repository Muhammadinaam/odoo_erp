# Odoo ERP

- Create chart of accounts
    - ![](https://github.com/Muhammadinaam/odoo_erp/blob/master/readme_gifs/setup_chart_of_accounts.gif)

    
- Enter opening balances of accounts
    - https://www.youtube.com/watch?v=z_XJGHEF0T8&ab_channel=OdooMates
- Set "Anglo-Saxon Accounting"
    - Go to settings
    - search "anglo"
    - Check "Anglo-Saxon Accounting" checkbox
    - Click save button
- Enable "Landed Costs"
    - Go to settings
    - search "landed"
    - Check "Landed Costs" checkbox
    - Click save button
- Setup "Average costing and Automated costing for inventory"
    - Create following account heads in chart of accounts for inventory costing:
        - **Stock Valuation Account**: Stock Valuation Account is nothing but the account showing real value (current value) of assets. So this must be Current Assets.
        - **Stock Input Account**: Stock Input Account is an interim account for parking the "accounting payable"during 'Receive Products" because later this will get knocked off against the Vendor (Accounts Payable) during creation of Vendor Bill. So this account type should be 'Current Liabilities'.
        - **Stock Output Account**: Stock Output Account is an interim account for parking the "accounts receivable" during "Shipments" because later this will get setoff against the Customer (Accounts Receivable) while creating Customer Bill. So the type should be "Current Assets".
- Employee contracts
- Employee Lunch
- Employee Attendance
- Repairs
- Fleet
- Maintenance
- Employees
- Recruitment
- Timeoff
- Expenses
- Manufacturing
- Purchase
- Inventory
- Sales
- Accounting
- Payroll
