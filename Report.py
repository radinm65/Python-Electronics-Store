from FileCommands import FileCommands
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference


class Report:

    @staticmethod
    def generate_top_customers_report():

        customers = FileCommands.get_file_data("./Database/Customers.json")

        report_data = []

        for customer in customers:
            total_spent = 0
            items_bought = 0

            for product in customer["bought"]:
                total_spent += product["price"]
                items_bought += 1

            report_data.append({
                "name": customer["firstname"] + " " + customer["lastname"],
                "total_spent": total_spent,
                "items_bought": items_bought
            })


        # مرتب سازی بر اساس پول خرج شده
        report_data.sort(
            key=lambda x: x["total_spent"],
            reverse=True
        )


        top_5 = report_data[:5]


        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Top Customers"


        sheet.append([
            "Customer",
            "Total Spent",
            "Items Bought"
        ])


        for customer in top_5:
            sheet.append([
                customer["name"],
                customer["total_spent"],
                customer["items_bought"]
            ])


        # Bar Chart
        chart = BarChart()
        chart.title = "Top 5 Customers By Spending"
        chart.y_axis.title = "Money"
        chart.x_axis.title = "Customer"


        data = Reference(
            sheet,
            min_col=2,
            min_row=1,
            max_row=len(top_5)+1
        )

        categories = Reference(
            sheet,
            min_col=1,
            min_row=2,
            max_row=len(top_5)+1
        )


        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)

        sheet.add_chart(chart, "E2")


        workbook.save("./Reports/Top_Customers_Report.xlsx")

        return True



    @staticmethod
    def generate_top_sellers_report():

        sellers = FileCommands.get_file_data("./Database/Sellers.json")

        report_data = []


        for seller in sellers:

            total_sales = 0
            items_sold = 0


            for product in seller["sold"]:
                total_sales += product["price"]
                items_sold += 1


            report_data.append({

                "name": seller["firstname"] + " " + seller["lastname"],
                "total_sales": total_sales,
                "items_sold": items_sold

            })


        report_data.sort(
            key=lambda x: x["total_sales"],
            reverse=True
        )


        top_5 = report_data[:5]


        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Top Sellers"


        sheet.append([
            "Seller",
            "Total Sales",
            "Items Sold"
        ])


        for seller in top_5:
            sheet.append([
                seller["name"],
                seller["total_sales"],
                seller["items_sold"]
            ])



        # Bar Chart
        chart = BarChart()

        chart.title = "Top 5 Sellers By Revenue"
        chart.y_axis.title = "Revenue"
        chart.x_axis.title = "Seller"


        data = Reference(
            sheet,
            min_col=2,
            min_row=1,
            max_row=len(top_5)+1
        )


        categories = Reference(
            sheet,
            min_col=1,
            min_row=2,
            max_row=len(top_5)+1
        )


        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)


        sheet.add_chart(chart, "E2")


        workbook.save("./Reports/Top_Sellers_Report.xlsx")

        return True