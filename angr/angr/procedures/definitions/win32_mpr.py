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
lib.set_library_names("mpr.dll")
prototypes = \
    {
        # 
        'WNetAddConnectionA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpRemoteName", "lpPassword", "lpLocalName"]),
        # 
        'WNetAddConnectionW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpRemoteName", "lpPassword", "lpLocalName"]),
        # 
        'WNetAddConnection2A': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpPassword", "lpUserName", "dwFlags"]),
        # 
        'WNetAddConnection2W': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpPassword", "lpUserName", "dwFlags"]),
        # 
        'WNetAddConnection3A': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "lpPassword", "lpUserName", "dwFlags"]),
        # 
        'WNetAddConnection3W': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "lpPassword", "lpUserName", "dwFlags"]),
        # 
        'WNetAddConnection4A': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "pAuthBuffer", "cbAuthBuffer", "dwFlags", "lpUseOptions", "cbUseOptions"]),
        # 
        'WNetAddConnection4W': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "pAuthBuffer", "cbAuthBuffer", "dwFlags", "lpUseOptions", "cbUseOptions"]),
        # 
        'WNetCancelConnectionA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "fForce"]),
        # 
        'WNetCancelConnectionW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "fForce"]),
        # 
        'WNetCancelConnection2A': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "dwFlags", "fForce"]),
        # 
        'WNetCancelConnection2W': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "dwFlags", "fForce"]),
        # 
        'WNetGetConnectionA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpLocalName", "lpRemoteName", "lpnLength"]),
        # 
        'WNetGetConnectionW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpLocalName", "lpRemoteName", "lpnLength"]),
        # 
        'WNetUseConnectionA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="NET_USE_CONNECT_FLAGS"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "lpPassword", "lpUserId", "dwFlags", "lpAccessName", "lpBufferSize", "lpResult"]),
        # 
        'WNetUseConnectionW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="NET_USE_CONNECT_FLAGS"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "lpPassword", "lpUserId", "dwFlags", "lpAccessName", "lpBufferSize", "lpResult"]),
        # 
        'WNetUseConnection4A': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "pAuthBuffer", "cbAuthBuffer", "dwFlags", "lpUseOptions", "cbUseOptions", "lpAccessName", "lpBufferSize", "lpResult"]),
        # 
        'WNetUseConnection4W': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndOwner", "lpNetResource", "pAuthBuffer", "cbAuthBuffer", "dwFlags", "lpUseOptions", "cbUseOptions", "lpAccessName", "lpBufferSize", "lpResult"]),
        # 
        'WNetConnectionDialog': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwnd", "dwType"]),
        # 
        'WNetDisconnectDialog': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwnd", "dwType"]),
        # 
        'WNetConnectionDialog1A': SimTypeFunction([SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "hwndOwner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "lpConnRes": SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), "dwFlags": SimTypeInt(signed=False, label="CONNECTDLGSTRUCT_FLAGS"), "dwDevNum": SimTypeInt(signed=False, label="UInt32")}, name="CONNECTDLGSTRUCTA", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpConnDlgStruct"]),
        # 
        'WNetConnectionDialog1W': SimTypeFunction([SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "hwndOwner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "lpConnRes": SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), "dwFlags": SimTypeInt(signed=False, label="CONNECTDLGSTRUCT_FLAGS"), "dwDevNum": SimTypeInt(signed=False, label="UInt32")}, name="CONNECTDLGSTRUCTW", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpConnDlgStruct"]),
        # 
        'WNetDisconnectDialog1A': SimTypeFunction([SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "hwndOwner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "dwFlags": SimTypeInt(signed=False, label="DISCDLGSTRUCT_FLAGS")}, name="DISCDLGSTRUCTA", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpConnDlgStruct"]),
        # 
        'WNetDisconnectDialog1W': SimTypeFunction([SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "hwndOwner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwFlags": SimTypeInt(signed=False, label="DISCDLGSTRUCT_FLAGS")}, name="DISCDLGSTRUCTW", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpConnDlgStruct"]),
        # 
        'WNetOpenEnumA': SimTypeFunction([SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), SimTypeInt(signed=False, label="WNET_OPEN_ENUM_USAGE"), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwScope", "dwType", "dwUsage", "lpNetResource", "lphEnum"]),
        # 
        'WNetOpenEnumW': SimTypeFunction([SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), SimTypeInt(signed=False, label="WNET_OPEN_ENUM_USAGE"), SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwScope", "dwType", "dwUsage", "lpNetResource", "lphEnum"]),
        # 
        'WNetEnumResourceA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hEnum", "lpcCount", "lpBuffer", "lpBufferSize"]),
        # 
        'WNetEnumResourceW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hEnum", "lpcCount", "lpBuffer", "lpBufferSize"]),
        # 
        'WNetCloseEnum': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hEnum"]),
        # 
        'WNetGetResourceParentA': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpBuffer", "lpcbBuffer"]),
        # 
        'WNetGetResourceParentW': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpBuffer", "lpcbBuffer"]),
        # 
        'WNetGetResourceInformationA': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpBuffer", "lpcbBuffer", "lplpSystem"]),
        # 
        'WNetGetResourceInformationW': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpBuffer", "lpcbBuffer", "lplpSystem"]),
        # 
        'WNetGetUniversalNameA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UNC_INFO_LEVEL"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpLocalPath", "dwInfoLevel", "lpBuffer", "lpBufferSize"]),
        # 
        'WNetGetUniversalNameW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UNC_INFO_LEVEL"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpLocalPath", "dwInfoLevel", "lpBuffer", "lpBufferSize"]),
        # 
        'WNetGetUserA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "lpUserName", "lpnLength"]),
        # 
        'WNetGetUserW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpName", "lpUserName", "lpnLength"]),
        # 
        'WNetGetProviderNameA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwNetType", "lpProviderName", "lpBufferSize"]),
        # 
        'WNetGetProviderNameW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwNetType", "lpProviderName", "lpBufferSize"]),
        # 
        'WNetGetNetworkInformationA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "dwProviderVersion": SimTypeInt(signed=False, label="UInt32"), "dwStatus": SimTypeBottom(label="WIN32_ERROR"), "dwCharacteristics": SimTypeInt(signed=False, label="NETINFOSTRUCT_CHARACTERISTICS"), "dwHandle": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "wNetType": SimTypeShort(signed=False, label="UInt16"), "dwPrinters": SimTypeInt(signed=False, label="UInt32"), "dwDrives": SimTypeInt(signed=False, label="UInt32")}, name="NETINFOSTRUCT", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpProvider", "lpNetInfoStruct"]),
        # 
        'WNetGetNetworkInformationW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "dwProviderVersion": SimTypeInt(signed=False, label="UInt32"), "dwStatus": SimTypeBottom(label="WIN32_ERROR"), "dwCharacteristics": SimTypeInt(signed=False, label="NETINFOSTRUCT_CHARACTERISTICS"), "dwHandle": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "wNetType": SimTypeShort(signed=False, label="UInt16"), "dwPrinters": SimTypeInt(signed=False, label="UInt32"), "dwDrives": SimTypeInt(signed=False, label="UInt32")}, name="NETINFOSTRUCT", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpProvider", "lpNetInfoStruct"]),
        # 
        'WNetGetLastErrorA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpError", "lpErrorBuf", "nErrorBufSize", "lpNameBuf", "nNameBufSize"]),
        # 
        'WNetGetLastErrorW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpError", "lpErrorBuf", "nErrorBufSize", "lpNameBuf", "nNameBufSize"]),
        # 
        'MultinetGetConnectionPerformanceA': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="NETRESOURCEA", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwSpeed": SimTypeInt(signed=False, label="UInt32"), "dwDelay": SimTypeInt(signed=False, label="UInt32"), "dwOptDataSize": SimTypeInt(signed=False, label="UInt32")}, name="NETCONNECTINFOSTRUCT", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpNetConnectInfoStruct"]),
        # 
        'MultinetGetConnectionPerformanceW': SimTypeFunction([SimTypePointer(SimStruct({"dwScope": SimTypeInt(signed=False, label="NET_RESOURCE_SCOPE"), "dwType": SimTypeInt(signed=False, label="NET_RESOURCE_TYPE"), "dwDisplayType": SimTypeInt(signed=False, label="UInt32"), "dwUsage": SimTypeInt(signed=False, label="UInt32"), "lpLocalName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpRemoteName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpComment": SimTypePointer(SimTypeChar(label="Char"), offset=0), "lpProvider": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="NETRESOURCEW", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"cbStructure": SimTypeInt(signed=False, label="UInt32"), "dwFlags": SimTypeInt(signed=False, label="UInt32"), "dwSpeed": SimTypeInt(signed=False, label="UInt32"), "dwDelay": SimTypeInt(signed=False, label="UInt32"), "dwOptDataSize": SimTypeInt(signed=False, label="UInt32")}, name="NETCONNECTINFOSTRUCT", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpNetResource", "lpNetConnectInfoStruct"]),
        # 
        'WNetSetLastErrorA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeBottom(label="Void"), arg_names=["err", "lpError", "lpProviders"]),
        # 
        'WNetSetLastErrorW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeBottom(label="Void"), arg_names=["err", "lpError", "lpProviders"]),
    }

lib.set_prototypes(prototypes)
