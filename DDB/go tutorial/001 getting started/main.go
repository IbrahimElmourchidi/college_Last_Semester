package main

const N = 100

var done = make(chan int)

func c() {
	for i := 0; i < N; i++ {
		print("-")
	}
	done <- 0
}
func main() {
	println("begin") // A
	go c()           // fork C
	for i := 0; i < N; i++ {
		print(".") // B
	}
	<-done           // wait C
	println("\nend") // D
}
