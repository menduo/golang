# golang

Run Go code in Python.

⚠️: WIP

# install

```shell
pip install golang
```

# or

```shell
pip install git+ssh://git@github.com/menduo/golang.git
```

# example

```python
import golang

code = """
package main
import "fmt"

func main(){
    fmt.Println("Hello World from github.com/menduo/golang")
}
"""
golang.run_code(code)

# golang.run(filepath)
```