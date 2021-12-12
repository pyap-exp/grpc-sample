# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import product_pb2 as product__pb2


class ProductStub(object):
    """The Inventory service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getProduct = channel.unary_unary(
                '/product.Product/getProduct',
                request_serializer=product__pb2.GetProductRequest.SerializeToString,
                response_deserializer=product__pb2.GetProductResponse.FromString,
                )
        self.setProduct = channel.unary_unary(
                '/product.Product/setProduct',
                request_serializer=product__pb2.SetProductRequest.SerializeToString,
                response_deserializer=product__pb2.SetProductResponse.FromString,
                )
        self.getBrandName = channel.unary_unary(
                '/product.Product/getBrandName',
                request_serializer=product__pb2.GetBrandNameRequest.SerializeToString,
                response_deserializer=product__pb2.GetBrandNameResponse.FromString,
                )
        self.setBrandName = channel.unary_unary(
                '/product.Product/setBrandName',
                request_serializer=product__pb2.SetBrandNameRequest.SerializeToString,
                response_deserializer=product__pb2.SetBrandNameResponse.FromString,
                )


class ProductServicer(object):
    """The Inventory service definition.
    """

    def getProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBrandName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setBrandName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.getProduct,
                    request_deserializer=product__pb2.GetProductRequest.FromString,
                    response_serializer=product__pb2.GetProductResponse.SerializeToString,
            ),
            'setProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.setProduct,
                    request_deserializer=product__pb2.SetProductRequest.FromString,
                    response_serializer=product__pb2.SetProductResponse.SerializeToString,
            ),
            'getBrandName': grpc.unary_unary_rpc_method_handler(
                    servicer.getBrandName,
                    request_deserializer=product__pb2.GetBrandNameRequest.FromString,
                    response_serializer=product__pb2.GetBrandNameResponse.SerializeToString,
            ),
            'setBrandName': grpc.unary_unary_rpc_method_handler(
                    servicer.setBrandName,
                    request_deserializer=product__pb2.SetBrandNameRequest.FromString,
                    response_serializer=product__pb2.SetBrandNameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.Product', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Product(object):
    """The Inventory service definition.
    """

    @staticmethod
    def getProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/getProduct',
            product__pb2.GetProductRequest.SerializeToString,
            product__pb2.GetProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/setProduct',
            product__pb2.SetProductRequest.SerializeToString,
            product__pb2.SetProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBrandName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/getBrandName',
            product__pb2.GetBrandNameRequest.SerializeToString,
            product__pb2.GetBrandNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setBrandName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/setBrandName',
            product__pb2.SetBrandNameRequest.SerializeToString,
            product__pb2.SetBrandNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
