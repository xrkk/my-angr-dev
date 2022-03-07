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
lib.set_library_names("dhcpcsvc.dll")
prototypes = \
    {
        # 
        'DhcpCApiInitialize': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Version"]),
        # 
        'DhcpCApiCleanup': SimTypeFunction([], SimTypeBottom(label="Void")),
        # 
        'DhcpRequestParams': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPCAPI_CLASSID", pack=False, align=None), offset=0), SimStruct({"nParams": SimTypeInt(signed=False, label="UInt32"), "Params": SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "OptionId": SimTypeInt(signed=False, label="UInt32"), "IsVendor": SimTypeInt(signed=True, label="Int32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPAPI_PARAMS", pack=False, align=None), offset=0)}, name="DHCPCAPI_PARAMS_ARRAY", pack=False, align=None), SimStruct({"nParams": SimTypeInt(signed=False, label="UInt32"), "Params": SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "OptionId": SimTypeInt(signed=False, label="UInt32"), "IsVendor": SimTypeInt(signed=True, label="Int32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPAPI_PARAMS", pack=False, align=None), offset=0)}, name="DHCPCAPI_PARAMS_ARRAY", pack=False, align=None), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Flags", "Reserved", "AdapterName", "ClassId", "SendParams", "RecdParams", "Buffer", "pSize", "RequestIdStr"]),
        # 
        'DhcpUndoRequestParams': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Flags", "Reserved", "AdapterName", "RequestIdStr"]),
        # 
        'DhcpRegisterParamChange': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPCAPI_CLASSID", pack=False, align=None), offset=0), SimStruct({"nParams": SimTypeInt(signed=False, label="UInt32"), "Params": SimTypePointer(SimStruct({"Flags": SimTypeInt(signed=False, label="UInt32"), "OptionId": SimTypeInt(signed=False, label="UInt32"), "IsVendor": SimTypeInt(signed=True, label="Int32"), "Data": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "nBytesData": SimTypeInt(signed=False, label="UInt32")}, name="DHCPAPI_PARAMS", pack=False, align=None), offset=0)}, name="DHCPCAPI_PARAMS_ARRAY", pack=False, align=None), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Flags", "Reserved", "AdapterName", "ClassId", "Params", "Handle"]),
        # 
        'DhcpDeRegisterParamChange': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Flags", "Reserved", "Event"]),
        # 
        'DhcpRemoveDNSRegistrations': SimTypeFunction([], SimTypeInt(signed=False, label="UInt32")),
        # 
        'DhcpGetOriginalSubnetMask': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["sAdapterName", "dwSubnetMask"]),
        # 
        'McastApiStartup': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["Version"]),
        # 
        'McastApiCleanup': SimTypeFunction([], SimTypeBottom(label="Void")),
        # 
        'McastGenUID': SimTypeFunction([SimTypePointer(SimStruct({"ClientUID": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ClientUIDLength": SimTypeInt(signed=False, label="UInt32")}, name="MCAST_CLIENT_UID", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["pRequestID"]),
        # 
        'McastEnumerateScopes': SimTypeFunction([SimTypeShort(signed=False, label="UInt16"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimStruct({"ScopeCtx": SimStruct({"ScopeID": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "Interface": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "ServerID": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None")}, name="MCAST_SCOPE_CTX", pack=False, align=None), "LastAddr": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "TTL": SimTypeInt(signed=False, label="UInt32"), "ScopeDesc": SimTypeBottom(label="UNICODE_STRING")}, name="MCAST_SCOPE_ENTRY", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["AddrFamily", "ReQuery", "pScopeList", "pScopeLen", "pScopeCount"]),
        # 
        'McastRequestAddress': SimTypeFunction([SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimStruct({"ClientUID": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ClientUIDLength": SimTypeInt(signed=False, label="UInt32")}, name="MCAST_CLIENT_UID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"ScopeID": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "Interface": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "ServerID": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None")}, name="MCAST_SCOPE_CTX", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"LeaseStartTime": SimTypeInt(signed=True, label="Int32"), "MaxLeaseStartTime": SimTypeInt(signed=True, label="Int32"), "LeaseDuration": SimTypeInt(signed=False, label="UInt32"), "MinLeaseDuration": SimTypeInt(signed=False, label="UInt32"), "ServerAddress": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "MinAddrCount": SimTypeShort(signed=False, label="UInt16"), "AddrCount": SimTypeShort(signed=False, label="UInt16"), "pAddrBuf": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="MCAST_LEASE_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"LeaseStartTime": SimTypeInt(signed=True, label="Int32"), "LeaseEndTime": SimTypeInt(signed=True, label="Int32"), "ServerAddress": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "AddrCount": SimTypeShort(signed=False, label="UInt16"), "pAddrBuf": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="MCAST_LEASE_RESPONSE", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["AddrFamily", "pRequestID", "pScopeCtx", "pAddrRequest", "pAddrResponse"]),
        # 
        'McastRenewAddress': SimTypeFunction([SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimStruct({"ClientUID": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ClientUIDLength": SimTypeInt(signed=False, label="UInt32")}, name="MCAST_CLIENT_UID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"LeaseStartTime": SimTypeInt(signed=True, label="Int32"), "MaxLeaseStartTime": SimTypeInt(signed=True, label="Int32"), "LeaseDuration": SimTypeInt(signed=False, label="UInt32"), "MinLeaseDuration": SimTypeInt(signed=False, label="UInt32"), "ServerAddress": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "MinAddrCount": SimTypeShort(signed=False, label="UInt16"), "AddrCount": SimTypeShort(signed=False, label="UInt16"), "pAddrBuf": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="MCAST_LEASE_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"LeaseStartTime": SimTypeInt(signed=True, label="Int32"), "LeaseEndTime": SimTypeInt(signed=True, label="Int32"), "ServerAddress": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "AddrCount": SimTypeShort(signed=False, label="UInt16"), "pAddrBuf": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="MCAST_LEASE_RESPONSE", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["AddrFamily", "pRequestID", "pRenewRequest", "pRenewResponse"]),
        # 
        'McastReleaseAddress': SimTypeFunction([SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimStruct({"ClientUID": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ClientUIDLength": SimTypeInt(signed=False, label="UInt32")}, name="MCAST_CLIENT_UID", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"LeaseStartTime": SimTypeInt(signed=True, label="Int32"), "MaxLeaseStartTime": SimTypeInt(signed=True, label="Int32"), "LeaseDuration": SimTypeInt(signed=False, label="UInt32"), "MinLeaseDuration": SimTypeInt(signed=False, label="UInt32"), "ServerAddress": SimUnion({"IpAddrV4": SimTypeInt(signed=False, label="UInt32"), "IpAddrV6": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="<anon>", label="None"), "MinAddrCount": SimTypeShort(signed=False, label="UInt16"), "AddrCount": SimTypeShort(signed=False, label="UInt16"), "pAddrBuf": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="MCAST_LEASE_REQUEST", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["AddrFamily", "pRequestID", "pReleaseRequest"]),
    }

lib.set_prototypes(prototypes)
