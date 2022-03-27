package main

import (
	"fmt"
	"os"
)

func main(){
	getArgsFromTerminal(os.Args);
	sayHello("Ibrahim Elmourchidi")
	fullName, nameLength  := getFullNameInfo("Ibrahim", "Elmourchidi")
	fmt.Println("Your Full Name is:", fullName, "\nYour Name Length:", nameLength)
	fmt.Println(calc(1,2, "sum"))
}

func getArgsFromTerminal(args []string){
	for i:= 1; i<len(args); i++{
		fmt.Println(args[i], " ")
	}
}

// function that takes the name as argument and print hello message 

func sayHello(name string){
	fmt.Println("Helllo,", name)
}

// function that returns the full name and the length of the full name
// notice since the two args of the same type we can write the type only once

func getFullNameInfo(firstName, lastName string) (string, int){
	// var fullName string = firstName+" "+lastName
	// var nameLength int = len(fullName)
	// you can use the auto type detection syntax
	fullName := firstName + " " + lastName
	nameLength := len(fullName)
	return fullName, nameLength
}

// make simple calculator
func calc(num1,num2 float32, operator string  ) float32{
	switch operator{
	case "min":
		return num1-num2
	case "mul":
		return num1*num2
	case "div":
		return num1/num2
	default:
		return num1+num2
	}
}

