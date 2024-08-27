# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import voice_pb2 as voice__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in voice_pb2_grpc.py depends on' # noqa: F541
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class VoiceStub(object):
    """Service to stream live voice of a participant in a call.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamingVoice = channel.stream_stream(
                '/five9.voicestream.Voice/StreamingVoice',
                request_serializer=voice__pb2.StreamingVoiceRequest.SerializeToString,
                response_deserializer=voice__pb2.StreamingVoiceResponse.FromString,
                _registered_method=True)


class VoiceServicer(object):
    """Service to stream live voice of a participant in a call.
    """

    def StreamingVoice(self, request_iterator, context):
        """Method for bidirectional streaming of messages:
        send audio of the user's speech and receive feedback in response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamingVoice': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingVoice,
                    request_deserializer=voice__pb2.StreamingVoiceRequest.FromString,
                    response_serializer=voice__pb2.StreamingVoiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'five9.voicestream.Voice', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('five9.voicestream.Voice', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Voice(object):
    """Service to stream live voice of a participant in a call.
    """

    @staticmethod
    def StreamingVoice(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/five9.voicestream.Voice/StreamingVoice',
            voice__pb2.StreamingVoiceRequest.SerializeToString,
            voice__pb2.StreamingVoiceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)