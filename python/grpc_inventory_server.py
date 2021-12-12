# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import product_pb2,product_pb2_grpc,supplier_pb2,supplier_pb2_grpc



class ProductServer(product_pb2_grpc.ProductServicer):

    def getProduct(self, request, context):
        return product_pb2.GetProductResponse(message='product=getProduct, %s!' % request.name)

    def setProduct(self, request, context):
        return product_pb2.SetProductResponse(message='product=setProduct, %s!' % request.name)

    def getBrandName(self, request, context):
        return product_pb2.GetBrandNameResponse(message='product=getBrandName, %s!' % request.name)

    def setBrandName(self, request, context):
        return product_pb2.SetBrandNameResponse(message='product=setBrandName, %s!' % request.name)            

class SupplierServer(supplier_pb2_grpc.SupplierServicer):

    def getSource(self, request, context):
        return supplier_pb2.GetSourceResponse(message='supplier=getSource, %s!' % request.name)
    def setSource(self, request, context):
        return supplier_pb2.SetSourceResponse(message='supplier=setSource, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServicer_to_server(ProductServer(), server)
    supplier_pb2_grpc.add_SupplierServicer_to_server(SupplierServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
