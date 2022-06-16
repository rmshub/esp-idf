# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wifi_constants.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14wifi_constants.proto\"v\n\x12WifiConnectedState\x12\x10\n\x08ip4_addr\x18\x01 \x01(\t\x12 \n\tauth_mode\x18\x02 \x01(\x0e\x32\r.WifiAuthMode\x12\x0c\n\x04ssid\x18\x03 \x01(\x0c\x12\r\n\x05\x62ssid\x18\x04 \x01(\x0c\x12\x0f\n\x07\x63hannel\x18\x05 \x01(\x05*Y\n\x10WifiStationState\x12\r\n\tConnected\x10\x00\x12\x0e\n\nConnecting\x10\x01\x12\x10\n\x0c\x44isconnected\x10\x02\x12\x14\n\x10\x43onnectionFailed\x10\x03*=\n\x17WifiConnectFailedReason\x12\r\n\tAuthError\x10\x00\x12\x13\n\x0fNetworkNotFound\x10\x01*c\n\x0cWifiAuthMode\x12\x08\n\x04Open\x10\x00\x12\x07\n\x03WEP\x10\x01\x12\x0b\n\x07WPA_PSK\x10\x02\x12\x0c\n\x08WPA2_PSK\x10\x03\x12\x10\n\x0cWPA_WPA2_PSK\x10\x04\x12\x13\n\x0fWPA2_ENTERPRISE\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wifi_constants_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WIFISTATIONSTATE._serialized_start=144
  _WIFISTATIONSTATE._serialized_end=233
  _WIFICONNECTFAILEDREASON._serialized_start=235
  _WIFICONNECTFAILEDREASON._serialized_end=296
  _WIFIAUTHMODE._serialized_start=298
  _WIFIAUTHMODE._serialized_end=397
  _WIFICONNECTEDSTATE._serialized_start=24
  _WIFICONNECTEDSTATE._serialized_end=142
# @@protoc_insertion_point(module_scope)
