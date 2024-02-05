# golang

run go code in python.

WIP

```shell
pip install golang
```

```python
import golang

code = """
package main
import "fmt"

func main(){
    fmt.Println("Hello World from github.com/menduo/golang")
}
"""
golang.run(code)

# golang.run(filepath)
```