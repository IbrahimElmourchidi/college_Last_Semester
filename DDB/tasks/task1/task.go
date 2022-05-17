package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	clearScreen()
	db, err := sql.Open("mysql", "root:@tcp(localhost:3306)/goTask1")
	if err != nil {
		fmt.Println("Database error")
	}
	defer db.Close()
	// initTables(db)
	option := initView(db)
	switch option {
	case "1":
		printAllProducts(db, getAllProducts(db))
	case "2":
		getSingleProduct(db)
	case "3":
		addNewProduct(db)
	case "4":
		updateProduct(db)
	case "5":
		delteProduct(db)
	case "6":
		clearDatabase(db)
	case "7":
		return
	default:
		main()
	}
	// clearDatabase(db)
	// printAllProducts(db, getAllProducts(db))
	// addNewProduct(db, "nike shoes", "a more amazing shoe", "5")
	// delteProduct(db, "10")
	// updateProduct(db, "11", "addidas shoes", "a more amazing shoes", "55")
	// getSingleProduct(db, "12")
	// printAllProducts(db, getAllProducts(db))

}

func getAllProducts(db *sql.DB) *sql.Rows {
	rows, err := db.Query("select * from products")
	if err != nil {
		fmt.Println("Database error")
	}

	return rows
}

func printAllProducts(db *sql.DB, rows *sql.Rows) {
	clearScreen()
	fmt.Println("\n========================================================")
	fmt.Println(getColNames(db))
	for rows.Next() {
		var prod_id, prod_name, prod_desc, prod_rate string
		err := rows.Scan(&prod_id, &prod_name, &prod_desc, &prod_rate)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(prod_id+"\t", prod_name+"\t", prod_desc+"\t", prod_rate+"\t")
	}
	fmt.Println("========================================================\n")
	rows.Close()
	subInitView()
}

func getColNames(db *sql.DB) []string {
	var colNames []string
	cols, err := db.Query(`SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='goTask1' AND TABLE_NAME='products'; `)
	if err != nil {
		fmt.Println("error while getting the col names")
	}
	for cols.Next() {
		var col string
		err := cols.Scan(&col)
		if err != nil {
			fmt.Println(err)
		}
		colNames = append(colNames, col)
	}
	return colNames
}

func getSingleProduct(db *sql.DB) {
	clearScreen()
	var id string
	fmt.Print("please enter the product id\n>>>  ")
	fmt.Scan(&id)
	result, err := db.Query("select * from products where product_id  = " + id)
	if err != nil {
		fmt.Println("error while updating product", id)
	}
	printAllProducts(db, result)
	result.Close()
	subInitView()
}

func addNewProduct(db *sql.DB) {
	clearScreen()
	var prodName, prodDesc, prodRate string
	fmt.Print("Please enter the product name :  ")
	fmt.Scan(&prodName)
	fmt.Print("Please enter the product description :  ")
	fmt.Scan(&prodDesc)
	fmt.Print("Please enter the product prodRate :  ")
	fmt.Scan(&prodRate)
	result, err := db.Query("INSERT INTO `products` (`product_id`, `product_name`, `product_description`, `product_rate`) VALUES (NULL, '" + prodName + "', '" + prodDesc + "', '" + prodRate + "');")
	if err != nil {
		fmt.Println("error while inserting")
	}
	result.Close()
	fmt.Println("\n ======= Added Successfully")
	subInitView()
}

func updateProduct(db *sql.DB) {
	var id, prodName, prodDesc, prodRate string
	fmt.Print("Please enter the product id:  ")
	fmt.Scan(&id)
	fmt.Print("Please enter the product new name :  ")
	fmt.Scan(&prodName)
	fmt.Print("Please enter the product new description :  ")
	fmt.Scan(&prodDesc)
	fmt.Print("Please enter the product new Rate :  ")
	fmt.Scan(&prodRate)
	result, err := db.Query("UPDATE `products` SET `product_name` = '" + prodName + "', `product_description` = '" + prodDesc + "', `product_rate` = '" + prodRate + "' WHERE `products`.`product_id` = " + id + "; ")
	if err != nil {
		fmt.Println("error while updating product", id)
	}
	result.Close()
	subInitView()
}

func delteProduct(db *sql.DB) {
	var id string
	fmt.Print("Please enter the product id :  ")
	fmt.Scan(&id)
	result, err := db.Query("delete from products where product_id =" + id)
	if err != nil {
		fmt.Println("error while deleting product", id)
	}
	result.Close()
	subInitView()
}

func clearScreen() {
	fmt.Print("\033[H\033[2J")
}

func initView(db *sql.DB) string {
	var option string
	fmt.Println("\n\n\n************ Welcome to the go DB task1 home page ***********")
	fmt.Println("\nPlease Select your option\n")
	fmt.Println("\t1: Get All Products")
	fmt.Println("\t2: Get a Single Product")
	fmt.Println("\t3: Add a Product")
	fmt.Println("\t4: Update a Product")
	fmt.Println("\t5: Delete a Product")
	fmt.Println("\t6: clear database")
	fmt.Println("\t7: Exit\n")
	fmt.Print("Your Choise>>>  ")
	fmt.Scan(&option)
	return option
}

func subInitView() {
	var option string
	fmt.Println("\nPlease Select your option\n")
	fmt.Println("\t1: Home Page")
	fmt.Println("\t2: Exit")
	fmt.Print("Your Choise>>>  ")
	fmt.Scan(&option)
	switch option {
	case "1":
		main()
	case "2":
		return
	default:
		fmt.Println("\n =======invalid option=======")
		subInitView()
	}
}

func clearDatabase(db *sql.DB) {
	result, err := db.Query("delete from products")
	if err != nil {
		fmt.Println("error while clear the database")
	}
	result.Close()
	fmt.Println("\n========= Database was cleared =========\n")
	subInitView()
}

// func initTables(db *sql.DB) {
// 	result, err := db.Query(`CREATE TABLE IF NOT EXISTS products (
// 		product_id int NOT NULL AUTO_INCREMENT,
// 		product_name varchar(255) NOT NULL,
// 		product_description varchar(255) NOT NULL,
// 		product_rate FLOAT,
// 		PRIMARY KEY (ID)
// 	); `)
// 	if err != nil {
// 		fmt.Println("cannot create the products table")
// 	}
// 	result.Close()
// }
