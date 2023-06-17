package main

import (
        "bufio"
        "fmt"
        "net/http"
        "os"
        "time"
)

var website string

func main() {

        if len(os.Args[1:]) == 0 {
                fmt.Println("Input website:")
                url := bufio.NewScanner(os.Stdin)
                url.Scan()
                website = url.Text()
        } else {
                website = os.Args[1:][0]
        }

        if website[:7] != "http://" && website[:8] != "https://" {
                website = "http://" + website
        }

        fmt.Println("Searching...")
        time.Sleep(1 * time.Second)

        resp, err := http.Get(website)
        if err != nil {
                panic(err)
        }
        defer resp.Body.Close()

        scanner := bufio.NewScanner(resp.Body)
        for i := 0; scanner.Scan() && i < 5; i++ {
                fmt.Println(scanner.Text())
        }
        if err := scanner.Err(); err != nil {
                panic(err)
        }
}