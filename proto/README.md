# Example protos

## Contents

- [helloworld.proto]
  - The simple example used in the overview.
- [route_guide.proto]
  - An example service described in detail in the tutorial.
  
  
## Command to use for converting proto to python file
  $ python3 -m grpc_tools.protoc -I=. --python_out=./ --grpc_python_out=./ ./product.proto

  $ python3 -m grpc_tools.protoc -I=. --python_out=./ --grpc_python_out=./ ./supplier.proto

