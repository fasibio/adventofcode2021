package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {

	file, _ := ioutil.ReadFile("input2.txt")
	lines := strings.Split(string(file), "\n")
	oldLineValue, _ := strconv.ParseInt(lines[0], 10, 64)
	matches := 0

	for _, v := range lines {
		if v == "" {
			continue
		}
		lineValue, _ := strconv.ParseInt(v, 10, 64)
		if lineValue > oldLineValue {
			matches++
		}
		oldLineValue = lineValue
	}

	print("Hello, World!", matches)
}
