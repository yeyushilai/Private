package main


import (
"fmt"
)

func main() {
	// 格式化输出
	// %d 表示整型数字，%s 表示字符串
	var stockcode=123
	var enddate="2020-12-31"
	var url="Code=%d&endDate=%s"
	var target_url=fmt.Sprintf(url,stockcode,enddate)
	fmt.Println(target_url)


	// 定义多个变量
	var a, b int = 3, 6
	var c bool
	fmt.Println(b)
	fmt.Println(a)
	fmt.Println(c)
}
