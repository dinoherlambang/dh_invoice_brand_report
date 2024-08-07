# DH Invoice Brand Report

## Overview
This Odoo module enhances invoice reports by adding product brand information to the PDF printouts. It's designed to provide more detailed and brand-specific information on customer invoices, improving clarity and professionalism in your billing process.

## Features
- Adds a 'Brand' column to invoice report PDFs
- Integrates seamlessly with existing Odoo invoice templates
- Compatible with Odoo 13.0
- Easy to install and configure

## Dependencies

This module depends on the following:
* `base`
* `account`
* `product`
* `product_brand` (from OCA)

### Installing OCA product_brand

This module requires the `product_brand` module from the OCA (Odoo Community Association). To install it:

1. Clone the OCA/brand repository:
   ```
   git clone https://github.com/OCA/brand.git -b 13.0
   ```

2. Add the cloned `brand` directory to your Odoo addons path. You can do this by:
   - Moving the `brand` directory to your existing addons path, or
   - Adding the path to the `brand` directory in your Odoo configuration file:
     ```
     addons_path = /path/to/existing/addons,/path/to/brand
     ```

3. Restart your Odoo server.

4. Go to Apps in your Odoo instance, remove the 'Apps' filter and search for 'product_brand'.

5. Install the `product_brand` module.

## Installation

Once the dependencies are satisfied:

1. Add this repository to your Odoo addons path.
2. Update your apps list in Odoo.
3. Search for 'DH Invoice Brand Report' in the Apps menu.
4. Click Install.

## Configuration
No additional configuration is needed. Once installed, the module will automatically add the brand information to your invoice reports.

## Usage
After installation:
1. Create a new invoice or open an existing one
2. Add products to the invoice lines as usual
3. Generate the PDF report
4. The brand information will appear in a new column on the invoice report

## Support
For support, please contact:
- Email: dino.herlambang@gmail.com
- Website: http://instagram.com/_dinoherlambang_/

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check our issues page or submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by Dino Herlambang

---

We hope this module enhances your Odoo experience! For any questions or feedback, please don't hesitate to contact us.