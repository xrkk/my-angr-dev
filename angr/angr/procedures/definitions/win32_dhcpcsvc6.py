# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("dhcpcsvc6.dll")
prototypes = \
    {
        # 
        'Dhcpv6CApiInitialize': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeBottom(label="Void"), arg_names=["Version"]),
        # 
        'Dhcpv6CApiCleanup': SimTypeFunction([], SimTypeBottom(label="Void")),
        # 
        'Dhcpv6RequestParams': SimTypeFunction([SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6CAPI_CLASSID", pack=False, align=None), offset=0), SimStruct({"nParams": SimTypeInt(signed=False, label="UInt32"), "Params": SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "OptionId": SimTypeInt(signed=False, label="UInt32"), "IsVendor": SimTypeInt(signed=True, label="Int32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6CAPI_PARAMS", pack=False, align=None), offset=0)}, name="DHCPV6CAPI_PARAMS_ARRAY", pack=False, align=None), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["forceNewInform", "reserved", "adapterName", "classId", "recdParams", "buffer", "pSize"]),
        # 
        'Dhcpv6RequestPrefix': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6CAPI_CLASSID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"nPrefixes": SimTypeInt(signed=False, label="UInt32"), "prefixArray": SimTypePointer(SimStruct({"prefix": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "prefixLength": SimTypeInt(signed=False, label="UInt32"), "preferredLifeTime": SimTypeInt(signed=False, label="UInt32"), "validLifeTime": SimTypeInt(signed=False, label="UInt32"), "status": SimTypeInt(signed=False, label="StatusCode")}, name="DHCPV6Prefix", pack=False, align=None), offset=0), "iaid": SimTypeInt(signed=False, label="UInt32"), "T1": SimTypeLongLong(signed=True, label="Int64"), "T2": SimTypeLongLong(signed=True, label="Int64"), "MaxLeaseExpirationTime": SimTypeLongLong(signed=True, label="Int64"), "LastRenewalTime": SimTypeLongLong(signed=True, label="Int64"), "status": SimTypeInt(signed=False, label="StatusCode"), "ServerId": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ServerIdLen": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6PrefixLeaseInformation", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["adapterName", "pclassId", "prefixleaseInfo", "pdwTimeToWait"]),
        # 
        'Dhcpv6RenewPrefix': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6CAPI_CLASSID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"nPrefixes": SimTypeInt(signed=False, label="UInt32"), "prefixArray": SimTypePointer(SimStruct({"prefix": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "prefixLength": SimTypeInt(signed=False, label="UInt32"), "preferredLifeTime": SimTypeInt(signed=False, label="UInt32"), "validLifeTime": SimTypeInt(signed=False, label="UInt32"), "status": SimTypeInt(signed=False, label="StatusCode")}, name="DHCPV6Prefix", pack=False, align=None), offset=0), "iaid": SimTypeInt(signed=False, label="UInt32"), "T1": SimTypeLongLong(signed=True, label="Int64"), "T2": SimTypeLongLong(signed=True, label="Int64"), "MaxLeaseExpirationTime": SimTypeLongLong(signed=True, label="Int64"), "LastRenewalTime": SimTypeLongLong(signed=True, label="Int64"), "status": SimTypeInt(signed=False, label="StatusCode"), "ServerId": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ServerIdLen": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6PrefixLeaseInformation", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["adapterName", "pclassId", "prefixleaseInfo", "pdwTimeToWait", "bValidatePrefix"]),
        # 
        'Dhcpv6ReleasePrefix': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6CAPI_CLASSID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"nPrefixes": SimTypeInt(signed=False, label="UInt32"), "prefixArray": SimTypePointer(SimStruct({"prefix": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "prefixLength": SimTypeInt(signed=False, label="UInt32"), "preferredLifeTime": SimTypeInt(signed=False, label="UInt32"), "validLifeTime": SimTypeInt(signed=False, label="UInt32"), "status": SimTypeInt(signed=False, label="StatusCode")}, name="DHCPV6Prefix", pack=False, align=None), offset=0), "iaid": SimTypeInt(signed=False, label="UInt32"), "T1": SimTypeLongLong(signed=True, label="Int64"), "T2": SimTypeLongLong(signed=True, label="Int64"), "MaxLeaseExpirationTime": SimTypeLongLong(signed=True, label="Int64"), "LastRenewalTime": SimTypeLongLong(signed=True, label="Int64"), "status": SimTypeInt(signed=False, label="StatusCode"), "ServerId": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ServerIdLen": SimTypeInt(signed=False, label="UInt32")}, name="DHCPV6PrefixLeaseInformation", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["adapterName", "classId", "leaseInfo"]),
    }

lib.set_prototypes(prototypes)
